# Implementing logging for debugging and monitoring

**Course:** Automation using Python — Part 1  
**Module 11:** Error Handling and Logging

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain why logging is important in automation scripts
- Use Python’s `logging` module for structured messages
- Record useful information for debugging and monitoring
- Choose appropriate log levels for different situations

---

## Introduction

When an automation script runs unattended, printed output may not be enough. Logging provides a structured way to record what happened, when it happened, and whether the script succeeded or failed. This is useful for debugging, monitoring, and audits.

---

## Key Concepts

### Why logging matters

Logging helps answer questions such as:

- Did the script run?
- Which step failed?
- How many records were processed?
- Was the output created successfully?

### The `logging` module

Python includes a built-in `logging` module that supports levels and output destinations such as the console or log files.

Common levels:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

### Typical logging practice

A script might:

- log start and finish times
- log major steps
- log warnings for unusual but non-fatal conditions
- log errors when failures occur

### Logging vs `print()`

`print()` is useful for quick tests, but logging is better for real automation because it is more structured and configurable.

---

## Examples

### Example 1: Basic logging setup

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Script started")
logging.warning("Input file is empty")
logging.error("Failed to connect to server")
```

### Example 2: Log to a file

```python
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Daily report generated")
```

### Example 3: Logging inside error handling

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    value = 10 / 0
except ZeroDivisionError:
    logging.exception("Calculation failed")
```

---

## Notes

- Use `INFO` for normal progress messages.
- Use `WARNING` for suspicious conditions that do not stop the script.
- Use `ERROR` or `exception()` when something fails.
- Keep log messages clear and specific.

---

## Summary

- Logging records what happens inside an automation script.
- The `logging` module is more useful than `print()` for production-style automation.
- Good logs improve debugging, monitoring, and operational visibility.

---

## Practice Exercises

1. Configure logging and record a script start message.
2. Write a log message to a file with a timestamp format.
3. Catch an exception and log it using `logging.exception()`.

---

## Further Reading

- [logging documentation](https://docs.python.org/3/library/logging.html)
