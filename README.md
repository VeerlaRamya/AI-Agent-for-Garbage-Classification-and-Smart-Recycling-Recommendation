# ♻️ AI Garbage Classification

An AI-based garbage classification system that uses **Deep Learning**, **EfficientNet-B3**, and a **Streamlit web application** to identify the type of garbage from an uploaded image and provide a suitable recycling recommendation.

The system classifies garbage into six categories:

* 📦 **Cardboard**
* 🍾 **Glass**
* 🥫 **Metal**
* 📄 **Paper**
* 🧴 **Plastic**
* 🗑️ **Trash**

> **Note:** This project is developed for educational and demonstration purposes.

---

## 📌 Project Overview

Garbage needs to be properly identified and categorized before it can be appropriately managed or recycled.

This project demonstrates how **computer vision and deep learning** can be used to automatically identify garbage from an image.

The user uploads an image through the Streamlit application. The image is processed and passed to a trained **EfficientNet-B3** model. The model predicts the garbage category and provides a confidence score.

Based on the predicted category, the application also provides a **smart recycling recommendation** with practical recycling steps.

---

## ✨ Key Features

* ♻️ AI-based garbage image classification
* 🧠 EfficientNet-B3 deep learning model
* 📷 Image upload and prediction
* 🎯 Six garbage categories
* 📊 Prediction probability for each class
* 📈 Prediction confidence score
* 🔴 Low-confidence warning
* ♻️ Smart recycling recommendations
* ✅ Recommended recycling steps
* 💡 Smart recycling tips
* 🌐 Streamlit-based web application
* 📱 Simple user-friendly interface

---

## 🏗️ System Workflow

```text
                  User
                   │
                   ▼
          Upload Garbage Image
                   │
                   ▼
           Image Preprocessing
             300 × 300 pixels
                   │
                   ▼
            EfficientNet-B3
                   │
                   ▼
        Class Probability Scores
                   │
                   ▼
         Highest Probability Class
                   │
                   ▼
          Predicted Garbage Type
                   │
            ┌──────┴──────┐
            ▼             ▼
       Confidence     Class Result
            │             │
            └──────┬──────┘
                   ▼
       Recycling Recommendation
                   │
                   ▼
             Streamlit UI
                   │
                   ▼
              User Result
```

---

## 📊 Garbage Categories

The model is trained to classify images into six categories.

| Category  | Description                        |
| --------- | ---------------------------------- |
| Cardboard | Cardboard-based waste              |
| Glass     | Glass-based waste                  |
| Metal     | Metal-based waste                  |
| Paper     | Paper-based waste                  |
| Plastic   | Plastic-based waste                |
| Trash     | General non-recyclable/other waste |

---

# 📊 Dataset

The project uses a garbage image dataset containing six different categories of waste.

### Garbage Categories

- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

### Dataset Distribution

| Category | Number of Images |
|---|---:|
| Cardboard | 403 |
| Glass | 501 |
| Metal | 410 |
| Paper | 594 |
| Plastic | 482 |
| Trash | 137 |
| *Total* | *2527* |

The dataset contains *2527 images* across six garbage categories.

The dataset is divided into training and validation data using an *80/20 split*.

Approximately:

- Training Images: 2024
- Validation Images: 503

### Dataset Download

The complete dataset can be downloaded from Kaggle:

👉 [Download Garbage Classification Dataset](https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification)

After downloading, extract the dataset and place it inside the project as:

```text
dataset/
├── cardboard/
├── glass/
├── metal/
├── paper/
├── plastic/
└── trash/


### If you specifically want to upload the 2527 images to GitHub

*41.3 MB is below GitHub's 100 MB per-file limit*, but GitHub recommends keeping repositories much smaller, and 2,527 separate files can make the repository unnecessarily heavy.

For your *college/project GitHub*, I recommend the first approach. Keep the dataset locally and upload the trained garbage_model.keras plus your source code.

---

## 🧹 Data Preparation

The project uses TensorFlow/Keras to load the image dataset.

Images are resized to:

```text
300 × 300 pixels
```

The dataset is divided into:

```text
80% → Training Dataset
20% → Validation Dataset
```

A fixed random seed of `42` is used to maintain consistent dataset splitting.

```python
IMG_SIZE = (300, 300)
BATCH_SIZE = 32
SEED = 42
```

---

## 🧠 Deep Learning Model

The project uses **EfficientNet-B3** for image classification.

EfficientNet-B3 is a convolutional neural network architecture designed for image classification. It extracts visual features from the input image and uses those features to determine which garbage category the image belongs to.

### Model Input

```text
300 × 300 RGB Image
```

### Model Output

The model produces six class probabilities:

```text
Cardboard
Glass
Metal
Paper
Plastic
Trash
```

The class with the highest probability is selected as the final prediction.

---

## 🎯 Prediction Process

For every uploaded image, the model produces a probability for each garbage category.

Example:

```text
Cardboard   → 13.90%
Glass       →  0.04%
Metal       →  0.04%
Paper       → 85.61%
Plastic     →  0.32%
Trash       →  0.09%
```

Since **Paper** has the highest probability:

```text
Predicted Class: Paper
Confidence: 85.61%
```

The probabilities represent the model's prediction for each possible class. They do **not** represent the percentage of physical materials present in the image.

---

## 📈 Model Performance

The model was evaluated using the validation dataset.

### Final Result

| Metric              |     Result |
| ------------------- | ---------: |
| Validation Accuracy | **90.30%** |
| Validation Loss     | **0.3076** |
| Image Size          |  300 × 300 |
| Number of Classes   |          6 |
| Batch Size          |         32 |
| Training Epochs     |         10 |

The latest training run achieved **90.30% validation accuracy**.

> Validation accuracy represents the model's performance on the validation portion of the dataset and should not be interpreted as a guarantee that every new image will be classified correctly.

---

## 📊 Training Graphs

The project generates two graphs during training.

### Training vs Validation Accuracy

```text
accuracy_graph.png
```

This graph shows how training accuracy and validation accuracy change across epochs.

### Training vs Validation Loss

```text
loss_graph.png
```

This graph shows how training loss and validation loss change across epochs.

---

## 🔴 Confidence-Based Prediction

The application displays the confidence associated with the predicted class.

For example:

```text
Confidence: 85.61%

