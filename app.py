import streamlit as st
import pickle
import re
import nltk
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load
model = load_model("model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_SEQUENCE_LENGTH = 100
stop = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop]
    return " ".join(words)

def predict_news(text):
    text = preprocess(text)
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)

    pred = model.predict(padded, verbose=0)[0][0]

    if pred >= 0.5:
        label = "Fake"
    else:
        label = "Real"

    return label, pred

st.title("📰 Fake News Detection")

user_input = st.text_area("Enter News Text")

if st.button("Predict"):
    if user_input.strip() != "":
        label, prob = predict_news(user_input)

        confidence = prob if label == "Fake" else (1 - prob)

        st.success(f"Prediction: {label}")
        st.write(f"Confidence: {round(confidence*100,2)}%")
        st.write(f"Raw Prediction Value: {prob}")  # debug
    else:
        st.warning("Please enter some text")