import streamlit as st

st.set_page_config(page_title="Buttons Demo", page_icon = "▶️")

st.title("Buttons and Interactions Demo")

if st.button("Click me"):
    st.write("Button was clicked!")

if st.button("Important Action", type = "primary"):
    st.write("Primary button clicked!")

st.button("You can't press this!", disabled = True)

show_extra = st.checkbox("Show extra message.")
if show_extra:
    st.write("Here's your extra message: Have a nice day!")