import requests
import pandas as pd
import sqlite3

# EXTRACT
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 12.7, "longitude": 77.8, "hourly": "temperature_2m"}

response = requests.get(url, params=params)
response.raise_for_status()

# TRANSFORM
df = pd.DataFrame(response.json()["hourly"])
print(df.head())

# LOAD
conn = sqlite3.connect("weather.db")
df.to_sql("weather_hourly", conn, index=False, if_exists="replace")

# CHECK
result = pd.read_sql("SELECT * FROM weather_hourly", conn)
print(result.shape)

conn.close()
