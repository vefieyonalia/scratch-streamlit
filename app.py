import streamlit as st

st.set_page_config(page_title="My Scratch Game", page_icon="🎮", layout="centered")

st.title("🎮 My Scratch Project")
st.write("Mainkan game langsung di bawah:")

st.markdown(
    """
    <iframe src="https://scratch.mit.edu/projects/1210664748/embed"
    allowtransparency="true" width="485" height="402" frameborder="0"
    scrolling="no" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)
