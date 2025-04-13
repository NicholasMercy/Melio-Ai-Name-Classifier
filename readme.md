# 🧠 Melio AI Name Classifier – Development Log

## Hour 1 (16:45 – 17:45)

### 🎯 Initial Goals
- Set up development environment (IDE, Python project)
- Understand KServe, Highwind, and machine learning deployment solutions
- Outline necessary requirements

### 📝 Session Highlights
1. Initialized repo with a basic Python project and virtual environment (venv)
2. Revisited Python fundamentals
3. Implemented a basic rule-based classification function for testing
4. Set up Git and began version control
5. Learned to test individual pieces of code
6. Built and tested a simple FastAPI app
7. Researched environments, cursor handling, and ML infrastructure

### 📌 Goals for Next Session
- Test integration between the API and rule-based classifier
- Research how to integrate file or CSV input into the API
- Deploy the API to production using Highwind
- Confirm complete integration is working
- Replace rule-based logic with a trained ML model in Hour 3
- Explore optimization strategies in Hour 4
- *(Optional)* Return classification results as a downloadable file

---

## Hour 2 (18:35 – 18:45)

### 🎯 Initial Goal
- Build the first version of the machine learning-based classifier

### 📝 Session Highlights
1.Studied and used AI to help explore solutions for fast simple, model training, went with spacy, panda, primarly ("en_core_web_md")
2.Studied and learnt how LogisticRegression works, with training of model, how to save, what to look out for and how vectors, reshaping, and predictions work.
3.Created and saved on our own model based on the train_classifier.py script
4.Encountered errors with reshaping vectors when inputting into api, implemented error handling
5.Seperated our function to seperate script for cleaner code, used our model to return in app.py and works!
6.Generated this readme in free time, did not count this time as it was just general logging.

### 📌 Goals for Next Session
-Deploy to production with Highwind
-Test
-Optimize
-Refractor where necessary
-Send to Melio AI
---

## Hour 3 - start 20:31

### 🎯 Goal
- Deploy the trained ML classifier into production using the API

---

## Hour 4

### 🎯 Goals
- Finalize production deployment
- Conduct tests and apply performance optimizations


Environment Setup

### 🐍 Python Version
- Python 3.12.8

### 📦 Dependencies
```bash
spacy==3.8.5 = en_core_web_md
scikit-learn==1.6.1
pandas==2.2.3
fastapi==0.115.12
uvicorn==0.34.1
joblib==1.4.2