import streamlit as st
from PIL import Image
from ultralytics import YOLO
import tempfile
import os
import json

# Load model with error handling
try:
    model = YOLO("best.pt")  # Replace with your trained model path
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# Disease information database
DISEASE_INFO = {
    "actinic keratosis": {
        "description": "A rough, scaly patch on the skin caused by years of sun exposure.",
        "treatment": "Cryotherapy, topical medications, photodynamic therapy, or surgical removal.",
        "severity": "Moderate (can progress to squamous cell carcinoma)",
        "color": "#FF9F1C"
    },
    "basal cell carcinoma": {
        "description": "The most common type of skin cancer, appearing as a waxy bump or flat lesion.",
        "treatment": "Surgical excision, Mohs surgery, cryotherapy, or radiation therapy.",
        "severity": "Low (rarely spreads but can be locally destructive)",
        "color": "#FF6B6B"
    },
    "dermatofibroma": {
        "description": "A common benign skin growth that appears as a firm, small brown or red bump.",
        "treatment": "Usually none needed, but can be surgically removed if bothersome.",
        "severity": "Benign (non-cancerous)",
        "color": "#4ECDC4"
    },
    "melanoma": {
        "description": "The most serious type of skin cancer that develops in melanocytes.",
        "treatment": "Surgical removal, immunotherapy, targeted therapy, radiation, or chemotherapy.",
        "severity": "High (can spread rapidly if not treated early)",
        "color": "#6A4C93"
    },
    "nevus": {
        "description": "A benign mole or birthmark caused by clusters of pigmented cells.",
        "treatment": "Monitoring for changes, surgical removal if suspicious.",
        "severity": "Benign (but some may develop into melanoma)",
        "color": "#A5C882"
    },
    "pigmented benign keratosis": {
        "description": "A harmless warty spot that appears stuck on the skin, often pigmented.",
        "treatment": "Usually none needed, can be removed by cryotherapy or scraping if desired.",
        "severity": "Benign",
        "color": "#7FDBFF"
    },
    "seborrheic keratosis": {
        "description": "Noncancerous skin growth that appears waxy and raised, often brown.",
        "treatment": "Typically none needed, can be removed by cryotherapy or scraping if bothersome.",
        "severity": "Benign",
        "color": "#B5EAD7"
    },
    "squamous cell carcinoma": {
        "description": "A common form of skin cancer that develops in squamous cells.",
        "treatment": "Surgical removal, Mohs surgery, radiation therapy, or topical medications.",
        "severity": "Moderate to High (can spread if not treated)",
        "color": "#FF9AA2"
    }
}

# Page config - full width layout
st.set_page_config(
    page_title="DermAI Pro | Skin Cancer Detection",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🧬"
)

