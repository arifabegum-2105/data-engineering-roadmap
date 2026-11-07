import sqlite3
import pandas as pd

conn = sqlite3.connect("weather.db")

query = """
WITH hourly AS (
	SELECT substr(time,1,10) AS day,time, temperature_2m
	from weather_hourly
),
ranked AS(
	SELECT day, time, temperature_2m,
	ROW_NUMBER() OVER(
	    PARTITION BY day
	    ORDER BY temperature_2m DESC
	    ) AS rank_in_day
FROM hourly
)
SELECT day,time,temperature_2m
FROM ranked
where rank_in_day=1
ORDER BY day
"""

print(pd.read_sql(query, conn))
conn.close()