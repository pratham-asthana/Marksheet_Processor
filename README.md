# Marksheet Processor 📟🔍

A Python-based deep learning project to **automatically detect and parse text from marksheet images** using **YOLOv8**, **custom dataset annotation**, and **OCR techniques**. This system processes scanned student marksheets and extracts structured tabular data, ready for analysis or automation.

---

## 📸 Output Demo

![Output Screenshot](https://github.com/pratham-asthana/Marksheet_Processor/blob/main/SS.png)

---

## 🧠 Features

* 🧾 Object detection on scanned marksheet fields using YOLOv8.
* 🔤 Text recognition using OCR tools (e.g., Tesseract or PaddleOCR).
* 🧪 Custom dataset training and label splitting utilities.
* 📂 Organized data pipelines: raw → labeled → split.
* 📊 Result visualization and verification support.

---

## 🗂️ Project Structure

```
Marksheet_Processor/
├── dataset/                # Labeled images and annotation files
├── datasett_split/         # Training and validation split datasets
├── documentation/          # Supporting docs and presentation
│   └── Create Marksheet Parsing.pptx
├── raw_data(images)/       # Raw unannotated image data
├── runs/train/             # YOLOv8 training logs and model outputs
├── .gitattributes          # Git settings
├── SS.png                  # Output screenshot of the final result
├── data.yaml               # YOLO data configuration file
├── data_splitter.py        # Python script to split dataset
├── rename.py               # File renaming utility
├── Marksheet_parsing.ipynb # Main notebook for inference and integration
├── model_training.ipynb    # Notebook to train YOLO model on dataset
├── yolov8n.pt              # YOLOv8 trained model weights
└── README.md               # Project documentation
```

---

## ⚙️ Installation

### ✅ Prerequisites

* Python 3.8+
* PyTorch and Ultralytics YOLOv8
* OpenCV, Pandas, Matplotlib

### 📦 Install dependencies

```bash
pip install ultralytics opencv-python pandas matplotlib
```

---

## 🚀 Usage

### 1. Train the model

```bash
# Inside model_training.ipynb or using CLI
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=50)
```

### 2. Inference on new marksheets

Run the inference code in `Marksheet_parsing.ipynb` to detect and extract text from input images.

---

## 📁 Dataset Preparation

* Place raw images in `raw_data(images)/`
* Annotate them using tools like Roboflow or CVAT
* Export to YOLOv8 format and place in `dataset/`
* Use `data_splitter.py` to create train/val split in `datasett_split/`

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use and modify for educational or commercial purposes.

---

## 👨‍💻 Author

**Pratham Asthana**
📧 [prathamasthana04@gmail.com](mailto:prathamasthana04@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/pratham-asthana-243133265) • [GitHub](https://github.com/pratham-asthana)

---

## 🤝 Contributions

If you find bugs or want to suggest improvements, feel free to open issues or submit pull requests.