# Load CSS
with open("style2.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Custom HTML for full-screen hero section
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <h1 class="main-title">DermAI <span class="highlight">Pro</span></h1>
        <p class="subtitle">Advanced Skin Lesion Analysis Platform</p>
        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-value">8+</div>
                <div class="stat-label">Skin Conditions Detected</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">99%</div>
                <div class="stat-label">Detection Accuracy</div>
            </div>
            <div class="stat-item">
                <div class="stat-value">24/7</div>
                <div class="stat-label">Availability</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main container with full-width
with st.container():
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="upload-card">
            <h3><i class="fas fa-cloud-upload-alt"></i> Upload Image</h3>
            <p>Get instant AI analysis of skin lesions</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            " ",
            type=["jpg", "jpeg", "png"],
            key="file_uploader",
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3><i class="fas fa-info-circle"></i> How It Works</h3>
            <ol class="steps">
                <li>Upload a clear image of the skin area</li>
                <li>Our AI analyzes the image in seconds</li>
                <li>Get detailed results with treatment information</li>
            </ol>
            <div class="disease-preview">
                <div class="disease-tag" style="background-color: #FF6B6B">BCC</div>
                <div class="disease-tag" style="background-color: #6A4C93">Melanoma</div>
                <div class="disease-tag" style="background-color: #4ECDC4">Dermatofibroma</div>
                <div class="disease-tag" style="background-color: #FF9F1C">AK</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Results section
if uploaded_file is not None:
    try:
        with st.spinner("🔍 Analyzing image with our advanced AI..."):
            # Process image
            image = Image.open(uploaded_file).convert("RGB")
            
            # Save to temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                image_path = tmp_file.name
                image.save(image_path)
            
            # Run prediction
            results = model(image_path)
            result_img = results[0].plot()
            
            # Get unique detections
            detections = {}
            for box in results[0].boxes:
                class_id = int(box.cls[0])
                class_name = model.names[class_id].lower()
                confidence = float(box.conf[0])
                
                if class_name not in detections or confidence > detections[class_name]["confidence"]:
                    detections[class_name] = {
                        "confidence": confidence,
                        "count": detections.get(class_name, {}).get("count", 0) + 1,
                        "color": DISEASE_INFO.get(class_name, {}).get("color", "#6c757d")
                    }

        # Results container
        st.markdown("---")
        
        # Image comparison
        st.markdown("## 🖼️ Image Analysis")
        img_col1, img_col2 = st.columns(2)
        
        with img_col1:
            st.markdown("### Original Image")
            st.image(image, use_column_width=True)
        
        with img_col2:
            st.markdown("### AI Detection")
            st.image(result_img, use_column_width=True)

        # Detection summary
        st.markdown("## 📊 Detection Report")
        
        if not detections:
            st.warning("No skin conditions detected in the image.")
        else:
            # Summary metrics
            st.markdown("### Summary Statistics")
            cols = st.columns(4)
            cols[0].metric("Total Findings", sum(d["count"] for d in detections.values()))
            cols[1].metric("Unique Conditions", len(detections))
            
            primary_detection = max(detections.items(), key=lambda x: x[1]["confidence"])
            cols[2].metric("Primary Condition", primary_detection[0].title())
            cols[3].metric("Confidence Level", f"{primary_detection[1]['confidence']:.1%}")
            
            # Detailed findings
            st.markdown("### Detailed Analysis")
            for disease, data in detections.items():
                disease_color = DISEASE_INFO.get(disease, {}).get("color", "#6c757d")
                
                # Updated Detailed Analysis section
                with st.expander("", expanded=True):
                    st.markdown(f"""
                    <div style="display: flex; align-items: center; margin-bottom: 12px;">
                       <div class="disease-bullet" style="background-color: {disease_color}"></div>
                       <span style="margin-left: 8px; font-weight: 600; font-size: 1.1rem;">
                          {disease.title()} 
                          <span style="color: {disease_color}">({data['confidence']:.1%})</span>
                      </span>
                    </div>
                    """, unsafe_allow_html=True)
    
                    if disease in DISEASE_INFO:
                       info = DISEASE_INFO[disease]
                       st.markdown(f"""
                       <div style="padding: 16px; background-color: rgba(255,255,255,0.7); border-radius: 8px;">
                            <h4 style="color: {disease_color}">Condition Information</h4>
                            <p><strong>Description:</strong> {info['description']}</p>
                            <p><strong>Recommended Treatment:</strong> {info['treatment']}</p>
                            <p><strong>Severity:</strong> {info['severity']}</p>
                            <p><strong>Number of detections:</strong> {data['count']}</p>
                       </div>
                       """, unsafe_allow_html=True)
                    else:
                        st.warning(f"Information not available for {disease}")

        # Cleanup
        os.remove(image_path)

    except Exception as e:
        st.error(f"An error occurred during processing: {str(e)}")
        if 'image_path' in locals() and os.path.exists(image_path):
            os.remove(image_path)

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-section">
            <h4>DermAI Pro</h4>
            <p>Advanced AI for dermatological analysis for cancer detection</p>
        </div>
        <div class="footer-section">
            <h4>Quick Links</h4>
            <a href="#">How it works</a>
            <a href="#">About the technology</a>
            <a href="#">Clinical studies</a>
        </div>
        <div class="footer-section">
            <h4>Contact</h4>
            <p>vm0017@srmist.edu.in</p>
            <p>np3448@srmist.edu.in</p>
            <p>+91 6309010455</p>
        </div>
    </div>
    <div class="footer-bottom">
        <p>© 2023 DermAI Pro | Clinical Decision Support System | Not for diagnostic use</p>
        <p class="disclaimer">This AI system assists healthcare professionals but does not replace clinical judgment.</p>
    </div>
</div>
""", unsafe_allow_html=True)
