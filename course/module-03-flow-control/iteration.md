# Iteration

**Course:** Automation using Python — Part 1  
**Module 3:** Flow Control

---

## Learning Objectives

- Understand repeated execution with iteration
- Process each record in a collection
- Use `range()` and `enumerate()` effectively

---

## What Is Iteration?

Iteration means repeating steps over items in a sequence.

```python
policy_ids = ["POL001", "POL002", "POL003"]
for pid in policy_ids:
    print("Processing", pid)
```

---

## `range()` and `enumerate()`

```python
for i in range(3):
    print("Batch", i + 1)

claims = ["CLM101", "CLM102"]
for index, claim_id in enumerate(claims, start=1):
    print(index, claim_id)
```

---

## Summary

- Iteration is essential for batch automation.
- `for` loops are commonly used for collections.
- `enumerate()` helps when index is also needed.

---

## Practice Exercises

1. Iterate through 10 policy IDs and print each.
2. Print index and claim ID using `enumerate()`.
3. Use `range()` to simulate 5 daily reminder attempts.
