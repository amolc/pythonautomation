# Automating database queries and data manipulation tasks

**Course:** Automation using Python — Part 1  
**Module 9:** Database Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Run automated SELECT, INSERT, and UPDATE operations from Python
- Process query results in loops and simple reports
- Use transactions and parameters more safely
- Build small repeatable database workflows

---

## Introduction

After connecting to a database, the next step is automating actual work: reading rows, inserting data, updating statuses, and generating simple outputs. Python is especially useful when the same query or update must run repeatedly.

---

## Key Concepts

### Automating queries

A script can run the same SQL query every day or every hour and then process the results automatically.

Examples:

- find claims submitted today
- list customers with missing contact data
- count unpaid invoices by branch

### Automating inserts and updates

Python can insert imported data, update status values, or mark records as processed.

### Parameterized SQL

Values should be passed as parameters, not built directly into SQL strings. This improves correctness and security.

### Transactions and commits

For data-changing operations, call `commit()` after successful work. If something fails, you may need to roll back instead of saving partial changes.

---

## Examples

### Example 1: Query and print matching rows

```python
import sqlite3

connection = sqlite3.connect("automation.db")
cursor = connection.cursor()

cursor.execute("SELECT id, name FROM customers")
for row in cursor.fetchall():
    print(row)

connection.close()
```

### Example 2: Insert multiple rows

```python
import sqlite3

customers = [("Asha",), ("Vikram",), ("Nina",)]

connection = sqlite3.connect("automation.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT)")
cursor.executemany("INSERT INTO customers (name) VALUES (?)", customers)
connection.commit()
connection.close()
```

### Example 3: Update rows safely

```python
import sqlite3

connection = sqlite3.connect("automation.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS claims (id INTEGER PRIMARY KEY, status TEXT)")
cursor.execute("UPDATE claims SET status = ? WHERE status = ?", ("reviewed", "pending"))
connection.commit()
connection.close()
```

---

## Notes

- Log how many rows were inserted or updated when possible.
- Test update queries on sample data first.
- Use transactions carefully so partial failures do not create confusion.
- Keep SQL readable and focused on one job at a time.

---

## Summary

- Python can automate repeated database queries and updates efficiently.
- Parameterized SQL and transaction handling improve safety.
- Small, focused scripts are often the best way to automate database tasks.

---

## Practice Exercises

1. Query all rows from a sample table and print them.
2. Insert three new rows using `executemany()`.
3. Update a status field for matching rows and commit the change.

---

## Further Reading

- [sqlite3 how-to guides](https://docs.python.org/3/library/sqlite3.html)
