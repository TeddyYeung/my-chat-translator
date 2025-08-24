import streamlit as st
from utils import print_message
from langchain_core.messages import ChatMessage

st.set_page_config(page_title="나만의 Translator 💬", page_icon="💬")
st.title("나만의 Translator 💬")

# Session State 메시지 리스트 초기화(일관된 key 사용 및 구조적 관리)
if "messages" not in st.session_state:
    st.session_state["messages"] = []

print_message()

# 사용자 입력 처리 및 세션 상태 업데이트
user_input = st.chat_input("메세지를 입력해 주세요.")
if user_input:
    # 메시지 추가: "user" 역할 추가
    st.chat_message("user").write(user_input)
    st.session_state["messages"].append(ChatMessage(role="user", content=user_input))

    # 예시: assistant 응답 메시지 (실전 서비스에선 모델 inference로 교체 가능)
    with st.chat_message("assistant"):
        assistant_reply = f"MY INPUT: {user_input}"
        st.write(assistant_reply)
        st.session_state["messages"].append(ChatMessage(role="assistant", content=assistant_reply))
