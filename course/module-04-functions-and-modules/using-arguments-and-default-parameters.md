# Using Arguments and Default Parameters

**Course:** Automation using Python — Part 1  
**Module 4:** Functions and Modules

---

## Learning Objectives

- Use positional and keyword arguments
- Set practical default parameter values
- Design functions for optional business rules

---

## Positional and Keyword Arguments

```python
def create_policy_notice(policy_id, status):
    return f"Policy {policy_id} is {status}."

print(create_policy_notice("POL001", "ACTIVE"))
print(create_policy_notice(status="LAPSED", policy_id="POL002"))
```

---

## Default Parameters

```python
def calculate_claim_settlement(claim_amount, deductible=1000):
    return max(0, claim_amount - deductible)

print(calculate_claim_settlement(25000))
print(calculate_claim_settlement(25000, deductible=2500))
```

---

## Summary

- Use defaults for common values.
- Prefer keyword arguments when clarity matters.
- Keep parameter order logical and simple.

---

## Practice Exercises

1. Create a function with default tax rate `18%`.
2. Call function using positional and keyword styles.
3. Add an optional `is_senior_citizen` parameter for discount logic.
