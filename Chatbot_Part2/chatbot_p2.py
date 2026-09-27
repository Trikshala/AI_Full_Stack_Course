import streamlit as st
from ollama import chat

st.set_page_config(page_title = "JimmyBot", page_icon="🤖")
st.title("LlamaBot - here to talk!")

personality = "You are a charming and friendly person named Llama. Answer warmly. Keep the answers within one sentence."

personality_2 = "You are a funny and quirky thief. Answer accordingly. Keep the answers within one sentence."

if "history" not in st.session_state:
    st.session_state.history = [{"role" : "system", "content" : personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg = None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0], icon = st.session_state.toast_msg[1])
    st.session_state.toast_msg = None

with st.sidebar:
    st.header("Chat Controls")
    if st.button("Clear Conversation"):
        st.session_state.history = [{"role" : "system", "content" : personality}]
        st.session_state.toast_msg = ("Conversation cleared!", "🗑️")
        st.rerun()
    if st.button("Change Personality"):
        st.session_state.history[0]["content"] = personality_2
        st.session_state.toast_msg = ("Personality changed!", "🎭")
        st.rerun()

with st.chat_message("assistant"):
    st.write("Hi, there! My name is Llama. Ask me a question to get started.")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Type something...")
if question:
    st.session_state.history.append({"role" : "user", "content" : question})
    
    with st.chat_message("user"):
        st.write(question)

    try:
        with st.spinner("Thinking..."):
            response = chat(model = "llama3.2", messages = st.session_state.history)
        reply = response["message"]["content"]
        st.session_state.history.append({"role" : "assistant", "content": reply})

        with st.chat_message("ai"):
            st.write(reply)
    except Exception as e:
        st.write("Error while responding. Is ollama running?")