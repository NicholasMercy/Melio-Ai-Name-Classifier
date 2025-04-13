from fastapi import FastAPI
from pydantic import BaseModel
from classifier import classify_name

# FastAPI app
app = FastAPI()

class NameRequest(BaseModel):
    full_name: str
    

@app.post("/classify/")
def classify(request: NameRequest):
    classification = classify_name(request.full_name)
    return {"classification": classification}
