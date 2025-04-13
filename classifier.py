import spacy 
#load the spacy model
nlp = spacy.load("en_core_web_sm")

def classify_name(name):
    
    names = ["Nick", "Ryan", "John"]
    for name in names:
        doc = nlp(name)
        print(name, [(ent.text, ent.label_) for ent in doc.ents])

if __name__ == "__main__":
    classify_name("Nick")
    classify_name("Ryan")
    classify_name("John")
    
