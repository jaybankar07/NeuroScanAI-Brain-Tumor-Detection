import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load trained CNN model
model = load_model('tumor_detector_cnn.h5')

# App title
st.set_page_config(page_title="Brain Tumor Classifier", page_icon="🧠")
st.title("🧠 Brain Tumor MRI Classifier")
st.subheader("Upload an MRI image to detect the presence of a brain tumor.")

# Upload image
uploaded_file = st.file_uploader("Choose an MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded MRI Scan', use_column_width=True)

    # Preprocess image
    img = img.resize((150, 150))  # Match your CNN input shape
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Make prediction
    prediction = model.predict(img_array)[0][0]

    # Show result
    st.markdown("### 🔍 Prediction Result:")
    if prediction > 0.5:
        st.error("⚠️ Tumor Detected")
    else:
        st.success("✅ No Tumor Detected")

