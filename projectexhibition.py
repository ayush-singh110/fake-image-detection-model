import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("C:\\Users\\Ayush singh\\Downloads\\Classifcation_model.h5")
    return model

model = load_model()

# Define the Streamlit app
st.title("Fake Image Detector")
st.header("Upload an Image for Prediction")

# File uploader to take image input
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    st.write("Processing the image...")
    image = image.resize((256, 256))  # Resize image to match the model's input size
    image_array = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
    
    if len(image_array.shape) == 2:  # If grayscale, add channel dimension
        image_array = np.expand_dims(image_array, axis=-1)
    
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(image_array)
    st.subheader("Prediction Result")
    st.write(f"Prediction: {prediction}")
else:
    st.write("Please upload an image file to make a prediction.")
