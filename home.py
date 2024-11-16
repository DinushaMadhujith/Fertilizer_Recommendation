from PIL import Image, UnidentifiedImageError
import streamlit as st

def show_home():
    # Set the inline CSS styles directly in the body
    st.markdown("""
    <style>
    body {
        background-color: #ADD8E6; /* Set page background color to light blue */
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with inline CSS
    st.markdown("<h1 style='color: darkgreen; text-align: center;'>Welcome to the Fertilizer Recommendation App</h1>", unsafe_allow_html=True)

    # Display an image
    try:
        image = Image.open("images.jpeg")
        st.image(image, use_column_width=True)
    except UnidentifiedImageError:
        st.error("Could not identify the image file. Please check the file format and path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

    # Introduction text with inline CSS
    st.markdown("""
        <p style='color: black; text-align: justify;'>Agriculture is the backbone of sustainable development, and we’re here to support it with precision.</p>
        <p style='color: black; text-align: justify;'>Our app is designed to help farmers and agronomists choose the right fertilizer for their crops, based 
        on soil composition, crop type, and environmental conditions. By bridging technology with agriculture, 
        we aim to boost crop yields, enhance soil health, and contribute to food security.</p>
        <p style='color: black; text-align: justify;'><strong>Explore</strong> our prediction tools, browse product recommendations, and make informed decisions for a greener tomorrow!</p>
    """, unsafe_allow_html=True)

