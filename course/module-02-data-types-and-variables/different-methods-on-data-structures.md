# Different Methods on data structures

**Course:** Automation using Python — Part 1  
**Module 2:** Data Types and Variables

---

## Learning Objectives

- Use built-in methods on lists, dicts, and sets
- Select methods based on data shape
- Reduce manual loop code

---

## List Methods

```python
claims = ["CLM5", "CLM1", "CLM9"]
claims.sort()
claims.reverse()
print(claims.count("CLM5"))
```

## Dictionary Methods

```python
claim = {"id": "CLM5", "status": "PENDING"}
print(claim.keys())
print(claim.values())
claim.update({"status": "APPROVED"})
```

## Set Methods

```python
regions = {"north", "south"}
regions.add("east")
regions.discard("west")
print(regions)
```

---

## Summary

- Methods make code shorter and safer.
- Use structure-specific methods intentionally.
- Avoid reinventing built-in functionality.

---

## Practice Exercises

1. Sort claim IDs in descending order.
2. Update a policy dictionary with 3 new fields.
3. Add/remove items from a set of branch names.
