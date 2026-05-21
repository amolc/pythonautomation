# Loops - for and while loops

**Course:** Automation using Python — Part 1  
**Module 3:** Flow Control

---

## Learning Objectives

- Use `for` and `while` loops appropriately
- Control loop flow with `break` and `continue`
- Avoid infinite loops in production scripts

---

## `for` Loop Example

```python
claim_amounts = [15000, 80000, 120000]
for amount in claim_amounts:
    if amount > 100000:
        print("Escalate:", amount)
```

---

## `while` Loop Example

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print("Sending renewal reminder", attempts + 1)
    attempts += 1
```

---

## `break` and `continue`

```python
claims = ["CLM001", "", "CLM003", "STOP", "CLM005"]
for claim in claims:
    if claim == "":
        continue
    if claim == "STOP":
        break
    print("Processed", claim)
```

---

## Summary

- Use `for` when iterating known collections.
- Use `while` for condition-driven repeats.
- Use `break`/`continue` carefully for control.

---

## Practice Exercises

1. Print all active policy IDs from a list.
2. Use `while` to retry API call up to 5 times.
3. Skip invalid claim IDs and stop on sentinel value.
