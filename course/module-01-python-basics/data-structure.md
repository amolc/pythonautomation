# Data Structure

**Course:** Automation using Python — Part 1  
**Module 1:** Python Basics

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Describe lists, tuples, dictionaries, and sets and when to use each
- Create and access elements in each structure
- Explain mutability vs immutability
- Model simple automation data (records, unique tags, ordered queues) with the right structure
- Combine structures (e.g., list of dicts) for realistic datasets

---

## Introduction

**Data structures** organize multiple values. Automation rarely deals with a single number—you work with **lists of files**, **dictionaries of settings**, **unique error codes**, or **fixed coordinate pairs**.

Python’s four essential built-in collections are:

| Structure | Ordered | Mutable | Duplicates | Syntax |
|-----------|---------|---------|------------|--------|
| **list** | Yes | Yes | Allowed | `[1, 2, 3]` |
| **tuple** | Yes | No | Allowed | `(1, 2, 3)` |
| **dict** | Yes* | Yes (keys unique) | Keys unique | `{"a": 1}` |
| **set** | No | Yes | No | `{1, 2, 3}` |

\*Python 3.7+ preserves insertion order in dicts.

---

## Lists

Ordered, mutable sequences—your default “collection of items.”

```python
files = ["report.csv", "summary.csv", "archive.zip"]
files.append("notes.txt")
files[0] = "report_v2.csv"

print(len(files))       # 4
print(files[-1])        # last item: notes.txt
```

### Creating lists

```python
empty = []
numbers = list(range(5))   # [0, 1, 2, 3, 4]
same = [0] * 3              # [0, 0, 0] — careful with mutable items
```

### Nested lists

```python
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
```

---

## Tuples

Like lists but **immutable**—good for fixed records you should not accidentally change.

```python
point = (10, 20)
rgb = (255, 128, 0)

# Tuple unpacking
x, y = point
print(x, y)

# Single-element tuple needs a comma
singleton = (42,)
```

Use tuples for:

- Coordinates, date parts that stay together
- Returning multiple values from a function
- Dictionary keys (lists cannot be keys)

```python
config = {
    ("prod", "db"): "postgres://...",
    ("dev", "db"): "sqlite:///dev.db",
}
```

---

## Dictionaries

Key–value mappings—ideal for JSON-like records and configuration.

```python
job = {
    "id": "job-1042",
    "status": "running",
    "retries": 0,
}

job["status"] = "completed"
job["duration_sec"] = 45.2

print(job.get("owner", "system"))  # default if key missing
```

### Keys must be hashable

Strings, numbers, tuples (of immutables) work; lists do not.

```python
# invalid = {[1, 2]: "value"}  # TypeError
```

### Iterating

```python
for key in job:
    print(key, job[key])

for key, value in job.items():
    print(f"{key} => {value}")
```

---

## Sets

Unordered collections of **unique** items—fast membership tests and deduplication.

```python
tags = {"urgent", "billing", "urgent"}  # duplicate dropped
print(tags)  # {'urgent', 'billing'}

tags.add("ops")
print("urgent" in tags)  # True

failed_ids = set([101, 102, 101, 103])
print(failed_ids)  # {101, 102, 103}
```

### Set operations

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union: {1, 2, 3, 4, 5}
print(a & b)   # intersection: {3}
print(a - b)   # difference: {1, 2}
```

---

## Strings as Sequences

Strings behave like ordered sequences of characters (but are immutable):

```python
path = "logs/app.log"
print(path[0])      # l
print(path[-3:])    # log (slicing — see next chapter)
```

---

## Choosing the Right Structure

| Scenario | Structure |
|----------|-----------|
| Ordered queue of files to process | `list` |
| Fixed API version + host pair | `tuple` |
| User profile by field name | `dict` |
| Unique visitor IDs seen today | `set` |
| Tabular data (many rows) | `list` of `dict` (or pandas later) |

### Example: list of dicts (common in automation)

```python
runs = [
    {"id": 1, "ok": True, "files": 12},
    {"id": 2, "ok": False, "files": 0},
    {"id": 3, "ok": True, "files": 7},
]

success_count = sum(1 for r in runs if r["ok"])
print(f"Successful runs: {success_count}")
```

---

## Mutability Summary

```python
# Mutable — in-place changes affect all references
row = [1, 2, 3]
alias = row
alias.append(4)
print(row)  # [1, 2, 3, 4]

# Immutable — “change” creates new object
t = (1, 2)
# t.append(3)  # AttributeError
```

---

## Notes and Best Practices

- Use `dict.get(key, default)` instead of risking `KeyError`.
- Do not use a list as a default argument in functions (Module 4 pitfall)—use `None` and create inside.
- For config, prefer dicts or dedicated config files over dozens of separate variables.
- Serialize dicts/lists to JSON for APIs and logs (`json.dumps` in later modules).
- Sets are ideal for “already processed” IDs to avoid duplicate work.

---

## Summary

- **Lists** — ordered, mutable sequences for workflows and queues.
- **Tuples** — fixed, immutable records; useful for unpacking and dict keys.
- **Dicts** — labeled fields and configuration; mirror JSON objects.
- **Sets** — unique members and fast “seen before” tracking.
- Real automation data often uses **nested structures**, especially lists of dictionaries.

---

## Practice Exercises

### Exercise 1 — File processing queue

Create a list `queue` with paths:

`"/data/in/a.csv"`, `"/data/in/b.csv"`, `"/data/in/c.csv"`

Pop the first item (use `pop(0)` or slicing), append `"/data/in/d.csv"`, and print the final queue.

---

### Exercise 2 — Server record

Create a dict `server` with keys: `hostname`, `port`, `ssl`, `tags` (where `tags` is a set of at least two strings). Add a new tag `"monitored"` and change `port` to `443`.

Print each key-value pair on its own line.

---

### Exercise 3 — Deduplicate event IDs

Given:

```python
events = [1001, 1002, 1001, 1003, 1002, 1004]
```

Build a **set** `unique_events` and a **sorted list** `sorted_events` from it. Print both.

---

### Exercise 4 — Mini report table

Build `reports` as a list of three dicts with keys `name`, `size_kb`, `ok` (bool). Write a loop that prints only reports where `ok` is `True`, one per line:

`name: size_kb KB`

---

## Exercise Solutions

<details>
<summary>Click to reveal solutions</summary>

**Exercise 1:**

```python
queue = ["/data/in/a.csv", "/data/in/b.csv", "/data/in/c.csv"]
queue.pop(0)
queue.append("/data/in/d.csv")
print(queue)
```

**Exercise 2:**

```python
server = {
    "hostname": "api.internal",
    "port": 80,
    "ssl": False,
    "tags": {"prod", "east"},
}
server["tags"].add("monitored")
server["port"] = 443
for k, v in server.items():
    print(k, v)
```

**Exercise 3:**

```python
events = [1001, 1002, 1001, 1003, 1002, 1004]
unique_events = set(events)
sorted_events = sorted(unique_events)
```

**Exercise 4:** Example data and loop:

```python
reports = [
    {"name": "a.csv", "size_kb": 10, "ok": True},
    {"name": "b.csv", "size_kb": 0, "ok": False},
    {"name": "c.csv", "size_kb": 5, "ok": True},
]
for r in reports:
    if r["ok"]:
        print(f"{r['name']}: {r['size_kb']} KB")
```

</details>

---

## Further Reading

- [Built-in Types — Data structures](https://docs.python.org/3/library/stdtypes.html)
- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
