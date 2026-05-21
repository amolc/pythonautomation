# Module 1: Python Basics

**Automation using Python — Part 1**

Build a solid foundation in Python before moving into file automation, web scraping, and scheduling. This module is hands-on: every chapter includes runnable examples and exercises with solutions.

---

## What You Will Learn

- Install and run Python (REPL and scripts)
- Work with core data types and variables
- Organize data in lists, tuples, dicts, and sets
- Index, slice, and combine sequences
- Use built-in functions and common methods on strings and lists

---

## Prerequisites

- Python 3.9 or newer installed (`python3 --version`)
- A text editor or IDE (VS Code, PyCharm, Cursor, etc.)
- Basic comfort using a terminal

Optional: create a virtual environment in the project root:

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
```

---

## Chapters

| # | Chapter | Topics |
|---|---------|--------|
| 1 | [Introduction to Python](./introduction-to-python.md) | What Python is, installation, `print()`, comments, indentation, running scripts |
| 2 | [Data Types](./data-types.md) | `int`, `float`, `str`, `bool`, `None`, casting, truthiness |
| 3 | [Variables](./variables.md) | Assignment, naming, unpacking, references, constants |
| 4 | [Data Structure](./data-structure.md) | Lists, tuples, dicts, sets, choosing the right structure |
| 5 | [Operations on Data Structure](./operations-on-data-structure.md) | Indexing, slicing, `+`/`*`, `in`, dict merge |
| 6 | [Inbuilt methods](./inbuilt-methods.md) | `len`, `sorted`, string/list/dict methods, `help()` |

**Suggested pace:** One chapter per session; complete all exercises before the next module.

---

## Module Capstone Exercise

Combine skills from all chapters in one script `module1_capstone.py`:

1. Store a list of dicts representing files: `name` (str), `size_kb` (int), `ext` (str).
2. Filter to extensions in `{"csv", "json"}` (case-insensitive).
3. Print a report: total files, total size, largest file name.
4. Sort the filtered list by `size_kb` descending using `sorted()` with a `key`.
5. Print each line as: `NAME (SIZE KB)` using string methods or f-strings.

Example starter data:

```python
files = [
    {"name": "sales.csv", "size_kb": 120, "ext": "CSV"},
    {"name": "readme.txt", "size_kb": 2, "ext": "txt"},
    {"name": "config.json", "size_kb": 8, "ext": "json"},
]
```

---

## Next Module

[Module 2: Data Types and Variables](../module-02-data-types-and-variables/README.md) — deeper coverage of strings, input/output, and formatting.
