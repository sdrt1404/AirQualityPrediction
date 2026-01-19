import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor

st.title("PM2.5 Prediction")

# Загрузка модели
@st.cache_resource
def load_model():
    model = CatBoostRegressor()
    model.load_model("model/catboost_pm25_model.cbm")
    return model

model = load_model()

st.sidebar.header("Input parameters")

PM10 = st.sidebar.number_input("PM10", value=80.0)
SO2 = st.sidebar.number_input("SO2", value=12.0)
NO2 = st.sidebar.number_input("NO2", value=35.0)
CO = st.sidebar.number_input("CO", value=0.9)
O3 = st.sidebar.number_input("O3", value=22.0)
TEMP = st.sidebar.number_input("Temperature", value=15.0)
PRES = st.sidebar.number_input("Pressure", value=1012.0)
DEWP = st.sidebar.number_input("Dew Point", value=5.0)
RAIN = st.sidebar.number_input("Rain", value=0.0)
WSPM = st.sidebar.number_input("Wind Speed", value=2.5)
wd = st.sidebar.selectbox("Wind Direction", ["N","NE","E","SE","S","SW","W","NW","NNW"])
year = st.sidebar.number_input("Year", value=2014)
month = st.sidebar.number_input("Month", value=12)
day = st.sidebar.number_input("Day", value=15)
hour = st.sidebar.number_input("Hour", value=18)
station = st.sidebar.text_input("Station", value="Changping")

if st.button("Predict PM2.5"):
    df = pd.DataFrame([{
        "PM10": PM10,
        "SO2": SO2,
        "NO2": NO2,
        "CO": CO,
        "O3": O3,
        "TEMP": TEMP,
        "PRES": PRES,
        "DEWP": DEWP,
        "RAIN": RAIN,
        "WSPM": WSPM,
        "wd": wd,
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "station": station
    }])

    df = df[model.feature_names_]

    prediction = model.predict(df)[0]
    st.success(f"Predicted PM2.5: {prediction:.2f} µg/m³")
