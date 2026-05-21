# Scope of Variables

**Course:** Automation using Python — Part 1  
**Module 4:** Functions and Modules

---

## Learning Objectives

- Understand local and global scope
- Prevent accidental side effects
- Write predictable function logic

---

## Local vs Global

```python
company_name = "SafeLife Insurance"  # global

def print_branch_info():
    branch = "Mumbai"  # local
    print(company_name, branch)

print_branch_info()
```

---

## Common Mistake

```python
counter = 0

def increment():
    global counter
    counter += 1
```

Avoid heavy use of `global`; prefer returning updated values.

---

## Better Pattern

```python
def increment(counter):
    return counter + 1

counter = increment(0)
print(counter)
```

---

## Summary

- Local scope keeps functions safer.
- Global variables can introduce hidden dependencies.
- Prefer parameter/return based updates.

---

## Practice Exercises

1. Create one local and one global variable and print both.
2. Rewrite a `global`-based counter function without `global`.
3. Explain why local scope is safer in automation scripts.
