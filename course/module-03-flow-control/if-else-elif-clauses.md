# If, else, elif clauses

**Course:** Automation using Python — Part 1  
**Module 3:** Flow Control

---

## Learning Objectives

- Use branching logic in automation scripts
- Build multi-case business decision trees
- Keep conditional code clean and testable

---

## Basic Structure

```python
if condition_1:
    # do this
elif condition_2:
    # do this
else:
    # fallback
```

---

## Insurance Example: Claim Priority

```python
claim_amount = 125000
fraud_score = 82

if fraud_score >= 80:
    priority = "INVESTIGATE"
elif claim_amount >= 100000:
    priority = "HIGH"
elif claim_amount >= 25000:
    priority = "MEDIUM"
else:
    priority = "LOW"

print("Claim priority:", priority)
```

---

## Best Practices

- Order conditions from most specific to broad.
- Avoid deeply nested `if` blocks when possible.
- Move repeated logic into functions.

---

## Summary

- `if/elif/else` controls decision paths.
- Use it to implement policy and claims rules.
- Prioritize readability in business logic.

---

## Practice Exercises

1. Categorize customer age into `MINOR`, `ADULT`, `SENIOR`.
2. Set renewal discount slab using `if/elif/else`.
3. Route claim to `FAST_TRACK` or `MANUAL_REVIEW` based on amount and score.
