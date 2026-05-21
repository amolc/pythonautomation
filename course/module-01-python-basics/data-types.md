# Data Types

**Course:** Automation using Python — Part 1  
**Module 1:** Python Basics

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Name and use Python’s core built-in types: `int`, `float`, `str`, `bool`, and `None`
- Inspect types with `type()` and `isinstance()`
- Convert between types safely for automation tasks (parsing numbers from text, etc.)
- Predict the result of mixed-type operations
- Choose appropriate types when representing real-world automation data

---

## Introduction

Every value in Python has a **data type**. The type tells the interpreter what operations are valid: you can divide two numbers, but dividing two sentences is meaningless.

Automation scripts constantly juggle types: file paths are **strings**, retry counts are **integers**, success flags are **booleans**, and missing configuration might be **`None`**. Understanding types prevents subtle bugs—especially when reading CSV rows, API JSON, or user input.

---

## Built-in Types at a Glance

| Type | Example | Typical automation use |
|------|---------|-------------------------|
| `int` | `42`, `-7`, `0` | Counts, IDs, exit codes |
| `float` | `3.14`, `-0.5` | Percentages, timings, coordinates |
| `str` | `"hello"`, `'C:\\logs'` | Paths, messages, JSON text |
| `bool` | `True`, `False` | Feature flags, success/failure |
| `NoneType` | `None` | “No value yet” / optional setting |

Python also has collection types (`list`, `dict`, etc.) covered in the **Data Structure** chapter.

---

## Integers (`int`)

Whole numbers with unlimited size (only memory limits apply).

```python
files_processed = 128
exit_code = 0
year = 2026

# Underscores improve readability (PEP 515)
batch_size = 10_000
print(batch_size)  # 10000
```

### Arithmetic

```python
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...  (always float division)
print(10 // 3)  # 3         (floor division)
print(10 % 3)   # 1         (remainder)
print(2 ** 8)   # 256        (power)
```

---

## Floating-Point Numbers (`float`)

Approximate real numbers—fine for metrics, risky for exact money without `decimal`.

```python
cpu_usage = 87.5
duration_seconds = 0.1 + 0.2
print(duration_seconds)  # 0.30000000000000004  (binary float quirk)

# Round for display
print(round(duration_seconds, 2))  # 0.3
```

---

## Strings (`str`)

Immutable sequences of Unicode characters. Single or double quotes are equivalent.

```python
path = "C:/data/report.csv"
message = 'Process finished'

# Triple quotes for multiline templates
email_body = """Hello,

Your nightly backup completed successfully.
"""
```

### Escape sequences

```python
print("Line one\nLine two")      # newline
print("Tab\there")               # tab
print("Quote: \"inside\"")       # escaped quote
print(r"C:\new\folder")          # raw string — backslashes literal
```

---

## Booleans (`bool`)

Only two values: `True` and `False`. Subclass of `int` (`True == 1`, `False == 0`), but use them for logic—not math.

```python
job_ok = True
retry_enabled = False

print(job_ok and retry_enabled)  # False
print(job_ok or retry_enabled)   # True
print(not job_ok)                # False
```

### Truthiness

Many values act as “true” or “false” in conditions:

| Falsy | Truthy (examples) |
|-------|-------------------|
| `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}` | Non-zero numbers, non-empty strings/collections |

```python
name = ""
if name:
    print("Has name")
else:
    print("Name missing")  # runs — empty string is falsy
```

---

## `None` — Absence of Value

`None` is a singleton meaning **“no value assigned.”**

```python
result = None

if result is None:
    print("No result from API yet")
```

Use `is None` / `is not None`—not `== None` (style and correctness with custom objects).

---

## Checking Types

```python
value = "100"

print(type(value))           # <class 'str'>
print(type(value) == str)    # True

# isinstance() is preferred (handles inheritance)
print(isinstance(value, str))       # True
print(isinstance(100, (int, float)))  # True if numeric
```

In automation, log types when debugging bad API data:

```python
payload = {"count": "42"}  # string, not int!
print(type(payload["count"]))
```

---

## Type Conversion (Casting)

Convert explicitly when reading files or user input:

