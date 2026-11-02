# Data Engineering Roadmap

My learning journey in data engineering. I build small projects step by step and make sure I understand every line.

## Progress

| Week | Day | What I built |
|------|-----|--------------|
| 1 | 1 | CSV to SQLite pipeline with pandas |

## Day 1: Sales pipeline

A mini ETL pipeline in Python.

- **Extract:** read `sales.csv` with `pd.read_csv`
- **Transform:** removed duplicate rows and converted `order_date` from string to datetime. The missing `amount` is left as `NULL` on purpose, so `AVG()` ignores it instead of treating it as a free order.
- **Load:** wrote the clean data to a SQLite table with `if_exists="replace"`, so re-running the script gives the same result.

**Run it:**

    cd week-01-python-etl/day-01-sales-pipeline
    pip install pandas
    python pipeline.py

## Tools

Python, pandas, SQLite, SQL, Git, GitHub CLI
