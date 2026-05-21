# Basic queries with aggregate functions

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Use aggregate functions for summary reporting
- Group records by business dimensions
- Build insurer dashboard metrics

---

## Common Aggregates

- `COUNT()` → number of records
- `SUM()` → total amount
- `AVG()` → average value
- `MIN()` and `MAX()` → smallest/largest value

```sql
SELECT COUNT(*) AS total_claims,
       SUM(claim_amount) AS total_claim_amount,
       AVG(claim_amount) AS avg_claim_amount
FROM claims;
```

---

## Grouped Summary

```sql
SELECT product_type,
       COUNT(*) AS policy_count,
       SUM(premium) AS total_premium
FROM policies
GROUP BY product_type;
```

---

## Summary

- Aggregates convert detailed rows into business insights.
- Use `GROUP BY` for category-wise analysis.
- Essential for operational and management reporting.

---

## Practice Exercises

1. Count active vs lapsed policies by status.
2. Find maximum claim amount per branch.
3. Calculate average premium by product type.
