from fastapi import FastAPI
from pydantic import BaseModel

def classify_name(name: str) -> str:
    name = name.lower()

    if any(keyword in name for keyword in ["university", "college", "institute", "school"]):
        return "University"

    elif any(keyword in name for keyword in ["inc", "ltd", "llc", "corp", "technologies", "solutions"]):
        return "Company"

    else:
        return "Person"

# FastAPI app
app = FastAPI()


class NameRequest(BaseModel):
    full_name: str

@app.post("/classify/")
def classify(request: NameRequest):
    classification = classify_name(request.full_name)
    return {"classification": classification}
