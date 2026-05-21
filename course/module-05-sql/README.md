# Module 5: SQL

**Automation using Python — Part 1**

This module introduces SQL fundamentals required for automation pipelines that read and update policy, customer, and claim data.

---

## Learning Outcomes

- Understand database types and relational concepts
- Set up SQLite/PostgreSQL/MySQL environments
- Write core SQL queries and filters
- Perform CRUD operations safely
- Use joins and aggregates for reporting

---

## Chapters

1. [Introduction to SQL](./introduction-to-sql.md)
2. [Types of databases relational vs non-relational](./types-of-databases-relational-vs-non-relational.md)
3. [Installing and setting up database (sqlite / postgresql / mysql)](./installing-and-setting-up-database-sqlite---postgresql---mysql.md)
4. [Basic queries and filtering conditions](./basic-queries-and-filtering-conditions.md)
5. [CRUD operations](./crud-operations.md)
6. [Basic queries with aggregate functions](./basic-queries-with-aggregate-functions.md)
7. [SQL joins](./sql-joins.md)
8. [Advanced queries](./advanced-queries.md)

---

## Module Capstone

Create a SQL report workflow for insurance operations:

1. Build `customers`, `policies`, and `claims` tables
2. Insert sample rows
3. Generate branch-wise claim count and premium summary
4. Detect customers with no active policy
5. Export query output for Python automation stage
