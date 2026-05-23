# The os and os.path modules

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Use `os` and `os.path` for file and directory operations
- Inspect the current working directory and path properties
- Build and validate paths programmatically
- Recognize when `pathlib` may be a cleaner alternative

---

## Introduction

Before `pathlib` became widely preferred, many Python scripts used `os` and `os.path` for filesystem tasks. These modules are still common in real codebases, so it is important to understand them.

---

## Key Concepts

### The `os` module

The `os` module provides functions for interacting with the operating system.

Common uses:

- get the current working directory
- list folder contents
- create directories
- rename or remove files

### The `os.path` module

`os.path` helps with path operations such as:

- joining path parts
- checking whether a path exists
- checking whether a path is a file or folder
- extracting file names or extensions

### Example operations

Useful functions include:

- `os.getcwd()`
- `os.listdir()`
- `os.mkdir()` or `os.makedirs()`
- `os.remove()`
- `os.path.join()`
- `os.path.exists()`
- `os.path.isfile()`
- `os.path.isdir()`

### `os.path` vs `pathlib`

Both approaches are valid. In modern Python, `pathlib` is often easier to read. However, you will still see `os` and `os.path` in older scripts and in some production code.

---

## Examples

### Example 1: Print the current working directory

```python
import os

print(os.getcwd())
```

### Example 2: Build and inspect a path

```python
import os

file_path = os.path.join("input", "report.csv")
print(file_path)
print("Exists:", os.path.exists(file_path))
```

### Example 3: List files in a folder

```python
import os

for name in os.listdir("input"):
    print(name)
```

---

## Notes

- `os.path.join()` is safer than manually concatenating path strings.
- Use `os.makedirs(path, exist_ok=True)` when creating nested folders.
- Prefer `pathlib` for new code, but be comfortable reading `os`-based code.
- Always check path existence before removing or opening files.

---

## Summary

- `os` and `os.path` are core tools for filesystem automation.
- They support path creation, folder listing, and existence checks.
- Modern Python often favors `pathlib`, but `os` remains important to understand.

---

## Practice Exercises

1. Print the current working directory with Python.
2. Use `os.path.join()` to build a path to `output/result.txt`.
3. Write a script that lists all items inside a folder using `os.listdir()`.

---

## Further Reading

- [os documentation](https://docs.python.org/3/library/os.html)
- [os.path documentation](https://docs.python.org/3/library/os.path.html)
