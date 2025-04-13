import pandas as pd
import spacy
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os
import re

# Load the spaCy model with vectors
nlp = spacy.load("en_core_web_md")

# Load dirty data
df = pd.read_csv("data/names_data_candidate.csv")

#Cleans the data
df['name'] = df['dirty_name'].str.strip().apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
df['label'] = df['dirty_label'].str.strip().str.lower()

#Drop rows with missing values
df.dropna(subset=['name', 'label'], inplace=True)

#Encode the labels
le = LabelEncoder()
y = le.fit_transform(df['label'])

#Create vectors for each name
x= [nlp(name).vector for name in df['name']]

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

os.makedirs('models', exist_ok=True)

joblib.dump(model, 'models/name_classifier.pkl')
joblib.dump(le, 'models/label_encoder.pkl')

print("✅ Model trained and saved from cleaned data!")

