# Operations on Data Structure

**Course:** Automation using Python — Part 1  
**Module 1:** Python Basics

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Index and slice sequences (strings, lists, tuples)
- Use positive and negative indices correctly
- Concatenate and repeat sequences with `+` and `*`
- Test membership with `in` and `not in`
- Apply common operators on lists and dicts (`+=`, slicing assignment, merging dicts)
- Avoid off-by-one errors when extracting substrings and sublists

---

## Introduction

Once data lives in lists, strings, or dicts, automation scripts **select**, **combine**, and **filter** it: take the file extension from a path, grab the first CSV row, or split a log line into fields.

This chapter covers the operations that apply across sequences and the most useful patterns for everyday scripting.

---

## Indexing

Positions start at **0** for the first element.

```python
items = ["alpha", "beta", "gamma"]

print(items[0])   # alpha
print(items[1])   # beta
print(items[2])   # gamma
# print(items[3])  # IndexError — out of range
```

### Negative indices

Count from the end: `-1` is the last item.

```python
print(items[-1])   # gamma
print(items[-2])   # beta
```

| Index | -3 | -2 | -1 |
|-------|----|----|-----|
| Value | alpha | beta | gamma |

---

## Slicing

Syntax: `sequence[start:stop:step]`

- **start** — included (default `0`)
- **stop** — excluded (default end)
- **step** — stride (default `1`)

```python
text = "automation"

print(text[0:4])    # auto
print(text[:4])     # auto  (from beginning)
print(text[4:])     # mation (through end)
print(text[:])      # full copy of string
print(text[::2])    # atoain — every 2nd character
print(text[::-1])    # noitamotua — reversed
```

### Slicing lists (returns a new list)

```python
nums = [10, 20, 30, 40, 50]
middle = nums[1:4]      # [20, 30, 40]
last_two = nums[-2:]    # [40, 50]
```

### Assignment to slices (lists only)

```python
data = [1, 2, 3, 4, 5]
data[1:3] = [99, 88]
print(data)  # [1, 99, 88, 4, 5]

data[:] = []  # clear in place
print(data)   # []
```

Strings and tuples do **not** support item assignment (immutable).

---

## Concatenation and Repetition

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Concatenate | `"log/" + "app.txt"` |
| `*` | Repeat | `"-" * 40` |

```python
header = "ID" + "," + "Name" + "," + "Status"
print(header)

separator = "=" * 50
print(separator)

paths = ["/in/"] * 3   # three references to SAME list — usually unintended
paths = ["/in/"] + ["/tmp/"] + ["/out/"]  # better
```

### Building paths safely

For real path work use `pathlib` (Module 7). For learning:

```python
base = "/var/log"
name = "app.log"
full = base + "/" + name
print(full)
```

---

## Membership: `in` and `not in`

Works on strings, lists, tuples, sets, and dict keys.

```python
allowed = {"csv", "json", "xml"}
filename = "report.CSV"

ext = filename.split(".")[-1].lower()
if ext in allowed:
    print("Extension OK")
else:
    print("Unsupported type")
```

```python
message = "ERROR: disk full"
if "ERROR" in message:
    print("Alert team")
```

```python
user = {"id": 42, "name": "Sam"}
print("email" in user)       # False — key check
print("id" in user)          # True
```

---

## Comparing Sequences

```python
print([1, 2] == [1, 2])   # True
print([1, 2] < [1, 3])    # True — lexicographic order
print("ab" < "ac")        # True
```

---

## List Operations

```python
a = [1, 2]
b = [3, 4]

combined = a + b           # [1, 2, 3, 4]
a += [5]                   # in-place: a is [1, 2, 5]
repeated = [0] * 4         # [0, 0, 0, 0]

print(len(a))
print(2 in a)
```

### Shallow copy vs reference

```python
original = [1, [2, 3]]
shallow = original[:]
shallow[0] = 99
shallow[1].append(4)
print(original)  # [1, [2, 3, 4]] — nested list shared
```

Use `copy.deepcopy()` when nesting matters (stdlib `copy` module).

---

## Dictionary Operations

```python
defaults = {"retries": 1, "timeout": 30}
overrides = {"timeout": 60}

# Merge (Python 3.9+)
config = defaults | overrides
print(config)  # {'retries': 1, 'timeout': 60}

# Update in place
defaults.update(overrides)
```

