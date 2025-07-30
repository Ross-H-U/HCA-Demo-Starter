import streamlit as st

# App Title
st.set_page_config(page_title="Loom Video Player", layout="centered")

st.title("Health Universe Video Hub")

# Logo Upload Section
st.subheader("Upload Health Universe Logo")
logo_file = st.file_uploader("Upload your Health Universe logo (PNG/JPG preferred)", type=["png", "jpg", "jpeg"])
if logo_file:
    st.image(logo_file, caption="Health Universe Logo", use_column_width=True)

# Video Section
st.subheader("Featured Loom Video")
st.markdown(
    """
    <iframe 
        src="https://www.loom.com/embed/7d92c32a5d2b457887f0b9665b58ba08?sid=6e32b4f4-ed7b-4218-a194-833ebbeab40b" 
        frameborder="0" 
        webkitallowfullscreen 
        mozallowfullscreen 
        allowfullscreen 
        style="width:100%;height:500px;">
    </iframe>
    """,
    unsafe_allow_html=True,
)

# Video Description
st.subheader("Video Description")
st.markdown(
    """
    **Video Title:** Health Universe - Quick Start Video  
    **Description:**  
    This video provides a breif introduction to adding new users and getting started with deploying a quick streamlit application.

    **[Link to Documentation](https://docs.healthuniverse.com/overview)**
    """
)