🟢 High Confidence
The model is highly confident in this prediction.
```

For lower-confidence predictions, the application displays a warning.

Example:

```text
Confidence: 49.43%

🔴 Low Confidence
The model is not very certain about this prediction.
Try uploading a clearer image.
```

This allows the user to understand that an AI prediction may sometimes be uncertain.

---

## ♻️ Smart Recycling Recommendation

After classification, the application provides a recycling recommendation based on the predicted garbage category.

### Example: Plastic

```text
Category: Recyclable

Clean and dry the plastic item before recycling.
```

### Recommended Steps

* Remove food or liquid residue.
* Separate caps if required by the local recycling system.
* Place clean plastic in the appropriate recycling bin.
* Avoid recycling heavily contaminated plastic.

### Smart Tip

Reuse plastic containers whenever possible before recycling.

Similar recommendations are provided for the other garbage categories.

---

## 🌐 Streamlit Web Application

The user interface is developed using **Streamlit**.

The application allows the user to:

1. Upload a garbage image.
2. View the uploaded image.
3. Click **Analyze Garbage**.
4. Get the predicted garbage category.
5. View the prediction confidence.
6. View probabilities for all six classes.
7. Receive a recycling recommendation.
8. View recommended recycling steps and a smart tip.

---

## 🖥️ Application Prediction Flow

```text
User
 │
 ▼
Upload Image
 │
 ▼
Streamlit Application
 │
 ▼
Image Preprocessing
 │
 ▼
EfficientNet-B3 Model
 │
 ▼
Prediction Probabilities
 │
 ▼
Highest Probability
 │
 ▼
Garbage Category
 │
 ▼
Confidence Score
 │
 ▼
Recycling Recommendation
 │
 ▼
Result Displayed
```

---

## 📂 Project Structure

```text
AI-Garbage-Classification/
│
├── dataset/
│   ├── cardboard/
│   ├── glass/
│   ├── metal/
│   ├── paper/
│   ├── plastic/
│   └── trash/
│
├── model.py
├── train.py
├── predict.py
├── streamlit_app.py
├── recommendation.py
│
├── garbage_model.keras
├── accuracy_graph.png
├── loss_graph.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

> The `.venv/` virtual environment and Python cache files are not included in the repository.

---

## 📝 File Description

| File / Folder         | Purpose                                                           |
| --------------------- | ----------------------------------------------------------------- |
| `model.py`            | Defines the EfficientNet-B3 model                                 |
| `train.py`            | Loads the dataset, trains the model and generates training graphs |
| `predict.py`          | Performs prediction on an individual image                        |
| `streamlit_app.py`    | Streamlit web application                                         |
| `recommendation.py`   | Provides recycling recommendations                                |
| `garbage_model.keras` | Saved trained model                                               |
| `accuracy_graph.png`  | Training and validation accuracy graph                            |
| `loss_graph.png`      | Training and validation loss graph                                |
| `dataset/`            | Garbage image dataset                                             |
| `requirements.txt`    | Python dependencies                                               |
| `README.md`           | Project documentation                                             |

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Deep Learning

* TensorFlow
* Keras
* EfficientNet-B3

## Image Processing

* Pillow
* NumPy

## Data Visualization

* Matplotlib

## Web Application

* Streamlit

## Version Control

* Git
* GitHub

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Garbage-Classification.git
```

## 2. Navigate to the Project

```bash
cd AI-Garbage-Classification
```

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate the Virtual Environment

For Windows:

```powershell
.venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The terminal will display a local URL similar to:

```text
http://localhost:8501
```

Open the URL in a web browser.

---

# 🧪 Example Prediction

Example:

```text
Uploaded Image: paper.jpg

Predicted Class: Paper

Confidence: 85.61%
```

The application then provides the appropriate recycling recommendation.

---

# 🎯 Project Objective

The main objective of this project is to demonstrate how **deep learning and computer vision can be used to identify different types of garbage from images**.

The project also demonstrates how an AI prediction can be connected to a simple user-facing application and used to provide practical recycling guidance.

---

# 🔮 Future Enhancements

Possible future improvements include:

* Increasing the size and diversity of the dataset
* Improving classification accuracy
* Adding more garbage categories
* Using a separate test dataset for final evaluation
* Deploying the application online
* Adding real-time camera-based classification
* Adding automated waste sorting hardware
* Improving low-confidence predictions
* Adding more detailed recycling information

These are possible future enhancements and are not currently part of the implemented system.

---

# ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

The recycling recommendations are general guidance. Actual recycling rules can vary depending on the local waste-management system.

---

# 👨‍💻 Project

**AI Garbage Classification**

Developed as a mini-project demonstrating the application of deep learning and computer vision to garbage classification.
---

## 👨‍💻 Developed By

**VEERLA RAMYA**

AI Garbage Classification  
Mini Project  
Department of CSE-DATA SCIENCE

---

## 📜 License

This project is developed for educational and demonstration purposes.

You may view and use the code for learning purposes. Please provide appropriate credit to the original project when reusing or modifying it.

---

