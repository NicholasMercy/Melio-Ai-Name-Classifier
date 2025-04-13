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

**Assumptions**  
1. I went into this beginning with the assumption of flexiblity and integration with Kserve so I first wanted to get the basic fundamentals done before going foward.  
2. I used AI to help me undestand how different process work and came to conclusion to use a pre built model to train another due to time constraints  
3. I assumed intially that publishing to Highwind would be a simple endeavour from past experiences with other infastructures  

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
1. Studied and used AI to help explore solutions for fast simple, model training, went with spacy, panda, primarly ("en_core_web_md")  
2. Studied and learnt how LogisticRegression works, with training of model, how to save, what to look out for and how vectors, reshaping, and predictions work.  
3. Created and saved on our own model based on the train_classifier.py script  
4. Encountered errors with reshaping vectors when inputting into api, implemented error handling  
5. Seperated our function to seperate script for cleaner code, used our model to return in app.py and works!  
6. Generated this readme in free time, did not count this time as it was just general logging.  

**Assumptions**  
1. I came to the conclusion of using the fast spacy model since it is quick and simple to train and save the required models  
2. I used fast api for the time being to test, I should have tried using Kserve local testing in an earlier stage  
3. I assumed error handling was present with alot of the issues, but I had to build where necessary  

### 📌 Goals for Next Session
- Deploy to production with Highwind  
- Test  
- Optimize  
- Refractor where necessary  
- Send to Melio AI  

---

## Hour 3 - start 20:31 - 9:31

### 🎯 Goal
- Deploy the trained ML classifier into production using the API

### 📝 Session Highlights
1. Realized I should change my project structure now to cater for Kserve intregarion  
2. Spent most of my time learning integration with Kserve and how it works  
3. Implemented src folder, docker files, and studied and understood how these process work  
4. Refractored my code to cater for these changes  
5. A big part of my time was understanding the code and catering I need to adhere  

**Assumptions**  
1. I assumed this would be the simplest endeavour but was the one where i spent the most time learning, refractoring and understanding  
2. I assumed publishing to production didnt require me to refractor my code  
3. Throughout this process I realised I spent more time here than usual so my goal shifted into simply getting api into production for time being and the extra time will try to work on the model hosting  

### 📌 Goals for Next Session
1. local test - 10 mins  
2. deploy - 15 mins  
3. test on production - 5 mins  
4. Deploy Model - 30 mins  

---

## Hour 4 - 10:15

### 🎯 Goals
- Finalize production deployment
- Conduct tests and apply performance optimizations

---

## ⚙️ Environment Setup

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
