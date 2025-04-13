import spacy
import joblib
import os

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Load trained model and label encoder
model = joblib.load("models/name_classifier.pkl")
le = joblib.load("models/label_encoder.pkl")

# Function to classify the name using the saved model
def classify_name(name: str) -> str:
    # Preprocess the name
    name = name.strip()
    name_vector = nlp(name).vector.reshape(1, -1)

    # Ensure the vector is the correct shape -- had this error before
    if name_vector.shape[1] != 300:
        raise ValueError(f"Expected 300 features, got {name_vector.shape[1]}.")

    # Predict and decode label
    predicted_label = model.predict(name_vector)
    label = le.inverse_transform(predicted_label)[0]
    return label
