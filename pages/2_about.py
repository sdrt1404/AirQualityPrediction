import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("About the Project")

st.markdown("""
## Air Quality PM2.5 Prediction

**Цель проекта:**  
Прогнозирование концентрации мелкодисперсных частиц PM2.5 на основе
метеорологических, временных и химических параметров окружающей среды.

**Модель:** CatBoostRegressor  
**Метрики:** RMSE ≈ 20.7  
**Интерпретация:** SHAP values  
**Деплой:** FastAPI (локально) + Streamlit (демо-интерфейс)
""")

st.divider()

# -------------------------------
# Dataset section
# -------------------------------
st.header("Исходные данные")

st.markdown("""
Используется **Beijing Air Quality Dataset**  
Станция наблюдения: **Changping**

Датасет содержит:
- более **35 000 записей**,
- временные признаки (год, месяц, день, час),
- концентрации загрязняющих веществ,
- метеорологические параметры.
""")

# Загрузка данных
@st.cache_data
def load_data():
    df = pd.read_csv('AirQualityChangping.csv')
    return df

df = load_data()

st.subheader("Пример данных")
st.dataframe(df.head())

st.markdown(f"""
**Размер датасета:**  
- Строки: {df.shape[0]}  
- Колонки: {df.shape[1]}
""")

st.divider()

# -------------------------------
# Visualizations
# -------------------------------
st.header("Визуализация данных")

# 1. Distribution of PM2.5
st.subheader("Распределение PM2.5")

fig, ax = plt.subplots()
sns.histplot(df["PM2.5"], bins=50, kde=True, ax=ax)
ax.set_xlabel("PM2.5 (µg/m³)")
ax.set_ylabel("Частота")
st.pyplot(fig)

st.markdown("""
Распределение имеет правостороннюю асимметрию,
что указывает на наличие периодов с высоким уровнем загрязнения.
""")

# 2. Seasonal pattern
st.subheader("Сезонность PM2.5 (по месяцам)")

fig, ax = plt.subplots()
sns.boxplot(x="month", y="PM2.5", data=df, ax=ax)
ax.set_xlabel("Месяц")
ax.set_ylabel("PM2.5")
st.pyplot(fig)

st.markdown("""
Наибольшие значения PM2.5 наблюдаются в зимние месяцы,
что связано с отопительным сезоном и погодными условиями.
""")

# 3. Correlation heatmap (numeric only)
st.subheader("Корреляция числовых признаков")

numeric_df = df.select_dtypes(include="number").drop(columns=["No"], errors="ignore")

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm",
    center=0,
    ax=ax
)
st.pyplot(fig)

st.markdown("""
Наибольшую корреляцию с PM2.5 показывают:
- PM10
- NO2
- CO
""")

st.divider()

# -------------------------------
# Conclusion
# -------------------------------
st.header("Вывод")

st.markdown("""
Исходные данные обладают выраженной сезонностью и сильной взаимосвязью
между загрязняющими веществами, что делает их подходящими
для задач регрессии и анализа факторов, влияющих на качество воздуха.

Полученные результаты подтверждают корректность выбора модели и признаков.
""")
