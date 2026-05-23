# Introduction to Python Libraries for Automation

**Course:** Automation using Python — Part 1  
**Module 6:** Introduction to Python Automation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Describe what a Python library is
- Identify common libraries used in automation projects
- Match libraries to automation tasks such as files, web requests, spreadsheets, and databases
- Install libraries using `pip` and use them responsibly

---

## Introduction

A Python library is a collection of reusable code that helps you perform tasks without writing everything from scratch. Instead of building file readers, spreadsheet handlers, or HTTP clients yourself, you can use well-tested libraries.

Libraries are one of the main reasons Python is so effective for automation.

---

## Key Concepts

### Standard library vs third-party libraries

Python gives you two major sources of tools:

#### Standard library

These libraries come with Python and do not require separate installation.

Common examples:

- `os` for working with operating system paths and folders
- `pathlib` for clean path handling
- `shutil` for copying and moving files
- `csv` for reading and writing CSV files
- `json` for JSON data
- `sqlite3` for SQLite databases
- `datetime` for date and time logic
- `subprocess` for running system commands

#### Third-party libraries

These are installed separately, usually with `pip`.

Popular automation examples:

- `requests` for calling web APIs
- `pandas` for tabular data processing
- `openpyxl` for Excel files
- `pyautogui` for mouse and keyboard automation
- `beautifulsoup4` for parsing HTML
- `selenium` for browser automation
- `python-dotenv` for loading environment variables from a `.env` file

### Choosing the right library

When selecting a library, consider:

- Does it solve the problem directly?
- Is it well known and actively maintained?
- Is it already used in your project?
- Does it introduce unnecessary complexity?

In many cases, the standard library is enough. Start there before adding external dependencies.

### Common library categories for automation

#### 1. File and folder automation

Useful modules:

- `pathlib`
- `os`
- `shutil`
- `glob`

Use cases:

- Rename files in bulk
- Move reports into dated folders
- Search for files matching a pattern

#### 2. Data processing

Useful modules and libraries:

- `csv`
- `json`
- `pandas`

Use cases:

- Clean downloaded reports
- Transform rows and columns
- Merge data from multiple files

#### 3. Web and API automation

Useful libraries:

- `requests`
- `beautifulsoup4`
- `selenium`

Use cases:

- Download data from an API
- Extract information from websites
- Automate browser-based systems when APIs are unavailable

#### 4. Spreadsheet automation

Useful libraries:

- `openpyxl`
- `pandas`

Use cases:

- Read and update Excel workbooks
- Build summary sheets
- Format export files

#### 5. Database automation

Useful modules and libraries:

- `sqlite3`
- database drivers such as `psycopg` or `mysql-connector-python`

Use cases:

- Load data into tables
- Query operational records
- Generate reports automatically

### Installing libraries with pip

Use `pip` to install third-party packages:

```bash
pip install requests pandas openpyxl
```

In professional workflows, it is best to install packages inside a virtual environment so each project keeps its own dependencies.

### Importing libraries in Python

```python
import csv
from pathlib import Path
import requests
```

Once imported, you can call functions or classes provided by the library.

---

## Examples

### Example 1: Using the standard library for file paths

```python
from pathlib import Path

reports_folder = Path("reports")
output_file = reports_folder / "daily_summary.csv"

print(output_file)
```

### Example 2: Using `requests` to call an API

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
print(response.status_code)
print(response.json())
```

### Example 3: Using `pandas` for quick data analysis

```python
import pandas as pd

data = {
    "branch": ["North", "South", "North"],
    "premium": [1200, 900, 1500]
}

df = pd.DataFrame(data)
print(df.groupby("branch")["premium"].sum())
```

---

## Notes

- Prefer the Python standard library when it already solves the problem well.
- Add third-party libraries only when they clearly save time or improve reliability.
- Read package documentation before using a new library in production work.
- Pin important dependencies in `requirements.txt` for reproducible environments.
- Be careful with browser or GUI automation because those workflows can be more fragile than API or file-based automation.

---

## Summary

- Python libraries provide reusable building blocks for automation.
- The standard library covers many common automation tasks, including files, CSV, JSON, and SQLite.
- Third-party libraries such as `requests`, `pandas`, and `openpyxl` expand Python’s automation capabilities.

---

## Practice Exercises

1. Name three standard library modules that are useful for automation and describe one use case for each.
2. Compare `requests` and `selenium` in one or two sentences.
3. Write a small Python script that imports `Path` from `pathlib` and prints a file path.

---

## Further Reading

- [Python Standard Library](https://docs.python.org/3/library/)
- [PyPI](https://pypi.org/)
- [Requests documentation](https://requests.readthedocs.io/)
- [pandas documentation](https://pandas.pydata.org/docs/)
