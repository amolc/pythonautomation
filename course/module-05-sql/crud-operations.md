# CRUD operations

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Perform Create, Read, Update, Delete operations
- Apply safe update and delete conditions
- Understand CRUD in insurance operations

---

## Create

```sql
INSERT INTO policies (policy_id, customer_id, product_type, premium, status)
VALUES ('POL-1001', 'CUS-501', 'HEALTH', 18000, 'ACTIVE');
```

## Read

```sql
SELECT * FROM policies WHERE policy_id = 'POL-1001';
```

## Update

```sql
UPDATE policies
SET premium = 19500
WHERE policy_id = 'POL-1001';
```

## Delete

```sql
DELETE FROM policies
WHERE policy_id = 'POL-1001';
```

---

## Summary

- CRUD operations are daily database tasks.
- Always use `WHERE` in update/delete statements.
- Validate impact before running destructive queries.

---

## Practice Exercises

1. Insert 3 claim records.
2. Update one claim status from `PENDING` to `APPROVED`.
3. Delete one test row using a safe filter.
