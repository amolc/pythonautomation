# Handling errors and exceptions in automation scripts

**Course:** Automation using Python — Part 1  
**Module 11:** Error Handling and Logging

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Explain what exceptions are in Python
- Use `try` and `except` blocks to handle failures
- Distinguish between recoverable and non-recoverable errors
- Make automation scripts safer and easier to troubleshoot

---

## Introduction

Automation scripts often interact with files, websites, databases, and external systems. Any of these steps can fail because of missing files, invalid data, permission issues, network problems, or unexpected input. Error handling helps a script respond clearly instead of crashing without explanation.

---

## Key Concepts

### What an exception is

An **exception** is a runtime error that interrupts normal program execution.

Common examples:

- `FileNotFoundError`
- `ValueError`
- `KeyError`
- `ZeroDivisionError`
- `TimeoutError`

### Basic error handling structure

Python uses `try` and `except` to catch exceptions:

```python
try:
    risky_code()
except SomeError:
    handle_problem()
```

This allows the script to show a meaningful message, log the problem, or continue with fallback logic.

### `else` and `finally`

- `else` runs if no exception occurs
- `finally` runs whether an error occurs or not

These blocks are useful for cleanup and success handling.

### Catch specific exceptions

It is better to catch specific exceptions than a broad `except Exception` unless you are logging and re-raising carefully. Specific handling makes scripts easier to debug.

### Error handling in automation

Good automation error handling should:

- explain what failed
- avoid silent failure
- prevent partial or unsafe work where possible
- keep logs or messages useful for later review

---

## Examples

### Example 1: Handle a missing file

```python
try:
    with open("input/report.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("Input file was not found")
```

### Example 2: Use `else` and `finally`

```python
try:
    number = int("25")
except ValueError:
    print("Invalid number")
else:
    print("Converted successfully:", number)
finally:
    print("Conversion step finished")
```

### Example 3: Validate data safely

```python
def calculate_average(total, count):
    try:
        return total / count
    except ZeroDivisionError:
        print("Count cannot be zero")
        return 0

print(calculate_average(100, 4))
print(calculate_average(100, 0))
```

---

## Notes

- Catch only the exceptions you expect and understand.
- Use clear error messages that identify the failed step.
- Do not hide serious failures unless you have a recovery plan.
- Combine error handling with logging for better visibility.

---

## Summary

- Exceptions are runtime errors that interrupt a script.
- `try`, `except`, `else`, and `finally` help control failure behavior.
- Good automation scripts handle errors clearly and safely.

---

## Practice Exercises

1. Write a script that tries to open a missing file and prints a friendly error message.
2. Convert a string to an integer and handle a possible `ValueError`.
3. Create a function that catches `ZeroDivisionError` and returns a safe default value.

---

## Further Reading

- [Python exceptions documentation](https://docs.python.org/3/tutorial/errors.html)
