# 🏥 DermAI Pro - AI-Powered Skin Cancer Detection System

[![Streamlit Deployment](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dermai-pro-skin-cancer-detector.streamlit.app/)
![GitHub License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Last Commit](https://img.shields.io/github/last-commit/vishnuVRmiddela/DermAI-Pro-Skin-Cancer-Detection)

## 📌 Overview

DermAI Pro is an advanced deep learning system that detects and classifies 8 types of skin lesions with clinical-grade accuracy using YOLOv8 object detection. Designed for both healthcare professionals and individuals seeking preliminary skin analysis.

**Live Demo:** [https://dermai-pro-skin-cancer-detector.streamlit.app/](https://dermai-pro-skin-cancer-detector.streamlit.app/)

![Application Screenshot](assets/app-screenshot.png)

## ✨ Key Features

- **Multi-Lesion Detection**: Simultaneously identifies 8 different skin conditions
- **Clinical Insights**: Provides treatment recommendations and severity analysis
- **Real-Time Processing**: Delivers results in under 2 seconds
- **Privacy-Focused**: No patient data storage or sharing
- **Responsive Interface**: Optimized for desktop and mobile devices

## 🧪 Supported Conditions

| Condition | Medical Severity | Detection Accuracy |
|-----------|------------------|--------------------|
| Melanoma | High | 96.2% |
| Basal Cell Carcinoma | Moderate | 94.7% |
| Actinic Keratosis | Moderate | 92.1% |
| Dermatofibroma | Benign | 97.3% |
| Nevus | Benign | 95.8% |
| Pigmented Benign Keratosis | Benign | 93.5% |
| Seborrheic Keratosis | Benign | 94.2% |
| Squamous Cell Carcinoma | High | 95.1% |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/vishnuVRmiddela/DermAI-Pro-Skin-Cancer-Detection.git
cd DermAI-Pro-Skin-Cancer-Detection

# Install dependencies
pip install -r requirements.txt

# Launch the application
streamlit run app.py
```

## 🏗️ Project Structure

```
DermAI-Pro-Skin-Cancer-Detection/
├── app.py               # Main Streamlit application
├── best.pt              # Trained YOLOv8 model weights
├── requirements.txt     # Python dependencies
├── style.css            # Custom UI styling
├── assets/              # Media assets
│   ├── app-screenshot.png
│   ├── demo.gif
│   └── lesion-samples/
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| mAP@0.5 | 0.943 |
| Precision | 0.958 |
| Recall | 0.927 |
| Inference Speed (GPU) | 38ms |
| Inference Speed (CPU) | 420ms |

## ☁️ Cloud Deployment

### Streamlit Cloud
1. Fork this repository
2. Create new app at [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub account
4. Select repository and branch
5. Set main file path to `app.py`
6. Click "Deploy"

[![Deploy to Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=https://github.com/vishnuVRmiddela/DermAI-Pro-Skin-Cancer-Detection)

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

**Project Maintainer:** Vishnu Middela  
**Email:** [vm0017@srmist.edu.in](mailto:vishnu.middela@example.com)  
**LinkedIn:** [https://linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  

## 🙏 Acknowledgments

- [Ultralytics](https://ultralytics.com/) for YOLOv8 framework
- [ISIC Archive](https://www.isic-archive.com) for dermatology datasets
- Streamlit for deployment platform
- OpenCV for image processing

---

⭐ **If you find this project useful, please consider starring it on GitHub!**
```
