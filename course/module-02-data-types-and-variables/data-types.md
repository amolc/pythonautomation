# Data Types

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Understand core Python data types
- Convert values safely
- Use the right type for insurance workflows

---

## Introduction

Insurance automation scripts process policy numbers, premium amounts, claim counts, dates, and status flags. Using correct data types helps avoid bugs and incorrect reporting.

---

## Core Types

| Type | Example | Insurance Example |
|---|---|---|
| `int` | `3` | Number of open claims |
| `float` | `24500.75` | Annual premium amount |
| `str` | `"POL-2026-00129"` | Policy number |
| `bool` | `True` | Policy is active |
| `None` | `None` | Settlement date not available |

```python
policy_id = "POL-2026-00129"
premium = 24500.75
open_claims = 3
is_active = True
settled_on = None
```

---

## Type Conversion

```python
premium_text = "18000.50"
premium_value = float(premium_text)

claims_text = "2"
claims_count = int(claims_text)

print(type(premium_value), premium_value)
print(type(claims_count), claims_count)
```

Always validate user input before converting.

---

## Summary

- Data types control how values are stored and processed.
- Use `int`, `float`, `str`, `bool`, and `None` intentionally.
- Convert external data carefully.

---

## Practice Exercises

1. Create variables for policy ID, premium, and policy status with correct types.
2. Convert `"25000"` into number and add 10%.
3. Represent missing nominee value using `None`.
