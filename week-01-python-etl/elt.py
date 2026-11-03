import pandas as pd
import sqlite3

#extract
df=pd.read_csv("sales.csv")

#load
conn=sqlite3.connect("sales.db")
df.to_sql("sales_raw",conn,index=False, if_exists="replace")

result=pd.read_sql("SELECT * FROM sales_raw",conn)
print(result)

#transform
conn.execute("DROP TABLE IF EXISTS sales_clean")
conn.execute("CREATE TABLE sales_clean AS SELECT DISTINCT * FROM sales_raw")
conn.commit()

clean = pd.read_sql("SELECT * FROM sales_clean", conn)
print(clean)

conn.close()