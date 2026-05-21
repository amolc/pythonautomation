# SQL joins

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Combine data across related tables
- Choose correct join type
- Build customer-policy-claim reports

---

## Common Join Types

- `INNER JOIN` → matching rows only
- `LEFT JOIN` → all rows from left table + matches from right
- `RIGHT JOIN` → all rows from right table + matches from left

---

## Insurance Example

```sql
SELECT c.customer_id,
       c.customer_name,
       p.policy_id,
       p.status,
       cl.claim_id,
       cl.claim_amount
FROM customers c
LEFT JOIN policies p ON c.customer_id = p.customer_id
LEFT JOIN claims cl ON p.policy_id = cl.policy_id;
```

This query helps identify customers with policies but no claims, and customers with no policies.

---

## Summary

- Joins are essential for multi-table analysis.
- Use meaningful aliases for readability.
- Start with `LEFT JOIN` for complete customer views.

---

## Practice Exercises

1. Join policies with customers and show holder names.
2. Find policies with no claim using join + `IS NULL`.
3. Build a claim summary with customer name and product type.
