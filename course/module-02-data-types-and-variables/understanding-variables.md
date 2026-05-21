# Understanding Variables

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Create and update variables correctly
- Follow good naming standards
- Understand mutable vs immutable behavior

---

## Variable Basics

A variable is a name that points to a value.

```python
customer_name = "Anita Shah"
sum_insured = 500000
```

Use business-meaningful names like `claim_status`, `renewal_due_date`, `branch_code`.

---

## Reassignment

```python
claim_status = "PENDING"
claim_status = "APPROVED"
```

---

## Mutable vs Immutable

```python
# Immutable
policy_type = "health"
policy_type = policy_type.upper()

# Mutable
pending_claims = ["CLM101", "CLM102"]
queue = pending_claims
queue.append("CLM103")
print(pending_claims)
```

Both `queue` and `pending_claims` point to the same list.

---

## Summary

- Variables are labels for values.
- Use clear names.
- Be careful when multiple names reference the same mutable object.

---

## Practice Exercises

1. Create 5 meaningful variables for policy processing.
2. Rename vague variables (`a`, `b`) into readable names.
3. Show list aliasing with two variables and one append operation.
