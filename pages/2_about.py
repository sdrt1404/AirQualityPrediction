import streamlit as st

st.title("About the Project")

st.markdown("""
### Air Quality PM2.5 Prediction

**Цель проекта:**  
Прогнозирование концентрации PM2.5 на основе метеорологических и химических параметров.

**Модель:**  
CatBoostRegressor

**Метрики:**  
RMSE ≈ 20.7

**Интерпретация:**  
Использованы SHAP values для анализа важности признаков.

**Деплой:**  
- FastAPI (REST API)
- Streamlit (демо-интерфейс)
""")
