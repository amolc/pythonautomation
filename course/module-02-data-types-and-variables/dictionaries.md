# Dictionaries

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Create and update dictionaries
- Access keys safely
- Model policy and claim records

---

## Introduction

Dictionaries map keys to values and are ideal for structured insurance data.

```python
policy = {
    "policy_id": "POL-2026-0081",
    "holder_name": "Anita Shah",
    "premium": 18500,
    "status": "ACTIVE"
}
```

---

## Access and Update

```python
print(policy["holder_name"])
print(policy.get("nominee", "Not Provided"))

policy["premium"] = 19250
policy["renewal_due"] = "2026-12-31"
```

---

## Iterate

```python
for key, value in policy.items():
    print(key, ":", value)
```

---

## Summary

- Dictionaries are key-value containers.
- Use `.get()` for optional fields.
- Use `.items()` for reporting and logs.

---

## Practice Exercises

1. Create a claim dictionary with 5 fields.
2. Update claim status from `PENDING` to `SETTLED`.
3. Print all key-value pairs.
