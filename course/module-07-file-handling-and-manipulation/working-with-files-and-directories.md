# Working with files and directories

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain the difference between files and directories
- Navigate file paths in Python
- Create, inspect, and organize folders programmatically
- Use modern path handling practices for automation scripts

---

## Introduction

Most automation tasks depend on files. A script may need to read reports, create logs, save outputs, or organize folders by date. To do that safely, you need to understand how Python works with files and directories.

A **file** stores data, such as a text document, CSV, Excel workbook, or image. A **directory** (or folder) contains files and sometimes other directories.

---

## Key Concepts

### Files, folders, and paths

A **path** tells Python where a file or folder is located.

Examples:

- `reports/daily.csv`
- `output/summary.txt`
- `logs/2026/may/run.log`

Paths may be:

- **Relative**: based on the current working directory
- **Absolute**: the full location on the machine

For automation projects, relative paths are often easier to manage inside one project folder.

### Why `pathlib` is useful

Python’s `pathlib` module provides a clean, readable way to work with paths.

Benefits:

- easier path joining
- clearer code
- better cross-platform support

Example:

```python
from pathlib import Path

report = Path("reports") / "daily.csv"
print(report)
```

### Common directory tasks

Automation scripts often need to:

- check whether a file exists
- create folders before writing output
- list files inside a directory
- separate input and output locations

### Safe automation habits

When working with files and directories:

- avoid hardcoding machine-specific paths unless necessary
- create output folders if they do not exist
- keep source files separate from generated files
- test on sample files before using important data

---

## Examples

### Example 1: Create project folders

```python
from pathlib import Path

for folder in ["input", "output", "logs"]:
    Path(folder).mkdir(exist_ok=True)

print("Folders are ready")
```

### Example 2: Check whether a file exists

```python
from pathlib import Path

file_path = Path("input") / "customers.csv"

if file_path.exists():
    print("File found")
else:
    print("File not found")
```

### Example 3: List items in a directory

```python
from pathlib import Path

for item in Path("input").iterdir():
    print(item.name)
```

---

## Notes

- Prefer `pathlib` for new Python code.
- Keep file paths readable and consistent across your project.
- Use separate folders such as `input`, `output`, and `logs`.
- Check for missing paths before reading or writing files.

---

## Summary

- Files store data, while directories organize files and subdirectories.
- Python scripts often rely on path handling for real automation work.
- `pathlib` makes file and directory operations easier and safer.

---

## Practice Exercises

1. Create a Python script that makes `input`, `output`, and `archive` folders.
2. Write code to check whether `input/report.txt` exists.
3. List all files inside a folder and print their names.

---

## Further Reading

- [pathlib documentation](https://docs.python.org/3/library/pathlib.html)
- [Python file and directory access](https://docs.python.org/3/library/filesys.html)
