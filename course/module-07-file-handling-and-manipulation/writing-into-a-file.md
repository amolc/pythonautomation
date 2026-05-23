# Writing into a file

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Write text data into files using Python
- Understand how write mode affects existing content
- Create output files for automation workflows
- Format written content clearly and safely

---

## Introduction

Automation scripts often produce output: reports, logs, summaries, transformed data, or status files. Writing to files allows a script to save results so they can be reviewed, shared, or used in later steps.

---

## Key Concepts

### Write mode

To write into a file, use `"w"` mode:

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

If the file does not exist, Python creates it. If it already exists, Python overwrites it.

### Writing strings

The `write()` method writes a string exactly as provided. If you want a new line, include `\n`.

### Structured output

It is often helpful to write files in a predictable format, such as:

- one item per line
- comma-separated text
- key-value lines
- timestamped log entries

### When writing is useful in automation

Examples:

- save a cleaned version of a report
- create an output summary for a manager
- store run results in a text file
- generate intermediate files for another script

---

## Examples

### Example 1: Write one message to a file

```python
with open("output/status.txt", "w", encoding="utf-8") as file:
    file.write("Automation run completed")
```

### Example 2: Write multiple lines

```python
lines = ["North branch: 12 claims", "South branch: 8 claims", "Total: 20 claims"]

with open("output/summary.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")
```

### Example 3: Write generated values

```python
total_premium = 24500
report_date = "2026-05-23"

with open("output/report.txt", "w", encoding="utf-8") as file:
    file.write(f"Report date: {report_date}\n")
    file.write(f"Total premium: {total_premium}\n")
```

---

## Notes

- `"w"` mode replaces existing content, so use it carefully.
- Ensure the parent output directory exists before writing.
- Add newline characters when writing multiple lines.
- Keep output format consistent so other scripts can read it later.

---

## Summary

- Writing to files allows automation scripts to store results.
- `"w"` mode creates or overwrites a file.
- Clear, structured output makes later automation easier.

---

## Practice Exercises

1. Write a file named `status.txt` containing one success message.
2. Save three lines of summary text into a new file.
3. Generate a text report with two labeled values using f-strings.

---

## Further Reading

- [Python file methods](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
