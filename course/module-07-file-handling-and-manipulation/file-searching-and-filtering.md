# File searching and filtering

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Search for files in directories and subdirectories
- Filter files by extension, name pattern, or size
- Use glob patterns in automation scripts
- Build file-selection logic before processing data

---

## Introduction

Automation scripts rarely process every file in a folder. Usually, they need only certain files, such as `.csv` reports, files with a date in the name, or files larger than a minimum size. Searching and filtering helps scripts target the right inputs.

---

## Key Concepts

### Searching for files

Python can search for files using:

- `pathlib.Path.glob()`
- `pathlib.Path.rglob()`
- `glob` from the standard library

`glob()` searches one directory level based on a pattern. `rglob()` searches recursively.

### Common file filters

You can filter by:

- file extension
- file name pattern
- file size
- last modified date
- whether the path is a file or directory

### Glob patterns

Examples:

- `*.txt` → all text files
- `report_*.csv` → CSV files starting with `report_`
- `**/*.log` → all log files in nested folders

### Why filtering matters

Filtering prevents mistakes and improves performance. It ensures your script processes only relevant files.

---

## Examples

### Example 1: Find all CSV files

```python
from pathlib import Path

for file_path in Path("input").glob("*.csv"):
    print(file_path.name)
```

### Example 2: Search recursively for log files

```python
from pathlib import Path

for file_path in Path("logs").rglob("*.log"):
    print(file_path)
```

### Example 3: Filter files by size

```python
from pathlib import Path

for file_path in Path("input").iterdir():
    if file_path.is_file() and file_path.stat().st_size > 1024:
        print(f"Large file: {file_path.name}")
```

---

## Notes

- Use `glob()` when you know the folder level.
- Use `rglob()` when files may be inside subfolders.
- Combine pattern matching with additional checks such as size or date.
- Always confirm that a path is a file before processing it.

---

## Summary

- File searching helps automation scripts locate relevant inputs.
- Filtering reduces mistakes by limiting processing to matching files.
- `glob()` and `rglob()` are practical tools for file selection.

---

## Practice Exercises

1. Print all `.txt` files inside an `input` folder.
2. Search recursively for `.csv` files inside a `reports` directory.
3. Print only files larger than 5 KB from a folder of sample data.

---

## Further Reading

- [glob documentation](https://docs.python.org/3/library/glob.html)
- [pathlib glob patterns](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob)
