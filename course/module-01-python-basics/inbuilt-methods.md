# Inbuilt Methods

**Course:** Automation using Python — Part 1  
**Module 1:** Python Basics

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Use built-in functions such as `len()`, `min()`, `max()`, `sum()`, and `sorted()`
- Call common string methods for cleaning and parsing automation data
- Mutate lists with `append()`, `extend()`, `insert()`, `pop()`, and `remove()`
- Discover method documentation with `help()` and `dir()`
- Choose between in-place methods and functions that return new values

---

## Introduction

Python objects expose **methods**—functions attached to a value: `"  hi  ".strip()`, `[1, 2].append(3)`.

The standard library also provides **built-in functions** that work on many types: `len(items)`, `sorted(names)`.

Automation scripts rely on these daily to normalize text, count rows, sort filenames, and manage in-memory queues before writing to disk or APIs.

---

## Built-in Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `len(x)` | Length / item count | `len("abc")` → 3 |
| `min(x)` | Smallest item | `min([3, 1, 2])` → 1 |
| `max(x)` | Largest item | `max([3, 1, 2])` → 3 |
| `sum(iterable)` | Sum of numbers | `sum([10, 20])` → 30 |
| `sorted(x)` | New sorted list | `sorted("cba")` → `['a','b','c']` |
| `reversed(x)` | Iterator over reversed sequence | `list(reversed([1,2]))` → `[2,1]` |
| `any(iterable)` | True if any truthy | `any([0, "", 5])` → True |
| `all(iterable)` | True if all truthy | `all([1, 2, 3])` → True |
| `enumerate(x)` | Index + value pairs | `for i, v in enumerate(["a","b"]):` |
| `zip(a, b)` | Pair elements | `list(zip([1,2], "ab"))` |

```python
sizes = [1024, 512, 2048, 256]
print("Files:", len(sizes))
print("Largest:", max(sizes))
print("Total bytes:", sum(sizes))
print("Ascending:", sorted(sizes))
```

### `sorted()` vs `.sort()`

```python
nums = [3, 1, 2]
ordered = sorted(nums)   # new list; nums unchanged
print(nums, ordered)

nums.sort()              # in-place; returns None
print(nums)              # [1, 2, 3]
```

Use `sorted()` when you need to keep the original order elsewhere.

---

## String Methods (Essential for Automation)

Strings are immutable—methods return **new** strings.

| Method | What it does |
|--------|----------------|
| `.lower()` / `.upper()` | Case conversion |
| `.strip()` / `.lstrip()` / `.rstrip()` | Remove whitespace (or chars) |
| `.replace(old, new)` | Substring replacement |
| `.split(sep)` | Break into list |
| `.join(iterable)` | Combine strings |
| `.startswith()` / `.endswith()` | Prefix/suffix test |
| `.find(sub)` | Index of substring (-1 if missing) |
| `.count(sub)` | Occurrence count |

```python
raw = "  ERROR:  Disk Full  \n"
clean = raw.strip().lower().replace("  ", " ")
print(clean)  # error: disk full

csv_line = "id,name,status"
fields = csv_line.split(",")
print(fields)  # ['id', 'name', 'status']

header = ",".join(["id", "name", "status"])
print(header)
```

### Chaining

```python
email = "  User@Example.COM "
normalized = email.strip().lower()
print(normalized)  # user@example.com
```

### Checking content

```python
filename = "backup.tar.gz"
print(filename.endswith((".tar.gz", ".zip")))
print(filename.startswith("backup"))
```

---

## List Methods

| Method | Effect |
|--------|--------|
| `.append(x)` | Add one item to end |
| `.extend(iterable)` | Add all items from iterable |
| `.insert(i, x)` | Insert at index |
| `.pop()` / `.pop(i)` | Remove and return item |
| `.remove(x)` | Remove first matching value |
| `.clear()` | Remove all |
| `.index(x)` | First index of value |
| `.count(x)` | Count occurrences |
| `.reverse()` | In-place reverse |
| `.copy()` | Shallow copy |

```python
pending = []
pending.append("job-1")
pending.extend(["job-2", "job-3"])
print(pending)

done = pending.pop(0)
print("Finished:", done)
print("Remaining:", pending)
```

### `append` vs `extend`

```python
a = [1, 2]
a.append([3, 4])      # [1, 2, [3, 4]] — nested list
b = [1, 2]
b.extend([3, 4])        # [1, 2, 3, 4]
```

---

## Dictionary Methods

