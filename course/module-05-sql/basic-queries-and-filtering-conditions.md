# Basic queries and filtering conditions

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Retrieve specific columns and rows
- Filter records using `WHERE`
- Sort and limit outputs for reporting

---

## Select and Filter

```sql
SELECT policy_id, holder_name, premium
FROM policies
WHERE status = 'ACTIVE';
```

---

## Multiple Conditions

```sql
SELECT claim_id, policy_id, claim_amount
FROM claims
WHERE claim_amount > 50000
  AND claim_status = 'PENDING';
```

---

## Sort and Limit

```sql
SELECT policy_id, premium
FROM policies
ORDER BY premium DESC
LIMIT 5;
```

---

## Summary

- Use `SELECT` for retrieval and `WHERE` for filtering.
- Combine conditions with `AND`/`OR`.
- Use `ORDER BY` and `LIMIT` for ranked views.

---

## Practice Exercises

1. Find all lapsed policies.
2. List top 10 highest claim amounts.
3. Select policies with premium between 15000 and 30000.
