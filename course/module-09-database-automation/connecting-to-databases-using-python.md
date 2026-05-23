# Connecting to databases using Python

**Course:** Automation using Python — Part 1  
**Module 9:** Database Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Connect Python to a database using built-in or external libraries
- Understand the role of a connection and cursor
- Run basic queries and fetch results
- Close database resources properly after use

---

## Introduction

Before a Python script can read or update database records, it must connect to the database. The exact library depends on the database type, but the overall pattern is similar across systems.

For beginners, SQLite is a useful starting point because it is included with Python through the `sqlite3` module.

---

## Key Concepts

### Database connection

A connection represents the active link between your Python script and the database.

### Cursor

A cursor lets you send SQL commands and fetch results.

### Typical workflow

A common connection workflow is:

1. open a connection
2. create a cursor if needed
3. execute SQL statements
4. fetch or commit results
5. close the connection

### Common libraries

- `sqlite3` for SQLite
- `psycopg` for PostgreSQL
- `mysql-connector-python` for MySQL

Even when the library changes, the concepts of connection, execute, fetch, commit, and close remain similar.

---

## Examples

### Example 1: Connect to SQLite

```python
import sqlite3

connection = sqlite3.connect("automation.db")
print("Connected")
connection.close()
```

### Example 2: Create a table and query rows

```python
import sqlite3

connection = sqlite3.connect("automation.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

connection.close()
```

### Example 3: Use a parameterized query

```python
import sqlite3

connection = sqlite3.connect("automation.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO customers (name) VALUES (?)", ("Asha",))
connection.commit()
connection.close()
```

---

## Notes

- Always close the connection when the script is finished.
- Use parameterized queries instead of string formatting for SQL values.
- Commit changes after inserts, updates, or deletes.
- Store credentials securely when working with external databases.

---

## Summary

- Python connects to databases through library-specific connection objects.
- A cursor is commonly used to run SQL statements and fetch results.
- Safe connection handling and parameterized queries are important best practices.

---

## Practice Exercises

1. Connect to a SQLite database file and print a success message.
2. Create a simple table using Python.
3. Insert one row with a parameterized query and commit the transaction.

---

## Further Reading

- [sqlite3 tutorial](https://docs.python.org/3/library/sqlite3.html)
- [DB-API 2.0 specification](https://peps.python.org/pep-0249/)
