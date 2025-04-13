import argparse
from typing import List
import spacy
import joblib
import numpy as np

from kserve import Model, ModelServer, model_server, InferRequest, InferResponse, InferOutput
from kserve.utils.utils import generate_uuid


class NameClassifier(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.model = None
        self.ready = False
        self.load()
        

    def load(self):
        self.nlp = spacy.load("en_core_web_md")
        self.model = joblib.load("saved_models/name_classifier.pkl")
        self.le = joblib.load("saved_models/label_encoder.pkl")
        self.ready = True
        print(f"Payload: load")

    def preprocess(self, payload: InferRequest, headers: dict = None, *args, **kwargs) -> np.ndarray:
        input_data = payload.inputs[0].data 
        vectors = []

        for name in input_data:
            vec = self.nlp(name.strip()).vector
            if vec.shape[0] != 300:
                raise ValueError(f"Expected 300-dim vector, got {vec.shape[0]}")
            vectors.append(vec)

        return np.array(vectors)




    def predict(self, data: np.ndarray, headers: dict = None, **kwargs) -> InferResponse:
        predictions = self.model.predict(data)
        decoded = self.le.inverse_transform(predictions).tolist()

        response_id = generate_uuid()
        output = InferOutput(name="output-0", shape=[len(decoded)], datatype="BYTES", data=decoded)
        return InferResponse(model_name=self.name, infer_outputs=[output], response_id=response_id)


# Required for Kserve entrypoint
parser = argparse.ArgumentParser(parents=[model_server.parser])
parser.add_argument("--model_name", default="name-classifier", help="Model name for serving")
args, _ = parser.parse_known_args()

if __name__ == "__main__":
    model = NameClassifier(args.model_name)
    ModelServer().start([model])
