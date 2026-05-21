# Tuples

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Understand tuple behavior
- Use tuples for fixed-format records
- Apply tuple unpacking in clean code

---

## Introduction

A tuple is ordered but immutable. It works well when values should not change accidentally.

```python
policy_key = ("POL-2026-0001", "HEALTH")
```

---

## Tuple Operations

```python
record = ("CLM7781", "APPROVED", 25000)
print(record[0])
print(len(record))

claim_id, status, amount = record
print(claim_id, status, amount)
```

---

## Summary

- Tuples are immutable sequences.
- Use them for fixed records and returned values.
- Tuple unpacking improves readability.

---

## Practice Exercises

1. Create a tuple `(policy_id, customer_id, premium)` and unpack it.
2. Try modifying one tuple item and observe the error.
3. Store branch codes in a tuple and print the last item.
