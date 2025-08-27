import streamlit as st
from langchain_core.messages import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from utils import print_message

st.set_page_config(page_title="나만의 Translator 💬", page_icon="💬")

# 메시지 저장용 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 화면 갱신 유도용 플래그
if "reset_flag" not in st.session_state:
    st.session_state["reset_flag"] = False

# UI 상단: 타이틀 및 리셋 버튼
with st.container():
    st.title("나만의 Translator 💬")
    if st.button("🔄 대화내용 초기화"):
        st.session_state["messages"] = []
        st.session_state["reset_flag"] = True

# 리셋 플래그가 켜져 있으면 처리 후 끔
if st.session_state["reset_flag"]:
    st.session_state["reset_flag"] = False
    # 추가적인 리셋 시 처리 로직 가능 (현재는 메시지 비움으로 충분)

# LLM 객체 초기화 (한 번만)
llm = ChatOllama(model="llama3.1:8b", temperature=0)

# Prompt 템플릿 정의
prompt_template_str = """
당신은 친절한 번역가입니다. 사용자의 질문에 간결하게 답변하세요.
{question}
"""
prompt_template = ChatPromptTemplate.from_template(prompt_template_str)

# 기존 대화 메시지 출력
print_message()

# 사용자 입력 대기 및 처리
user_input = st.chat_input("메시지를 입력해 주세요.")

if user_input:
    # 사용자 메시지 저장 및 화면에 출력
    st.chat_message("user").write(user_input)
    user_msg = ChatMessage(role="user", content=user_input)
    st.session_state["messages"].append(user_msg)

    # LLM 실행
    output = llm.invoke(prompt_template.format_prompt(question=user_input).to_string())

    # AI 응답 저장 및 화면 출력
    with st.chat_message("assistant"):
        st.write(output.content)
        assistant_msg = ChatMessage(role="assistant", content=output.content)
        st.session_state["messages"].append(assistant_msg)
