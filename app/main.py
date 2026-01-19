from fastapi import FastAPI
import pandas as pd

from app.schemas import AirQualityInput
from app.utils import model

app = FastAPI(title="Air Quality PM2.5 Predictor")

@app.post("/predict")
def predict(data: AirQualityInput):
    df = pd.DataFrame([data.dict()])

# ВАЖНО: выравниваем порядок колонок
    df = df[model.feature_names_]

    prediction = model.predict(df)[0]

    return {
        "predicted_pm25": round(float(prediction), 2)
    }
