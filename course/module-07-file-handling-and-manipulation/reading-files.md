# Reading files

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Read text files using different techniques
- Process file content line by line
- Understand when to use `read()`, `readline()`, and iteration
- Apply file reading to automation workflows

---

## Introduction

Reading file content is one of the most common automation tasks. Scripts often need to load configuration files, process reports, parse logs, or inspect downloaded text data.

Python provides several ways to read from files depending on the amount and structure of the content.

---

## Key Concepts

### Read the whole file

`read()` returns the entire file as one string.

Best for:

- small files
- quick inspection
- simple text processing

### Read one line at a time

`readline()` reads a single line.

Best for:

- step-by-step processing
- situations where you want only the first few lines

### Iterate through the file

Looping over the file object is memory-efficient and useful for larger files.

Best for:

- logs
- reports with many lines
- row-based processing

### Strip newline characters

Use `.strip()` or `.rstrip()` when you want cleaner text output.

---

## Examples

### Example 1: Read all content

```python
with open("input/report.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

### Example 2: Read one line

```python
with open("input/report.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()

print(first_line.strip())
```

### Example 3: Process a file line by line

```python
with open("input/report.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"{line_number}: {line.strip()}")
```

---

## Notes

- Use `read()` for small files and quick scripts.
- Use line-by-line iteration for larger files.
- Clean line endings with `.strip()` when printing or comparing text.
- Always open text files with the correct encoding when possible.

---

## Summary

- Python supports multiple file-reading patterns.
- The right method depends on file size and processing needs.
- Line-by-line reading is often best for automation scripts.

---

## Practice Exercises

1. Read a text file and print the full contents.
2. Read only the first line of a file.
3. Print each line of a file with its line number.

---

## Further Reading

- [Python file methods](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
