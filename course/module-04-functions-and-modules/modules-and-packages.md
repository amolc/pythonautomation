# Modules and Packages

**Course:** Automation using Python — Part 1  
**Module 4:** Functions and Modules

---

## Learning Objectives

- Understand modules and packages
- Organize related Python files logically
- Improve reuse and team collaboration

---

## Concepts

- **Module**: a single `.py` file
- **Package**: a folder containing related modules (often with `__init__.py`)

Example structure:

```text
insurance_tools/
  __init__.py
  premium.py
  claims.py
  reporting.py
```

---

## Why It Matters in Insurance Automation

When scripts grow (renewals, claims, reminders, reconciliation), splitting logic into modules avoids monolithic files and simplifies maintenance.

---

## Summary

- Use modules to split functionality.
- Use packages to group related modules.
- Better structure leads to easier testing and onboarding.

---

## Practice Exercises

1. Create two modules: `premium.py` and `claims.py`.
2. Move related functions to each module.
3. Create package folder `insurance_tools` and organize files.
