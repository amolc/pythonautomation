# Integrating CSV Data with Pandas and SQLite

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Read tabular data from a CSV file into a Pandas DataFrame.
- Connect to a SQLite database from a Python script.
- Export a DataFrame structure directly into a SQLite table using `to_sql()`.
- Retrieve and verify database records using standard SQL queries.

---

## Introduction

In real-world automation, data often originates in CSV files, spreadsheets, or log files. While Pandas is excellent for analyzing and cleaning this data, keeping data in CSV format is inefficient for web applications. CSV files are slow to query and do not support concurrent reads/writes well.

Instead, we can read a CSV using Pandas, clean it, and insert it into **SQLite**—a lightweight, serverless relational database engine. Once stored in SQLite, our Flask API can query and modify records efficiently.

---

## Key Concepts

### What is SQLite?

SQLite is a self-contained, serverless SQL database engine. Unlike PostgreSQL or MySQL, SQLite stores its entire database as a single file on disk (e.g., `app.db`). This makes it highly portable and ideal for desktop applications, testing, and microservices.

### Pandas to SQLite Integration

Pandas integrates with database engines using a library called **SQLAlchemy**. SQLAlchemy is a SQL toolkit and Object Relational Mapper (ORM) for Python.

To write a Pandas DataFrame to a database:
1. Create a SQLAlchemy engine.
2. Load a CSV with `pd.read_csv()`.
3. Use the **`df.to_sql()`** method.

Key parameters of `df.to_sql()`:
- `name`: The name of the SQL table to create or write to.
- `con`: The database connection or SQLAlchemy engine object.
- `if_exists`: What to do if the table already exists:
  - `'fail'`: Raise an error (default).
  - `'replace'`: Drop the table and recreate it before inserting.
  - `'append'`: Keep existing structure and insert new rows.
- `index`: Boolean (`True`/`False`). Dictates whether the DataFrame's index column should be stored as a database column.

---

## Examples

### Example 1: Ingesting a CSV and Storing in SQLite

Suppose we have a file named `employees.csv` in our project:
```csv
Name,Department,Salary
Amol,Engineering,95000
Snehal,Product,92000
Rahul,Marketing,65000
Priya,Engineering,105000
```

The following Python script reads this CSV and saves it to a SQLite database:

```python
import pandas as pd
from sqlalchemy import create_engine

# 1. Load CSV data into a Pandas DataFrame
df = pd.read_csv("employees.csv")

# 2. Create a SQLAlchemy connection engine for a SQLite database named 'company.db'
# 'sqlite:///...' uses 3 slashes for a relative path on your system
engine = create_engine("sqlite:///company.db")

# 3. Save the DataFrame to a SQL table named 'employees'
# We use if_exists='replace' so we can run this script repeatedly
df.to_sql("employees", con=engine, if_exists="replace", index=False)

print("Data imported from CSV to SQLite 'employees' table successfully!")
```

### Example 2: Querying SQL Table Data with Pandas

Once data is in SQLite, you can query it back into a DataFrame using `pd.read_sql()`:

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///company.db")

# Query the entire table
query = "SELECT * FROM employees WHERE Department = 'Engineering'"
df_engineering = pd.read_sql(query, con=engine)

print("Engineering Department Employees:")
print(df_engineering)
```

### Example 3: Connecting with built-in `sqlite3` for REST APIs

While Pandas is great for bulk operations (like loading and saving DataFrames), for thin API routes we can use Python's built-in `sqlite3` module to make quick, light queries.

```python
import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect("company.db")

# Create a cursor object to execute commands
cursor = conn.cursor()

# Run a query
cursor.execute("SELECT Name, Salary FROM employees")
rows = cursor.fetchall()

# Print results
for row in rows:
    print(f"Employee: {row[0]}, Salary: ${row[1]}")

# Always close the connection when done
conn.close()
```

---

## Notes

- **Database File Creation**: If the SQLite file (e.g. `company.db`) does not exist when you connect, SQLite will automatically create it in the specified directory.
- **SQL Injection Risk**: Never construct queries using string interpolation (`f"SELECT * FROM table WHERE id = {user_id}"`) if user input is involved. Instead, always use parameterized queries (`cursor.execute("SELECT * FROM table WHERE id = ?", (user_id,))`) to prevent SQL injection security issues.

---

## Summary

- SQLite stores relational tables inside a single local file.
- Use `pd.read_csv()` to load external CSV data.
- Use `df.to_sql()` with a SQLAlchemy engine connection to write DataFrames directly to SQL tables.
- Use Python's built-in `sqlite3` library for executing specific SQL queries in application logic.

---

## Practice Exercises

1. Create a CSV file `products.csv` containing columns `ID`, `Name`, `Price`, and `Category`. Write a Python script to import this file into a SQLite database `inventory.db` under the table `products`.
2. Write a Python function `get_cheap_products(max_price)` that connects to `inventory.db` using `sqlite3`, queries products costing less than `max_price`, and returns their names as a Python list.
3. Modify your import script from Exercise 1 to append a timestamp column `imported_at` to the DataFrame before saving it to SQL. Ensure that running the script twice appends the new data instead of replacing it (use `if_exists='append'`).

---

## Further Reading

- [Pandas to_sql Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html)
- [SQLAlchemy Core Tutorial](https://docs.sqlalchemy.org/en/20/core/tutorial.html)
- [Python sqlite3 Module Documentation](https://docs.python.org/3/library/sqlite3.html)
