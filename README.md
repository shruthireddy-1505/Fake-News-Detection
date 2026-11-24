# 📰 Fake News Detection Using Deep Learning

## 🚀 Live Demo

**Try the application here:**  
[Fake News Detection – Live Application](https://fake-news-detection-hssdtyc3bswng2jkdhy7zh.streamlit.app/)

## 📌 Project Overview

Fake News Detection is a machine learning-based web application that identifies whether a given news article is **Fake or Real**.

The project uses Natural Language Processing (NLP) and a trained LSTM-based deep learning model to analyze news text and predict its authenticity.

Users can enter news content into the application and receive a prediction along with a confidence score.

## ✨ Features

- Detects whether news is Fake or Real.
- Uses Natural Language Processing for text preprocessing.
- Removes special characters and English stopwords.
- Uses a trained deep learning model for prediction.
- Displays prediction confidence percentage.
- Simple and user-friendly Streamlit interface.
- Accessible online through Streamlit Community Cloud.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **NLP:** NLTK
- **Model:** LSTM (Bidirectional LSTM)
- **Tokenization:** Keras Tokenizer
- **Frontend:** Streamlit
- **Libraries:** NumPy, Pandas, Scikit-learn

## ⚙️ How It Works

1. User enters a news article in the text area.
2. The input text is converted to lowercase.
3. Special characters and numbers are removed.
4. English stopwords are removed using NLTK.
5. The processed text is converted into sequences using the saved tokenizer.
6. The sequences are padded to a fixed length of 100.
7. The trained LSTM model predicts the news category.
8. The application displays the result as Fake or Real with a confidence percentage.

## 📂 Project Structure

```text
Fake-News-Detection/
│
├── app.py
├── model.h5
├── tokenizer.pkl
├── requirements.txt
└── README.md
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Fake-News-Detection.git
```

### 2. Navigate to the project folder

```bash
cd Fake-News-Detection
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

### 5. Open in your browser

```text
http://localhost:8501
```

## 📊 Model Prediction

The trained model generates a prediction score between 0 and 1.

- Score greater than or equal to 0.5: Fake News
- Score less than 0.5: Real News

The application also displays the confidence percentage for the predicted category.

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live URL:**  
https://fake-news-detection-hssdtyc3bswng2jkdhy7zh.streamlit.app/

## 🎯 Project Objective

The main objective of this project is to explore the application of Natural Language Processing and Deep Learning in identifying potentially misleading news content.

## 👩‍💻 Author

**Shruthi**

B.Tech – Computer Science and Engineering

---

*This project was developed as an academic mini project to demonstrate the use of NLP and deep learning for fake news classification.*
