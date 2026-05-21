# Defining Functions

**Course:** Automation using Python — Part 1  
**Module 4:** Functions and Modules

---

## Learning Objectives

- Define reusable functions
- Keep logic DRY (Don't Repeat Yourself)
- Improve readability and maintainability

---

## Why Functions?

Functions let you group logic once and reuse it many times.

```python
def greet_policy_holder(name):
    print(f"Hello {name}, your policy update is ready.")

greet_policy_holder("Anita")
greet_policy_holder("Rahul")
```

---

## Function Structure

```python
def function_name(parameters):
    # logic
    return value
```

---

## Insurance Example

```python
def calculate_total_premium(base_premium, rider_premium):
    return base_premium + rider_premium

print(calculate_total_premium(18000, 2500))
```

---

## Summary

- Functions reduce duplication.
- Keep functions focused on one task.
- Use clear names that match business intent.

---

## Practice Exercises

1. Write a function to print claim acknowledgment message.
2. Write a function that returns premium with GST.
3. Call each function with at least two sample inputs.
