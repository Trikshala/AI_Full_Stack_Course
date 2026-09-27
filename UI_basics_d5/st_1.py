import streamlit as st

st.set_page_config(page_title = "My first app", page_icon = "🤖",layout = "centered")

st.title("🤖 My First App")

st.write("This is plain text using st.write()")

st.markdown("This is **bold**, this is *italic*, and this is :blue[coloured text].")

st.write("You can even add a divider below:")

st.divider()