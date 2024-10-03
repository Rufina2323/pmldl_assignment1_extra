from pydantic import BaseModel


class InferenceData(BaseModel):
    age: int
    sex: str
    cp: int
    trestbps: int
    chol: int
    fbs: bool
    restecg: int
    thalach: int
    exang: bool
    oldpeak: float
    slope: int
    ca: int
    thal: int
