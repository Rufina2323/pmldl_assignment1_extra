import pickle

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from schemas.inference_data import InferenceData


class ModelService:
    def __init__(self, model_path: str, scaler_path: str):
        self.model_path: str = model_path
        self.model: KNeighborsClassifier = self.initialize_model()

        self.scaler_path: str = scaler_path
        self.scaler: StandardScaler = self.initialize_scaler()

    def initialize_model(self) -> KNeighborsClassifier:
        with open(self.model_path, "rb") as model_file:
            loaded_model: KNeighborsClassifier = pickle.load(model_file)
        return loaded_model

    def initialize_scaler(self) -> StandardScaler:
        with open(self.scaler_path, "rb") as scaler_file:
            loaded_scaler: StandardScaler = pickle.load(scaler_file)
        return loaded_scaler

    def preprocess_data(self, data: InferenceData) -> np.ndarray:
        numpy_data: np.ndarray = np.asarray([[
            data.age,
            1 if data.sex == "male" else 0,
            data.cp,
            data.trestbps,
            data.chol,
            int(data.fbs),
            data.restecg,
            data.thalach,
            int(data.exang),
            data.oldpeak,
            data.slope,
            data.ca,
            data.thal
        ]])
        result: np.ndarray = self.scaler.transform(numpy_data)
        return result

    def inference(self, data: InferenceData) -> bool:
        preprocessed_data: np.ndarray = self.preprocess_data(data)
        raw_prediction: np.ndarray = self.model.predict(preprocessed_data)
        prediction: bool = bool(raw_prediction[0])
        return prediction
