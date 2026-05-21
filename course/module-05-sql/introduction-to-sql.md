# Introduction to SQL

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Understand what SQL is
- Query structured insurance data
- Connect SQL work to automation use cases

---

## What Is SQL?

SQL (Structured Query Language) is used to create, read, update, and delete data in relational databases.

In insurance, SQL is used for:

- Policy portfolio reporting
- Claim status tracking
- Renewal and lapse analytics
- Regulatory and audit extracts

---

## Basic Query Example

```sql
SELECT policy_id, holder_name, premium
FROM policies;
```

---

## Summary

- SQL is the standard language for relational data.
- It is critical for reporting and operational automation.
- Most Python automation workflows interact with SQL databases.

---

## Practice Exercises

1. Write a query to select all rows from `claims`.
2. Select only `policy_id` and `status` from `policies`.
3. Explain one insurance process where SQL helps automate reporting.
