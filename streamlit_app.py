import streamlit as st

st.set_page_config(
    page_title="My Streamlit Demo",
    page_icon="💻"
)

st.title("💻 My Streamlit Demo")

st.write("Welcome to my first Streamlit application!")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello, {name}! 👋")

number = st.slider(
    "Choose a number",
    1,
    100,
    50
)

st.write("You selected:", number)

if st.button("Click Me"):
    st.balloons()
    st.success("Button clicked successfully! 🎉")
