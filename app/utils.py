from catboost import CatBoostRegressor
import os

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "model/catboost_pm25_model.cbm"
)

model = CatBoostRegressor()
model.load_model(MODEL_PATH)
