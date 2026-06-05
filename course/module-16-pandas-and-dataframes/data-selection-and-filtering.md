# Data Selection and Filtering

**Course:** Automation using Python — Part 1  
**Module 16:** Pandas and DataFrames

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Filter DataFrame rows using single and multiple logical conditions.
- Select data cells, rows, and columns using label-based `.loc`.
- Select data cells, rows, and columns using integer-based `.iloc`.
- Distinguish between index-based and label-based indexing.

---

## Introduction

Finding specific data in large datasets is a core task in automation. Pandas offers robust filtering features. In this chapter, we will learn how to write boolean filters to extract subsets of rows, and how to query rows and columns using labels (`.loc`) or integer indices (`.iloc`).

---

## Key Concepts

### Filtering Data (Boolean Masking)
To filter rows in a DataFrame, we pass a boolean condition inside the brackets: `df[condition]`.
- For single conditions: `df[df["column"] > value]`
- For multiple conditions: Combine them using bitwise logical operators like `&` (AND) or `|` (OR). You **must** wrap each condition in parentheses: `df[(cond1) & (cond2)]`.

### Label-Based Indexing with `.loc`
`.loc` matches elements by row index labels and column names.
- Syntax: `df.loc[row_label, column_label]`
- Supports slicing, lists, and boolean criteria:
  - `df.loc[0]` gets the first row (if label is 0).
  - `df.loc[0, "name"]` gets the "name" cell in the row labeled 0.
  - `df.loc[:, ["name", "salary"]]` gets all rows for specified columns.
  - `df.loc[0:2]` gets rows labeled 0 through 2 **inclusive**.

### Integer-Based Indexing with `.iloc`
`.iloc` matches elements by their physical integer position (0-indexed).
- Syntax: `df.iloc[row_position, column_position]`
- Matches by position rather than label:
  - `df.iloc[0]` gets the first row.
  - `df.iloc[0, 1]` gets the value in the first row, second column.
  - `df.iloc[0:3, 0:2]` gets first 3 rows (indices 0, 1, 2) and first 2 columns (indices 0, 1). Note that `.iloc` slices are **exclusive** of the stop index, matching standard Python slicing.

---

## Examples

### Example 1: Filtering Data on Single and Multiple Conditions
```python
import pandas as pd

data = {
    "name": ["Amol", "Snehal", "Rahul", "Priya", "Amit"],
    "salary": [500000, 250000, 700000, 450000, 300000],
    "city": ["Pune", "Mumbai", "Delhi", "Pune", "Bangalore"],
    "experience": [5, 2, 7, 4, 3]
}
df = pd.DataFrame(data)

# Single condition: salary > 400000
high_salary = df[df["salary"] > 400000]
print("High Salary Employees:\n", high_salary)

# Multiple conditions: salary > 300000 AND city is Pune
filtered = df[(df["salary"] > 300000) & (df["city"] == "Pune")]
print("\nFiltered (Salary > 300k & City is Pune):\n", filtered)
```

### Example 2: Selecting with `.loc`
```python
import pandas as pd

# Using the same df
# 1. Access first row by label
print("First Row:\n", df.loc[0])

# 2. Specific cell value
print("\nFirst Row Name:", df.loc[0, "name"])

# 3. All rows, selected columns
print("\nNames and Salaries:\n", df.loc[:, ["name", "salary"]])

# 4. Multiple rows (inclusive slicing)
print("\nRows 0 to 2:\n", df.loc[0:2, ["name", "city"]])
```

### Example 3: Selecting with `.iloc`
```python
import pandas as pd

# Using the same df
# 1. First row by position
print("First Row:\n", df.iloc[0])

# 2. First row, second column (salary)
print("\nFirst Row, Second Column:", df.iloc[0, 1])

# 3. Position-based slice: first 3 rows and first 2 columns (exclusive)
print("\nSlicing with iloc:\n", df.iloc[0:3, 0:2])
```

---

## Notes

- **Crucial difference**: Slicing with `.loc` is **inclusive** (e.g. `0:2` returns rows 0, 1, and 2). Slicing with `.iloc` is **exclusive** (e.g. `0:3` returns rows 0, 1, and 2, but not 3).
- Always use parentheses for combined boolean operations: `df[(df["A"] > 1) & (df["B"] < 3)]` (using `and` or `or` directly will fail).

---

## Summary

- Filter rows by passing boolean vectors into bracket indexing `df[...]`.
- Sift datasets by row/column labels using `.loc[row_label, col_label]`.
- Slice datasets by numerical positions using `.iloc[row_idx, col_idx]`.

---

## Practice Exercises

1. Create a DataFrame representing 5 books with columns: `Title`, `Author`, `Price`, and `Genre`.
2. Filter the books to find all books priced under $20.
3. Filter the books to find all books that are in the "Fiction" genre AND priced under $15.
4. Using `.loc`, print the `Title` and `Price` of the first book in the dataset (row index 0).
5. Using `.iloc`, slice the DataFrame to get the first 2 rows and the first 2 columns.

---

## Further Reading

- [Pandas Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [loc API reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
- [iloc API reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html)
