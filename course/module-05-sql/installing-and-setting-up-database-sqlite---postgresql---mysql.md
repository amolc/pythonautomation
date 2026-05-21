# Installing and setting up database (sqlite / postgresql / mysql)

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Set up local SQL environments
- Understand where each database is useful
- Create a starter schema for practice

---

## Quick Setup Choices

### SQLite
- No server required
- Best for local training and small automation scripts

### PostgreSQL
- Strong enterprise features
- Common in production insurance platforms

### MySQL
- Widely used in web and operational systems
- Strong ecosystem and tooling

---

## Starter Table Example

```sql
CREATE TABLE policies (
    policy_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    product_type TEXT NOT NULL,
    premium NUMERIC NOT NULL,
    status TEXT NOT NULL
);
```

---

## Summary

- Use SQLite for learning and lightweight automation.
- Use PostgreSQL/MySQL for larger multi-user systems.
- Start with a clean schema and consistent naming.

---

## Practice Exercises

1. Install SQLite and create a local DB file.
2. Create `customers` and `claims` tables.
3. Insert three rows in each table.
