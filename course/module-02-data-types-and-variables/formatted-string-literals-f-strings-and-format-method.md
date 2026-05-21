# Formatted String Literals (f-strings and .format() method)

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Use f-strings for modern formatting
- Use `.format()` when templates are reusable
- Build dynamic business messages safely

---

## f-strings (Preferred)

```python
policy_id = "POL-2026-1881"
premium = 24500
status = "ACTIVE"

message = f"Policy {policy_id} is {status}. Annual premium: ₹{premium:,.2f}"
print(message)
```

---

## `.format()` Method

```python
template = "Claim {0} for {1} is {2}."
print(template.format("CLM-901", "Anita Shah", "SETTLED"))

print("Policy {id} renewed on {date}".format(id="POL-01", date="2026-05-21"))
```

---

## Summary

- Use f-strings in most current Python scripts.
- Use `.format()` when string templates are externalized.
- Both support number and alignment formatting.

---

## Practice Exercises

1. Print claim amount with 2 decimal places using f-string.
2. Recreate output using `.format()`.
3. Build an SMS template for renewal reminder.
