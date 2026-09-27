import streamlit as st

st.set_page_config(page_title = "Text Input Demo", page_icon = "📃")

st.title("Text Input Demo")

name = st.text_input("Enter your name:", value="Guest!", placeholder = "e.g. Sandhya")
st.write(f"Hello, {name}!")

secret = st.text_input("Enter a secret word:", type = "password")
st.write(f"Your secret has {len(secret)} characters.")

comments = st.text_area("Any additional comments?", height=150)
st.write(f"You wrote {len(comments)} characters.")