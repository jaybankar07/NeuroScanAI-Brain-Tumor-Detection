import streamlit as st
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="NeuroScanAI", page_icon="🧠")

# Title and subtitle
st.title("🧠 NeuroScanAI")
st.subheader("Brain Tumor MRI Classifier")
st.markdown("Upload a brain MRI image to check for the presence of a tumor using AI (model coming soon).")

# File uploader
uploaded_file = st.file_uploader("📤 Upload MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="🖼️ Uploaded MRI Image", use_column_width=True)

    # Placeholder for prediction result (UI only)
    st.markdown("### 🔍 Prediction Result (UI Only)")
    st.info("🤖 Model prediction will be displayed here once connected.")

# Footer
st.markdown("---")
st.caption("Developed by Jay Bankar | AI & Data Science | Sanjivani University")
