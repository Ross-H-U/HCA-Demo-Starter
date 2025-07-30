import streamlit as st
from PIL import Image

# App Title and Layout
st.set_page_config(page_title="Health Universe - Quick Start Video", layout="centered")

# Display Logo
logo = Image.open("02_HU-Logo_Horizontal.png")  # Ensure the file is in the app directory
st.image(logo, use_container_width=True)

# Main Title
st.title("Health Universe - Quick Start Video")

# Loom Video Embed
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

# Footer Description
st.markdown(
    """
    **Video Title:** Health Universe - Quick Start Video  

    **Description:**  
    This video provides a brief introduction to adding new users and getting started 
    with deploying a quick Streamlit application.

    **[Link to Documentation](https://docs.healthuniverse.com/overview)**
    """,
    unsafe_allow_html=True
)