```python
settings = {"retries": 1, "timeout": 30}

print(settings.keys())
print(settings.values())
print(settings.items())

settings.setdefault("retries", 5)   # set only if missing
settings.setdefault("log_level", "INFO")

removed = settings.pop("timeout", None)
print(removed, settings)
```

---

## Set Methods

```python
a = {1, 2, 3}
b = {3, 4}

a.update(b)           # in-place union
print(a)

a.discard(99)         # no error if missing
a.remove(1)           # KeyError if missing
```

---

## Discovering Methods: `help()` and `dir()`

```python
help(str.split)
print([m for m in dir(list) if not m.startswith("_")])
```

In the REPL, `help(list.append)` shows signature and docstring—useful when you forget parameter order.

---

## Practical Example: Normalize a Log File

```python
lines = [
    "  INFO: Started ",
    "ERROR: Timeout ",
    "  info: done ",
]

normalized = []
for line in lines:
    text = line.strip().upper()
    if text.startswith("ERROR"):
        normalized.append(text + " [ALERT]")
    else:
        normalized.append(text)

for entry in normalized:
    print(entry)
```

---

## Method Chaining vs Readability

Prefer clarity over long chains:

```python
# Dense
# x = raw.strip().split(":")[1].lower().replace(" ", "_")

# Clearer for maintenance
part = raw.strip().split(":", 1)[1]
x = part.lower().replace(" ", "_")
```

---

## Notes and Best Practices

- Methods that mutate (`list.sort`, `list.append`) return **`None`**—do not assign their result.
- Normalize user and file input with `.strip()` before validation.
- Use `.join()` to build delimited text—not repeated `+` in loops (efficiency and clarity).
- Prefer `in` / `startswith` over manual slicing when checking prefixes.
- Read library docs for timezone-aware dates, regex (`re` module), and paths (`pathlib`) in later modules.

---

## Summary

- **Built-ins** (`len`, `min`, `max`, `sum`, `sorted`) work across types and keep code concise.
- **String methods** clean and parse text from logs, CSV, and APIs.
- **List methods** manage work queues; know **`append` vs `extend`**.
- **Dict/set methods** support defaults, safe removal, and set algebra.
- Use **`help()`** and **`dir()`** to explore unfamiliar objects interactively.

---

## Practice Exercises

### Exercise 1 — File stats

```python
files = ["report.csv", "data.json", "image.png", "backup.csv"]
sizes = [1200, 800, 5000, 1200]
```

Print:

1. Number of files
2. Largest size
3. Total size
4. Filenames sorted alphabetically (use `sorted()` without changing `files`)

---

### Exercise 2 — Clean usernames

```python
raw_users = ["  Alice ", "BOB", "  charlie", "bob", ""]
```

Produce `clean_users`:

- Strip whitespace
- Lowercase
- Skip empty strings
- Remove duplicates while preserving first-seen order (hint: loop + list, or dict.fromkeys)

Print `clean_users`. Expected order: `alice`, `bob`, `charlie`.

---

### Exercise 3 — Work queue simulation

Start with `queue = ["email", "backup", "report"]`.

1. `append` `"cleanup"`
2. `pop` from the front until one item remains
3. Print each popped job and the final queue

---

### Exercise 4 — Method discovery

Pick any string method from `dir(str)` that we did not cover in this chapter. In a short comment, describe what it does and demonstrate it on `"automation"`.

---

## Exercise Solutions

<details>
<summary>Click to reveal solutions</summary>

**Exercise 1:**

```python
files = ["report.csv", "data.json", "image.png", "backup.csv"]
sizes = [1200, 800, 5000, 1200]

print(len(files))
print(max(sizes))
print(sum(sizes))
print(sorted(files))
```

**Exercise 2:**

```python
raw_users = ["  Alice ", "BOB", "  charlie", "bob", ""]
seen = set()
clean_users = []
for u in raw_users:
    name = u.strip().lower()
    if not name or name in seen:
        continue
    seen.add(name)
    clean_users.append(name)
print(clean_users)
```

Alternative: `list(dict.fromkeys(...))` after filtering.

**Exercise 3:**

```python
queue = ["email", "backup", "report"]
queue.append("cleanup")
while len(queue) > 1:
    job = queue.pop(0)
    print("Popped:", job)
print("Final queue:", queue)
```

**Exercise 4** (example with `.title()`):

```python
# .title() — title-cases words
print("automation pipeline".title())  # Automation Pipeline
```

</details>

---

## Further Reading

- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Text Sequence Methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [Mutable Sequence Types (list methods)](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
