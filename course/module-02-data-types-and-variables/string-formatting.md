# String Formatting

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Format data for logs and reports
- Control alignment and decimal precision
- Create readable premium summaries

---

## Formatting Example

```python
policy_id = "POL-7781"
premium = 12345.6789

print(f"Policy: {policy_id:>12}")
print(f"Premium: {premium:,.2f}")
```

Output:

```text
Policy:     POL-7781
Premium: 12,345.68
```

---

## Table Output Example

```python
rows = [("POL001", "ACTIVE", 18000), ("POL002", "LAPSED", 9500)]
print(f"{'Policy':<10}{'Status':<10}{'Premium':>12}")
for policy, status, amount in rows:
    print(f"{policy:<10}{status:<10}{amount:>12,.2f}")
```

---

## Summary

- Formatting improves readability and professionalism.
- Use width specifiers and precision values.
- Format money consistently.

---

## Practice Exercises

1. Format claim amount with commas and 2 decimals.
2. Left-align policy ID and right-align premium.
3. Print a 3-column report from tuples.
