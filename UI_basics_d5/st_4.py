import streamlit as st
import time

st.markdown("""
    <style>
    .stApp {
        background-color: #5D100A;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Chat UI Demo", page_icon="💬")
st.title("💬 Chat UI Demo")

with st.chat_message("assistant"):
    st.write("Hi, Ask me anything!")

user_message = st.chat_input("Type a message...")
if user_message:
    with st.chat_message("user"):
        st.write(user_message)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1.5)
        st.write(f"You said: '{user_message}'. I'm just a demo, not a real AI yet!")