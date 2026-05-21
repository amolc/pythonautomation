# Types of databases relational vs non-relational

**Course:** Automation using Python — Part 1  
**Module 5:** SQL

---

## Learning Objectives

- Compare relational and non-relational databases
- Choose the right database style for business scenarios
- Understand why SQL is central for structured insurance data

---

## Relational vs Non-relational

| Type | Structure | Example systems | Insurance fit |
|---|---|---|---|
| Relational | Tables + relationships | PostgreSQL, MySQL, SQLite | Core systems: policies, claims, billing |
| Non-relational | Documents/key-value/graph | MongoDB, Redis | Logs, event streams, flexible metadata |

---

## Why Relational Is Common in Insurance

Insurance operations rely on strongly structured data and referential consistency:

- One customer can have many policies
- One policy can have many claims
- Auditability and compliance require strict data rules

---

## Summary

- Relational DBs are best for transactional insurance systems.
- Non-relational DBs are useful for flexible/unstructured workloads.
- SQL remains the primary language for core data operations.

---

## Practice Exercises

1. List two relational and two non-relational databases.
2. Explain why claims data fits relational modeling.
3. Identify one scenario where document DB may help in insurance.
