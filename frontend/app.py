import streamlit as st
import requests
from PIL import Image
import io

# FastAPI backend URL
API_URL = "http://127.0.0.1:8090/predict"
USERNAME = "admin"
PASSWORD = "password123"

# Streamlit UI
st.title("CIFAR-10 Image Classification")
st.write("Upload an image to classify it using a pre-trained ResNet-18 model.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        # Read file as bytes first
        img_bytes = uploaded_file.read()
        
        # Ensure the file is not empty
        if len(img_bytes) < 10:  # Arbitrary threshold for invalid images
            st.error("Not In Scope or not able to classify")
        else:
            # Open image from bytes
            image = Image.open(io.BytesIO(img_bytes))

            # Convert to RGB if necessary
            if image.mode == "RGBA":
                image = image.convert("RGB")

            # Display uploaded image
            st.image(image, caption="Uploaded Image", use_container_width=True)

            # Send request to FastAPI
            with st.spinner("Predicting..."):
                response = requests.post(
                    API_URL,
                    files={"file": ("filename", img_bytes, "image/jpeg")},
                    auth=(USERNAME, PASSWORD)  # Basic Auth
                )

            # Display prediction result
            if response.status_code == 200:
                result = response.json()
                st.success(f"Predicted Class: **{result['predicted_class']}**")
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

    except Exception as e:
        st.error(f"Error: Unable to process the image. Details: {e}")
