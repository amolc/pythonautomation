# Python operators

**Course:** Automation using Python — Part 1  
**Module 3:** Flow Control

---

## Learning Objectives

- Use arithmetic, comparison, and logical operators
- Write conditions used in policy and claim checks
- Combine operators for business rules

---

## Operator Types

| Type | Examples | Insurance use case |
|---|---|---|
| Arithmetic | `+`, `-`, `*`, `/` | Premium and tax calculation |
| Comparison | `==`, `!=`, `>`, `<` | Claim amount threshold checks |
| Logical | `and`, `or`, `not` | Multi-condition eligibility rules |
| Membership | `in`, `not in` | Check status in allowed list |

```python
claim_amount = 85000
is_fraud_flagged = False

high_value = claim_amount > 50000
send_manual_review = high_value and not is_fraud_flagged
print(send_manual_review)
```

---

## Summary

- Operators are the foundation of flow control.
- Use logical operators for real business decisions.
- Keep conditions readable with clear variable names.

---

## Practice Exercises

1. Check if premium is between 10000 and 30000.
2. Verify if claim status is in `["PENDING", "REVIEW"]`.
3. Write a condition for manual review based on amount and policy age.