```python
age_text = "30"
age = int(age_text)
print(age + 1)  # 31

price = float("19.99")
count = int(3.9)   # truncates toward zero → 3

label = str(404)   # "404"
flag = bool(1)     # True
flag = bool(0)     # False
flag = bool("")    # False
```

### Safe conversion pattern

```python
raw = "not_a_number"
try:
    num = int(raw)
except ValueError:
    num = 0
    print(f"Invalid integer '{raw}', using default {num}")
```

You will formalize this with `try/except` in Module 11.

---

## Mixed-Type Operations

```python
print(3 + 5)        # 8   (int + int)
print(3 + 5.0)      # 8.0 (int + float → float)
# print("3" + 5)    # TypeError — must convert
print("3" + str(5)) # "35" (string concatenation)
print("repeat " * 3)  # "repeat repeat repeat "
```

---

## Type Hints (Preview)

Optional annotations document intent (Module 4 goes deeper):

```python
def process_rows(count: int, path: str) -> bool:
    ...
```

They do not change runtime behavior in standard Python but help editors and teammates.

---

## Notes and Best Practices

- Prefer `isinstance(x, int)` over `type(x) == int` when checking types.
- JSON numbers often arrive as `int` or `float`; JSON `null` becomes `None`.
- File paths on Windows may contain backslashes—use raw strings `r"..."` or forward slashes.
- Do not use `float` for currency; use `decimal.Decimal` when precision matters.
- Name booleans clearly: `is_active`, `has_error`, `should_retry`.

---

## Summary

- Core scalar types: **`int`**, **`float`**, **`str`**, **`bool`**, and **`None`**.
- Use **`type()`** and **`isinstance()`** to inspect values when debugging pipelines.
- **Cast** with `int()`, `float()`, `str()`, `bool()` when moving between text and numbers.
- **`/`** always returns a float; use **`//`** for integer division.
- Empty or zero values are often **falsy**—useful in automation conditionals.

---

## Practice Exercises

### Exercise 1 — Inventory counters

Create variables for:

- `items_in_stock` (integer): `150`
- `unit_price` (float): `12.5`
- `product_name` (string): `"USB-C Hub"`

Print the **total inventory value** (`items_in_stock * unit_price`) rounded to 2 decimal places using `round()`.

---

### Exercise 2 — Parse configuration strings

Simulate reading config from a text file (values are strings):

```python
max_retries = "3"
timeout_sec = "2.5"
debug = "false"
```

Convert each to the correct type (`int`, `float`, `bool`). For `bool`, treat `"true"` (case-insensitive) as `True`, anything else as `False`.

Print all three converted values and their types.

---

### Exercise 3 — Truthiness audit

Without running `if` blocks mentally only—then verify in Python—predict whether each prints “yes” or “no”:

```python
def check(label, value):
    if value:
        print(label, "yes")
    else:
        print(label, "no")

check("A", 0)
check("B", "0")
check("C", [])
check("D", None)
check("E", "False")
```

Write one paragraph explaining why `"False"` is truthy.

---

### Exercise 4 — Automation log line

Build a single string `log_line` from:

- `timestamp` = `"2026-05-21T08:00:00"`
- `level` = `"INFO"`
- `message` = `"Copied 12 files"`

Format: `[INFO] 2026-05-21T08:00:00 — Copied 12 files` using concatenation or an f-string (introduced fully in Module 2).

---

## Exercise Solutions

<details>
<summary>Click to reveal solutions</summary>

**Exercise 1:**

```python
items_in_stock = 150
unit_price = 12.5
product_name = "USB-C Hub"
total = items_in_stock * unit_price
print(round(total, 2))  # 1875.0
```

**Exercise 2:**

```python
max_retries = "3"
timeout_sec = "2.5"
debug = "false"

max_retries = int(max_retries)
timeout_sec = float(timeout_sec)
debug = debug.lower() == "true"

print(max_retries, type(max_retries))
print(timeout_sec, type(timeout_sec))
print(debug, type(debug))
```

**Exercise 3:** `B` and `E` print “yes” because non-empty strings are truthy—even `"0"` and `"False"`.

**Exercise 4:**

```python
timestamp = "2026-05-21T08:00:00"
level = "INFO"
message = "Copied 12 files"
log_line = f"[{level}] {timestamp} — {message}"
print(log_line)
```

</details>

---

## Further Reading

- [Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
