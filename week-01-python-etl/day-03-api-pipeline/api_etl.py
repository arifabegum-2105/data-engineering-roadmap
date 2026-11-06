import requests
import pandas as pd
import sqlite3

#extract
url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 12.7, "longitude": 77.8, "hourly": "temperature_2m"}

#transform
response = requests.get(url, params=params)
response.raise_for_status()
df = pd.DataFrame(response.json()["hourly"])
print(df.head())
data = response.json()
print(response.status_code)

#load
conn=sqlite3.connect("weather.db")
df.to_sql("weather_hourly",conn, index = False, if_exists = "append")
result=pd.read_sql("SELECT * FROM weather_hourly",conn)
print(result)

conn.close()
