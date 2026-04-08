from pydantic import BaseModel

class SpamPredictionRequest(BaseModel):
    text: str

class SpamPredictionResponse(BaseModel):
    text: str
    prediction: str
    confidence: float
