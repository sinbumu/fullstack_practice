import bentoml
from pydantic import BaseModel
import numpy as np

# 요청/응답 스키마
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisOutput(BaseModel):
    prediction: int

# Service 정의 (클래스 기반)
@bentoml.service(name="iris_classifier")
class IrisService:
    def __init__(self):
        self.model = bentoml.models.get("iris_rf_model:latest").load_model()

    @bentoml.api
    def predict(self, data: IrisInput) -> IrisOutput:
        features = np.array([[
            data.sepal_length, data.sepal_width,
            data.petal_length, data.petal_width
        ]])
        pred = self.model.predict(features)
        return IrisOutput(prediction=int(pred[0]))