```python
keys = list(config.keys())
values = list(config.values())
pairs = list(config.items())
```

---

## Set Operations (Recap)

```python
seen = set()
for job_id in [1, 2, 1, 3]:
    if job_id not in seen:
        print("Processing", job_id)
        seen.add(job_id)
```

---

## Practical Automation Examples

### Extract file extension

```python
path = "/archive/report.final.csv"
parts = path.split(".")
ext = parts[-1] if len(parts) > 1 else ""
print(ext)  # csv
```

### First and last log line

```python
lines = ["start", "processing", "done"]
first = lines[0]
last = lines[-1]
```

### Batch chunks (simple)

```python
ids = list(range(10))
batch_size = 3
for i in range(0, len(ids), batch_size):
    batch = ids[i : i + batch_size]
    print("Batch:", batch)
```

---

## Common Pitfalls

| Pitfall | Problem | Fix |
|---------|---------|-----|
| Off-by-one | `text[0:len(text)]` vs last index | Remember stop is exclusive |
| Empty slice | `text[5:5]` → `""` | Check lengths first |
| `[:-0]` | Returns empty (not full string) | Use `[:]` for full copy |
| Shared nested lists | Aliasing inner lists | `deepcopy` when needed |
| Case sensitivity | `"CSV" in {"csv"}` is False | Normalize with `.lower()` |

---

## Summary

- **Indexing** targets one element; **negative** indices count from the end.
- **Slicing** `start:stop:step` extracts sub-sequences; stop is **exclusive**.
- **`+`** and **`*`** concatenate and repeat; use carefully with mutable lists.
- **`in`** tests membership—essential for validation and filtering.
- **Dict merge** (`|`) and **update** combine configuration layers in automation scripts.

---

## Practice Exercises

### Exercise 1 — Path parsing

Given:

```python
path = "/opt/automation/jobs/nightly/run_2026-05-21.log"
```

Using only slicing and `split` (no `pathlib`):

1. Print the **filename** (`run_2026-05-21.log`)
2. Print the **date portion** `2026-05-21` from the filename (hint: split on `_` and `.`)

---

### Exercise 2 — Slice the queue

```python
queue = ["a", "b", "c", "d", "e", "f"]
```

Without modifying the original list, create:

- `first_three` — first 3 items
- `last_two` — last 2 items
- `reversed_queue` — reversed order
- `every_other` — items at indices 0, 2, 4

Print all four.

---

### Exercise 3 — Merge configs

```python
base = {"env": "prod", "retries": 1, "notify": True}
patch = {"retries": 3, "timeout": 120}
```

Produce `effective` where patch wins on conflicts. Print `effective`. Then check if `"timeout" in effective`.

---

### Exercise 4 — Filter extensions

```python
files = ["a.csv", "b.txt", "c.csv", "d.JSON", "e.csv"]
allowed = {"csv", "json"}
```

Build a new list `selected` containing only files whose extension (lowercase, after the last `.`) is in `allowed`. Print `selected`.

Expected: `['a.csv', 'c.csv', 'd.JSON']` if you lowercase extension before compare (`d.json` matches `json`).

---

## Exercise Solutions

<details>
<summary>Click to reveal solutions</summary>

**Exercise 1:**

```python
path = "/opt/automation/jobs/nightly/run_2026-05-21.log"
filename = path.split("/")[-1]
print(filename)
# run_2026-05-21 from run_2026-05-21.log
middle = filename.split("_", 1)[1]  # 2026-05-21.log
date_part = middle.split(".")[0]
print(date_part)
```

**Exercise 2:**

```python
queue = ["a", "b", "c", "d", "e", "f"]
first_three = queue[:3]
last_two = queue[-2:]
reversed_queue = queue[::-1]
every_other = queue[::2]
```

**Exercise 3:**

```python
base = {"env": "prod", "retries": 1, "notify": True}
patch = {"retries": 3, "timeout": 120}
effective = base | patch
print("timeout" in effective)  # True
```

**Exercise 4:**

```python
files = ["a.csv", "b.txt", "c.csv", "d.JSON", "e.csv"]
allowed = {"csv", "json"}
selected = []
for f in files:
    ext = f.split(".")[-1].lower()
    if ext in allowed:
        selected.append(f)
print(selected)
```

</details>

---

## Further Reading

- [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
- [pathlib](https://docs.python.org/3/library/pathlib.html) — preferred for paths in automation
