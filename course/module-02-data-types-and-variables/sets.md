# Sets

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Use sets for unique values
- Apply set operations for reconciliation
- Remove duplicates from uploaded data

---

## Introduction

Sets are unordered collections of unique values.

```python
policy_ids = {"POL001", "POL002", "POL003", "POL001"}
print(policy_ids)
```

---

## Set Operations

```python
active_policies = {"POL001", "POL002", "POL005"}
renewal_due = {"POL002", "POL004", "POL005"}

print("Common:", active_policies & renewal_due)
print("Only active:", active_policies - renewal_due)
print("All outreach:", active_policies | renewal_due)
```

---

## Summary

- Sets automatically remove duplicates.
- Use intersection, union, and difference for data matching.
- Best when order is not important.

---

## Practice Exercises

1. Remove duplicate branch codes from a list.
2. Find common policy IDs between two teams.
3. Find missing IDs using set difference.
