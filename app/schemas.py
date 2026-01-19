from pydantic import BaseModel

class AirQualityInput(BaseModel):
    PM10: float
    SO2: float
    NO2: float
    CO: float
    O3: float
    TEMP: float
    PRES: float
    DEWP: float
    RAIN: float
    WSPM: float
    wd: str
    year: int
    month: int
    day: int
    hour: int
    station: str
