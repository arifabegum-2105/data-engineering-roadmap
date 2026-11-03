# Data Engineering Roadmap

My learning journey in data engineering. I build small projects step by step and make sure I understand every line.

## Progress

| Week | Day | What I built |
|------|-----|--------------|
| 1 | 1 | CSV to SQLite pipeline with pandas (ETL) |
| 1 | 2 | Same data as an ELT pipeline, cleaned with SQL |

## Day 1: Sales pipeline (ETL)

- **Extract:** read `sales.csv` with `pd.read_csv`
- **Transform:** removed duplicate rows and converted `order_date` from string to datetime. The missing `amount` is left as `NULL` on purpose, so `AVG()` ignores it instead of treating it as a free order.
- **Load:** wrote the clean data to a SQLite table with `if_exists="replace"`, so re-running the script gives the same result.

## Day 2: Sales pipeline (ELT)

- **Extract and Load:** loaded the raw data, duplicates included, into a `sales_raw` table.
- **Transform:** created a `sales_clean` table with SQL (`SELECT DISTINCT`) inside the database. The raw table stays untouched, so I can change the cleaning rules without extracting again.


    cd week-01-python-etl/day-01-sales-pipeline
    pip install pandas
    python pipeline.py

## Tools

Python, pandas, SQLite, SQL, Git, GitHub CLI
