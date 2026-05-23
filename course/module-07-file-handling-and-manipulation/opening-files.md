# Opening Files

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Open files using the correct file modes
- Understand read, write, and append behavior
- Use context managers for safe file handling
- Avoid common mistakes when opening files

---

## Introduction

Before Python can read from or write to a file, the file must be opened. File opening tells Python what file to access and how you plan to use it.

This is a basic but important skill because nearly every automation workflow reads input files or generates output files.

---

## Key Concepts

### The `open()` function

Python uses the built-in `open()` function:

```python
open("example.txt", "r")
```

The first argument is the file path. The second argument is the file mode.

### Common file modes

- `"r"` → read
- `"w"` → write (creates or overwrites)
- `"a"` → append
- `"rb"` → read binary
- `"wb"` → write binary

### Why context managers matter

The safest way to open files is with `with`:

```python
with open("example.txt", "r") as file:
    data = file.read()
```

This automatically closes the file after the block finishes, even if an error occurs.

### Text encoding

For text files, specify encoding when appropriate:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

This helps avoid text decoding issues across systems.

---

## Examples

### Example 1: Open and read a text file

```python
with open("input/report.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

### Example 2: Open a file for writing

```python
with open("output/result.txt", "w", encoding="utf-8") as file:
    file.write("Automation completed successfully")
```

### Example 3: Open a file for appending

```python
with open("logs/run.log", "a", encoding="utf-8") as file:
    file.write("Script finished\n")
```

---

## Notes

- Use `with open(...)` instead of opening a file manually and forgetting to close it.
- Be careful with `"w"` mode because it overwrites existing content.
- Use `encoding="utf-8"` for most text automation tasks.
- Check that the file path exists before opening in read mode.

---

## Summary

- Files must be opened before Python can read or write them.
- File modes control whether you read, write, or append.
- Context managers are the safest way to handle files.

---

## Practice Exercises

1. Open a text file and print its contents.
2. Create a new file and write one line into it.
3. Append a second line to the same file.

---

## Further Reading

- [open() documentation](https://docs.python.org/3/library/functions.html#open)
- [Python I/O tutorial](https://docs.python.org/3/tutorial/inputoutput.html)
