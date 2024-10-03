from schemas.prediction_response import PredictionResponse
from schemas.inference_data import InferenceData
from fastapi import FastAPI

from services.services import ModelService

app = FastAPI()

model_service = ModelService("/app/models/model.pkl", "/app/models/scaler.pkl")


@app.post("/inference", response_model=PredictionResponse)
def inference(data: InferenceData):
    prediction: bool = model_service.inference(data)
    return {
        "prediction": prediction
    }
