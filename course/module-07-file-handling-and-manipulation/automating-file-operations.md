# Automating file operations

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Automate common file operations with Python
- Copy, move, rename, and delete files safely
- Organize files based on simple rules
- Apply automation patterns to repetitive file workflows

---

## Introduction

Many business and personal workflows involve repetitive file tasks: renaming uploads, moving reports into dated folders, archiving old logs, or copying templates. Python can automate these steps and reduce time spent on manual file handling.

---

## Key Concepts

### Common file automation tasks

Typical file automation includes:

- copying files
- moving files into folders
- renaming files in bulk
- deleting temporary files
- archiving old outputs

### Useful tools

Python provides several useful modules:

- `pathlib` for path handling
- `shutil` for copying and moving
- `os` for some low-level filesystem work

### Copy, move, and rename

Use `shutil.copy()` or `shutil.copy2()` to copy files. Use `shutil.move()` to move or rename files.

### Delete with care

Deleting files is permanent in many automation contexts. Before deleting:

- confirm the path
- test on sample data
- avoid deleting source files unless required

### Rule-based organization

A useful automation pattern is:

1. scan files
2. decide what to do based on a rule
3. perform the action
4. log or print the result

---

## Examples

### Example 1: Rename all `.txt` files

```python
from pathlib import Path

folder = Path("input")

for file_path in folder.glob("*.txt"):
    new_name = file_path.with_name(f"processed_{file_path.name}")
    file_path.rename(new_name)
    print(f"Renamed {file_path.name} -> {new_name.name}")
```

### Example 2: Move CSV files to an archive folder

```python
from pathlib import Path
import shutil

source = Path("input")
archive = Path("archive")
archive.mkdir(exist_ok=True)

for file_path in source.glob("*.csv"):
    shutil.move(str(file_path), archive / file_path.name)
    print(f"Moved {file_path.name} to archive")
```

### Example 3: Delete temporary files

```python
from pathlib import Path

for file_path in Path("output").glob("*.tmp"):
    file_path.unlink()
    print(f"Deleted {file_path.name}")
```

---

## Notes

- Prefer moving files into an archive instead of deleting them immediately.
- Print or log each action during automation.
- Test file automation on a small folder first.
- Be careful with wildcard patterns so you do not affect the wrong files.

---

## Summary

- Python can automate repetitive file operations quickly and reliably.
- `pathlib` and `shutil` are useful tools for copy, move, rename, and delete workflows.
- File automation should be rule-based, testable, and safe.

---

## Practice Exercises

1. Write a script that renames all `.log` files by adding a date prefix.
2. Move all `.csv` files from `input` to `archive`.
3. Delete all `.tmp` files from an `output` folder after printing their names.

---

## Further Reading

- [shutil documentation](https://docs.python.org/3/library/shutil.html)
- [pathlib documentation](https://docs.python.org/3/library/pathlib.html)
