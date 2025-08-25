import streamlit as st
from langchain_core.messages import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from utils import print_message

st.set_page_config(page_title="나만의 Translator 💬", page_icon="💬")
st.title("나만의 Translator 💬")

# 세션 상태 메시지 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Ollama LLM 객체 한 번만 초기화
llm = ChatOllama(model="llama3.2:3b", temperature=0)

# Prompt 템플릿 정의
prompt_template_str = """
당신은 친절한 번역가입니다. 사용자의 질문에 간결하게 답변하세요.
{question}
"""
prompt_template = ChatPromptTemplate.from_template(prompt_template_str)


user_input = st.chat_input("메시지를 입력해 주세요.")

print_message()  # 기존 메시지 화면에 출력

if user_input:
    # 사용자 메시지 저장 및 화면 출력
    st.chat_message("user").write(user_input)
    user_msg = ChatMessage(role="user", content=user_input)
    st.session_state["messages"].append(user_msg)

    # prompt 템플릿에 질문 변수 할당하여 체인 호출
    output = llm.invoke(prompt_template.format_prompt(question=user_input).to_string())

    # AI 응답 메시지 저장 및 화면 출력
    with st.chat_message("assistant"):
        st.write(output.content)
        assistant_msg = ChatMessage(role="assistant", content=output.content)
        st.session_state["messages"].append(assistant_msg)
