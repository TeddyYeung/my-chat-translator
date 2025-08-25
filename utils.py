import streamlit as st

# 대화 출력 함수 (ChatMessage 객체 처리)
def print_message():
    if "messages" in st.session_state and len(st.session_state["messages"]) > 0:
        for chat_message in st.session_state["messages"]:
            st.chat_message(chat_message.role).write(chat_message.content)
