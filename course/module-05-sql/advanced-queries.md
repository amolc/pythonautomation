# Advanced queries

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Use subqueries and common table expressions (CTEs)
- Apply case-based logic in SQL
- Build advanced operational reports

---

## Subquery Example

Find claims above average amount:

```sql
SELECT claim_id, policy_id, claim_amount
FROM claims
WHERE claim_amount > (
    SELECT AVG(claim_amount) FROM claims
);
```

---

## CTE Example

```sql
WITH high_value_claims AS (
    SELECT claim_id, policy_id, claim_amount
    FROM claims
    WHERE claim_amount >= 100000
)
SELECT *
FROM high_value_claims;
```

---

## CASE Example

```sql
SELECT claim_id,
       claim_amount,
       CASE
           WHEN claim_amount >= 100000 THEN 'HIGH'
           WHEN claim_amount >= 25000 THEN 'MEDIUM'
           ELSE 'LOW'
       END AS risk_band
FROM claims;
```

---

## Summary

- Advanced SQL helps create intelligent business reports.
- Subqueries and CTEs improve modularity.
- `CASE` is useful for classification logic.

---

## Practice Exercises

1. Find policies with premium above average premium.
2. Use CTE to list active policies due for renewal this month.
3. Categorize premium values into slabs with `CASE`.
