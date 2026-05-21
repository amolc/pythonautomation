# Variables

**Course:** Automation using Python — Part 1  
**Module 1:** Python Basics

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Create variables and assign values using `=`
- Follow Python naming rules and PEP 8 conventions
- Reassign variables and understand that names refer to objects
- Use multiple assignment and swapping idioms
- Distinguish between variables and constants by convention
- Explain dynamic typing in practical automation scenarios

---

## Introduction

A **variable** is a name that refers to a value stored in memory. In automation scripts, variables hold file paths, counters, API tokens (from environment variables, not hard-coded secrets), and status messages.

Unlike some languages, Python does not require `int x = 5;`—you simply assign and Python infers the type dynamically.

---

## Creating Variables

Assignment uses a single equals sign `=`. It is **not** a mathematical equality test.

```python
host = "localhost"
port = 8080
is_running = True
```

Read assignment as: **“Attach the name on the left to the object on the right.”**

```python
x = 10
x = 20      # name x now refers to 20; 10 may be garbage-collected if unused
x = x + 5   # 25
print(x)
```

---

## Naming Rules and Conventions

### Hard rules (syntax)

| Rule | Valid | Invalid |
|------|-------|---------|
| Letters, digits, underscores | `retry_count` | `2fast` (starts with digit) |
| Case-sensitive | `Count` ≠ `count` | — |
| No reserved keywords | `status` | `class`, `for`, `if` |

```python
# SyntaxError examples (do not run as a block):
# class = "economy"
# my-var = 1
```

### PEP 8 conventions (style)

| Style | Example | Use for |
|-------|---------|---------|
| `snake_case` | `max_retries`, `log_file` | Variables, functions |
| `UPPER_SNAKE` | `MAX_SIZE`, `DEFAULT_PATH` | Module-level constants |
| Descriptive names | `elapsed_seconds` | Not `es` or `t` |

```python
# Constants by convention (still reassignable unless you enforce otherwise)
MAX_RETRIES = 3
DEFAULT_OUTPUT_DIR = "/var/automation/output"
```

---

## Dynamic Typing

The same name can refer to different types over time:

```python
status = 200          # int — HTTP OK code
status = "success"    # str — human-readable
status = True         # bool — simplified flag
```

For maintainability in production automation, **avoid reusing one name for unrelated meanings**. Prefer separate names: `http_code`, `status_message`, `job_succeeded`.

---

## Multiple Assignment

```python
# Same value to several names
x = y = z = 0

# Unpack a sequence into names
width, height = 1920, 1080
print(width, height)

# Swap without a temporary variable
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

Unpacking is common when parsing CSV rows or `split()` results:

```python
line = "error,Connection timeout,3"
level, message, code = line.split(",")
print(level, message, code)
```

---

## Variable Scope (Preview)

Inside a function, assignments create **local** names unless declared `global` (rare in good automation code):

```python
retries = 1  # module-level

def run_job():
    retries = 3  # local — does not change module-level retries
    print("inside", retries)

run_job()
print("outside", retries)  # still 1
```

Module 4 covers scope in depth.

---

## Deleting Names

```python
temp_data = [1, 2, 3]
del temp_data
# print(temp_data)  # NameError
```

Use `del` sparingly; usually reassignment or letting a function end is enough.

---

## Variables and Objects

Python variables are **references** (labels on objects):

```python
list_a = [1, 2, 3]
list_b = list_a      # both names refer to the SAME list
list_b.append(4)
print(list_a)        # [1, 2, 3, 4]

# Copy if you need independence
list_c = list_a.copy()
list_c.append(99)
print(list_a)        # unchanged by list_c
```

This matters when passing lists or dicts into functions that mutate them.

---

## Environment Variables in Automation

Store secrets in the environment, not in source code:

```python
import os

api_key = os.environ.get("API_KEY")
if not api_key:
    raise SystemExit("Set API_KEY before running this script")
```

You will use `os` heavily in Module 7.

---

## Notes and Best Practices

- Initialize counters and flags before loops: `processed = 0`, `errors = []`.
- Use `UPPER_SNAKE` for values that should not change during a run.
- Never name variables `list`, `dict`, `str`—they shadow built-ins.
- Prefer `snake_case` over `camelCase` in Python projects.
- Group related settings in a dict or config file (later modules).

---

## Summary

- Variables are created with **`name = value`**; types are inferred dynamically.
- Follow **snake_case** for variables and **UPPER_SNAKE** for constants.
- **Unpacking** (`a, b = 1, 2`) simplifies working with pairs and split strings.
- Names refer to **objects**; aliasing (`b = a`) shares mutable data unless you **copy**.
- Use environment variables for secrets in real automation deployments.

---

## Practice Exercises

### Exercise 1 — Batch rename counter

Simulate renaming files `photo_001.jpg` … `photo_005.jpg`:

```python
prefix = "photo"
extension = ".jpg"
start = 1
count = 5
```

Use a loop (or manual prints) to build and print each filename. Store the **last filename** in `last_file` and print it after the loop.

---

### Exercise 2 — Swap and unpack

Start with `source = "archive"`, `destination = "live"`. Swap them using tuple unpacking. Print both names to prove the swap.

Then unpack `metrics = "98.5,42,1200"` into `cpu`, `memory`, `disk` (as strings first, then convert `cpu` to float).

---

### Exercise 3 — Naming audit

Which names violate PEP 8 or shadow built-ins? Rewrite them.

```python
List = ["a", "b"]
fileName = "report.csv"
MAX_retries = 5
```

---

### Exercise 4 — Shared reference bug

Predict the output, then run:

```python
defaults = {"retries": 1}
run_a = defaults
run_b = defaults
run_b["retries"] = 5
print(run_a["retries"])
```

Fix the pattern so `run_a` and `run_b` have independent dicts with the same initial values.

---

## Exercise Solutions

<details>
<summary>Click to reveal solutions</summary>

**Exercise 1** (loop version):

```python
prefix = "photo"
extension = ".jpg"
start = 1
count = 5
last_file = None
for i in range(start, start + count):
    last_file = f"{prefix}_{i:03d}{extension}"
    print(last_file)
print("Last:", last_file)
```

**Exercise 2:**

```python
source = "archive"
destination = "live"
source, destination = destination, source

metrics = "98.5,42,1200"
cpu, memory, disk = metrics.split(",")
cpu = float(cpu)
```

**Exercise 3:** Use `file_list`, `file_name`, `MAX_RETRIES`.

**Exercise 4:** Use `.copy()`:

```python
run_a = defaults.copy()
run_b = defaults.copy()
run_b["retries"] = 5
```

</details>

---

## Further Reading

- [PEP 8 — Naming conventions](https://peps.python.org/pep-0008/#naming-conventions)
- [Python assignment statements](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)
