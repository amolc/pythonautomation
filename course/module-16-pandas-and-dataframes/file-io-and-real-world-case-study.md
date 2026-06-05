# File I/O and Real-World Case Study

**Course:** Automation using Python — Part 1  
**Module 16:** Pandas and DataFrames

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Export Pandas DataFrames to CSV files.
- Load datasets from CSV files into DataFrames.
- Build complete end-to-end automation scripts that load, clean, analyze, and save structured tabular reports.

---

## Introduction

Automating administrative processes usually requires interacting with file systems. CSV (Comma-Separated Values) is the most common format for transferring structured tabular records. In this chapter, we will learn how to write to and read from CSV files, then tie together all NumPy and Pandas skills in a complete real-world employee dataset analysis script.

---

## Key Concepts

### Exporting to CSV
Use `df.to_csv("filename.csv", index=False)` to save your DataFrame. The parameter `index=False` is highly recommended as it prevents Pandas from writing the default numeric row indices (0, 1, 2...) as a separate unnamed column in the file.

### Reading from CSV
Use `pd.read_csv("filename.csv")` to load a CSV file directly back into a Pandas DataFrame.

---

## Examples

### Example 1: Exporting and Reading a CSV File
```python
import pandas as pd

# 1. Create a DataFrame
df = pd.DataFrame({
    "product": ["Apples", "Bananas"],
    "price": [1.2, 0.8]
})

# 2. Export to CSV
df.to_csv("products_output.csv", index=False)
print("CSV File Exported Successfully")

# 3. Read it back
loaded_df = pd.read_csv("products_output.csv")
print("\nLoaded DataFrame:\n", loaded_df)
```

### Example 2: Complete End-to-End Analysis Case Study
This example demonstrates a complete data workflow:
1. Define a raw employee dictionary.
2. Initialize the DataFrame.
3. Compute a new `bonus` column.
4. Filter for high-salary staff.
5. Demonstrate `.loc` and `.iloc` lookups.
6. Sort values by salary.
7. Compute average salaries by city.
8. Extract summary statistics.
9. Export the resulting tables.

```python
import pandas as pd
import numpy as np

# 1. Define raw data
employee_data = {
    "name": ["Amol", "Snehal", "Rahul", "Priya", "Amit"],
    "salary": [500000, 250000, 700000, 450000, 300000],
    "city": ["Pune", "Mumbai", "Delhi", "Pune", "Bangalore"],
    "experience": [5, 2, 7, 4, 3]
}

# 2. Convert to DataFrame
employees = pd.DataFrame(employee_data)
print("Original Data:")
print(employees)

# 3. Add a 10% bonus column
employees["bonus"] = employees["salary"] * 0.10
print("\nWith Bonus:")
print(employees)

# 4. Filter for employees with salary > 400,000
high_salary = employees[employees["salary"] > 400000]
print("\nHigh Salary Employees:")
print(high_salary)

# 5. loc Example (get row 0 name)
print("\nloc Example (Row 0 name):")
print(employees.loc[0, "name"])

# 6. iloc Example (get row 1, column 2 'city')
print("\niloc Example (Row 1, Column 2):")
print(employees.iloc[1, 2])

# 7. Sort by salary descending
sorted_employees = employees.sort_values(by="salary", ascending=False)
print("\nSorted By Salary:")
print(sorted_employees)

# 8. Group by city and get average salary
avg_salary_city = employees.groupby("city")["salary"].mean()
print("\nAverage Salary By City:")
print(avg_salary_city)

# 9. Get dataset statistics
print("\nStatistics:")
print(employees.describe())

# 10. Export to CSV
employees.to_csv("final_employee_data.csv", index=False)
print("\nFile Exported Successfully")
```

---

## Notes

- Make sure you have write permissions in your current directory when exporting files.
- If your CSV files use different delimiters (like tabs or semicolons), customize `read_csv` using the separator parameter: `pd.read_csv("file.txt", sep="\t")`.

---

## Summary

- Use `df.to_csv()` and `pd.read_csv()` to serialize and deserialize DataFrames.
- Pass `index=False` to avoid writing row indexes to the file.
- Grouping, filtering, and sorting functions can be chained together to build complete, automated analytical workflows.

---

## Practice Exercises

1. Create a script that defines a DataFrame of 5 movies with columns: `Movie Name`, `Release Year`, `Rating` (out of 10), and `Box Office Revenue` (in millions).
2. Save this movies DataFrame to `movies.csv` with `index=False`.
3. Load the data back from `movies.csv` into a new variable called `movies_df`.
4. Add a new column `Rating Out of 100` which multiplies `Rating` by 10.
5. Sort the movies by `Box Office Revenue` in descending order.
6. Group the movies by their release decade (or just print the mean rating) and write the sorted, modified DataFrame to `sorted_movies.csv`.

---

## Further Reading

- [Pandas IO Tools (Text, CSV, etc.)](https://pandas.pydata.org/docs/user_guide/io.html)
- [read_csv API reference](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [to_csv API reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
