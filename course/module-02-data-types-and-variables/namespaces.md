# Namespaces

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Understand local and global namespaces
- Avoid naming collisions
- Prevent bugs by not shadowing built-ins

---

## What Is a Namespace?

A namespace is a mapping of names to objects.

- **Local namespace**: inside a function
- **Global namespace**: at script level
- **Built-in namespace**: Python functions like `len`, `print`

---

## Example

```python
company = "SafeLife"  # global

def show_company():
    company = "SafeLife - Mumbai"  # local
    print(company)

show_company()
print(company)
```

---

## Pitfall

```python
# Avoid this
list = ["POL1", "POL2"]
```

This shadows Python's built-in `list()`.

---

## Summary

- Python resolves names from local to global to built-in.
- Keep names explicit and meaningful.
- Do not use built-in names for variables.

---

## Practice Exercises

1. Create local and global variables with same name and print both.
2. Shadow `sum` and observe the effect.
3. Refactor shadowed names.
