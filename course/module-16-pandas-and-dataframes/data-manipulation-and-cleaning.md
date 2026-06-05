# Data Manipulation and Cleaning

**Course:** Automation using Python — Part 1  
**Module 16:** Pandas and DataFrames

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Update values inside specific cells in a DataFrame.
- Add new calculated columns and delete existing columns.
- Sort DataFrame rows by one or more columns.
- Group rows based on matching values and calculate aggregations.
- Check for and fill in missing (`NaN`) values.

---

## Introduction

In typical automation tasks, raw data is rarely perfect. You will often need to modify values, add calculated fields (such as taxes or bonuses), delete unused columns, sort reports, and summarize data by category. In this chapter, we will master DataFrame updates, sorting, groupings, and data cleaning.

---

## Key Concepts

### Updating Data
You can modify specific cells by referencing their label indices using `.loc[row, col] = new_value`.

### Adding and Deleting Columns
- **Add**: Assign a series of values or a calculated expression directly: `df["new_col"] = df["col1"] * 0.10`.
- **Delete**: Use `.drop("col_name", axis=1)`. The `axis=1` parameter indicates that you are dropping a column rather than a row. By default, `.drop()` returns a new DataFrame copy; to modify the original in-place, pass `inplace=True` or reassign the result.

### Sorting Data
Use `df.sort_values(by="col_name", ascending=True)` to sort your rows. Set `ascending=False` for descending order.

### Grouping and Aggregating (`groupby`)
Use `.groupby("col1")` to group data by matching categories in `"col1"`, then chain an aggregation function (like `.mean()`, `.sum()`, `.count()`) on target columns. E.g. `df.groupby("city")["salary"].mean()` calculates the average salary for each city.

### Handling Missing Values
In Pandas, missing data is represented as `NaN` (Not a Number) or `None`.
- **Detect**: Use `df.isnull()` to return a boolean table where `True` marks missing cells.
- **Fill**: Use `df.fillna(value)` to replace all missing values with a default choice (like `0` or the mean of the column).

---

## Examples

### Example 1: Updating Data and Adding/Deleting Columns
```python
import pandas as pd

data = {
    "name": ["Amol", "Snehal", "Rahul", "Priya", "Amit"],
    "salary": [500000, 250000, 700000, 450000, 300000],
    "city": ["Pune", "Mumbai", "Delhi", "Pune", "Bangalore"],
    "experience": [5, 2, 7, 4, 3]
}
df = pd.DataFrame(data)

# 1. Update salary of row 0
df.loc[0, "salary"] = 600000
print("Updated Salary for Amol:\n", df.head(1))

# 2. Add 'bonus' column (10% of salary)
df["bonus"] = df["salary"] * 0.10
print("\nWith Bonus Column:\n", df)

# 3. Delete 'bonus' column
new_df = df.drop("bonus", axis=1)
print("\nAfter Dropping Bonus:\n", new_df)
```

### Example 2: Sorting and Grouping Data
```python
import pandas as pd

# Using the df from Example 1 (after updating Amol's salary to 600k)
# 1. Sort by salary descending
sorted_df = df.sort_values(by="salary", ascending=False)
print("Sorted by Salary (Descending):\n", sorted_df)

# 2. Group by city and find average salary
grouped = df.groupby("city")["salary"].mean()
print("\nAverage Salary by City:\n", grouped)
```

### Example 3: Handling Missing Values
```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing data
missing_data = {
    "name": ["Amol", "Snehal", None],
    "salary": [500000, None, 700000]
}
missing_df = pd.DataFrame(missing_data)

print("Original Table with Missing Data:\n", missing_df)

# Check for missing values
print("\nIs Null Check:\n", missing_df.isnull())

# Fill missing values (replacing NaN with 0)
filled_df = missing_df.fillna(0)
print("\nFilled Table (NaN replaced with 0):\n", filled_df)
```

---

## Notes

- Slicing methods like `drop()` and `sort_values()` return copies of the data by default. To modify the DataFrame in-place, pass `inplace=True`.
- Be careful with `fillna(0)` on numeric data. In statistics, replacing missing cells with `0` can distort mean and standard deviation calculations. Instead, consider filling with the column's mean: `df["salary"].fillna(df["salary"].mean())`.

---

## Summary

- Modify cells with `.loc[row, col] = value`.
- Add columns dynamically and drop columns using `.drop(..., axis=1)`.
- Sort DataFrames using `.sort_values(by="column")`.
- Split and aggregate tables by group using `.groupby("col")`.
- Screen and resolve empty cells using `.isnull()` and `.fillna()`.

---

## Practice Exercises

1. Create a DataFrame containing employee data: `Name`, `Department`, `Sales`.
2. Add a new column `Commission` which is equal to 5% of `Sales`.
3. Update the `Sales` of one employee to a higher value. Verify that their `Commission` updates if you recalculate.
4. Group the DataFrame by `Department` and calculate the total Sales in each department.
5. Create a copy of the DataFrame with some sales values set to `None`. Identify which rows have missing sales using `isnull()`, then fill those missing sales with the average Sales value of the company.

---

## Further Reading

- [Pandas GroupBy: Split-Apply-Combine](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Working with Missing Data in Pandas](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [sort_values API reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
