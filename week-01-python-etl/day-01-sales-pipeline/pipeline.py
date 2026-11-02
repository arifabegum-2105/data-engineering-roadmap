import pandas as pd
import sqlite3

# EXTRACT
df = pd.read_csv("sales.csv")

# TRANSFORM
df = df.drop_duplicates()
df["order_date"] = pd.to_datetime(df["order_date"])
df.info()

# LOAD
conn = sqlite3.connect("sales.db")
df.to_sql("sales", conn, index=False, if_exists="replace")

# CHECK
result = pd.read_sql("SELECT * FROM sales", conn)
print(result)

avg = pd.read_sql("SELECT AVG(amount) AS avg_amount FROM sales", conn)
print(avg)

conn.close()
