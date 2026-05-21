# Common String Methods

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Clean incoming text data
- Normalize case and spacing
- Validate basic string conditions

---

## Frequently Used Methods

```python
name = "  anita shah  "
print(name.strip().title())

email = "CUSTOMER@MAIL.COM"
print(email.lower())

status = "claim approved"
print(status.upper())
```

---

## Split and Join

```python
line = "POL001,ACTIVE,19500"
parts = line.split(",")
print(parts)
print(" | ".join(parts))
```

---

## Validation

```python
policy_id = "POL20260001"
print(policy_id.startswith("POL"))
print(policy_id.isalnum())
```

---

## Summary

- String methods are essential for data cleanup.
- Use `strip`, `lower`, `upper`, `title`, `split`, `join` regularly.
- Validate before processing.

---

## Practice Exercises

1. Clean a mixed-case customer name.
2. Split a CSV string into fields.
3. Verify a policy ID starts with `POL`.
