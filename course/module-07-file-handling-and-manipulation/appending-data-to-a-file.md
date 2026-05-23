# Appending data to a file

**Course:** Automation using Python — Part 1  
**Module 7:** File Handling and Manipulation

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Append new data to existing files without overwriting them
- Use append mode for logs and running summaries
- Understand how append behavior differs from write mode
- Add simple audit-style output to automation scripts

---

## Introduction

Sometimes a script should add new information to a file instead of replacing the old content. This is common for logs, history files, or daily status updates. In those cases, Python uses append mode.

---

## Key Concepts

### Append mode

Use `"a"` mode to add content to the end of a file:

```python
with open("run.log", "a", encoding="utf-8") as file:
    file.write("Finished\n")
```

If the file does not exist, Python creates it. If it exists, the new content is added after the existing content.

### Append vs write

- `"w"` overwrites the file
- `"a"` preserves the existing content and adds new data

### Common automation use cases

Append mode is useful for:

- execution logs
- daily run history
- error tracking
- status reports that grow over time

### Add timestamps or labels

Appending becomes more useful when each entry has context, such as a date, time, or process name.

---

## Examples

### Example 1: Append one log line

```python
with open("logs/run.log", "a", encoding="utf-8") as file:
    file.write("Automation completed successfully\n")
```

### Example 2: Append multiple values

```python
entries = ["Loaded file: claims.csv", "Processed 120 rows", "Export completed"]

with open("logs/process.log", "a", encoding="utf-8") as file:
    for entry in entries:
        file.write(entry + "\n")
```

### Example 3: Append a timestamped message

```python
from datetime import datetime

with open("logs/run.log", "a", encoding="utf-8") as file:
    timestamp = datetime.now().isoformat(timespec="seconds")
    file.write(f"[{timestamp}] Script finished\n")
```

---

## Notes

- Use append mode for logs and run history.
- Add newline characters so entries stay readable.
- Avoid appending unstructured text if another script will parse the file later.
- Consider timestamps for better traceability.

---

## Summary

- Append mode adds content to an existing file without deleting earlier data.
- It is especially useful for logs, history, and recurring status output.
- Good appended data should be readable, structured, and easy to trace.

---

## Practice Exercises

1. Append a new line to a file named `run.log`.
2. Write a script that appends three process messages to a log file.
3. Add a timestamped status line to a file using `datetime`.

---

## Further Reading

- [datetime documentation](https://docs.python.org/3/library/datetime.html)
- [Python I/O tutorial](https://docs.python.org/3/tutorial/inputoutput.html)
