# Built-in String Functions

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Use useful Python built-ins with strings
- Combine methods and built-ins for fast cleaning
- Validate data with `any()` and `all()`

---

## Useful Built-ins

```python
policy_id = "POL-2026-0009"
print(len(policy_id))
print(min(policy_id))
print(max(policy_id))
print(sorted(policy_id))
```

---

## Practical Example

```python
names = ["anita", "RAVI", "meera"]
normalized = [n.title() for n in names]

print("Count:", len(normalized))
print("Sorted:", sorted(normalized))
print("All non-empty:", all(n != "" for n in normalized))
```

---

## Summary

- Built-ins like `len`, `sorted`, `min`, `max`, `any`, and `all` are powerful.
- They reduce custom code.
- Combine them with string methods for clean automation scripts.

---

## Practice Exercises

1. Print length of each policy ID.
2. Sort customer names after title-casing.
3. Check if all policy IDs start with `POL`.
