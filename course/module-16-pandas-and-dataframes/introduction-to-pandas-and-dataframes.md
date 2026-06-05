# Introduction to Pandas and DataFrames

**Course:** Automation using Python — Part 1  
**Module 16:** Pandas and DataFrames

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Explain what Pandas is and how it represents tabular data.
- Create a DataFrame from standard Python dictionaries.
- Inspect a DataFrame's structure, shape, columns, and data types.
- Select single and multiple columns from a DataFrame.

---

## Introduction

**Pandas** is the standard library for data manipulation and analysis in Python. It provides fast, flexible, and expressive data structures designed to make working with relational or labeled data both easy and intuitive. In this chapter, we will look at the primary Pandas structure—the **DataFrame**—and learn how to inspect and navigate its columns.

---

## Key Concepts

### What is a DataFrame?
A DataFrame is a 2-dimensional labeled data structure, similar to a database table or an Excel spreadsheet. It consists of:
- **Columns**: Variables or features of the data.
- **Index**: Unique row identifiers (numbers starting from 0 by default).
- **Cells**: Individual data values.

### Creating DataFrames
We can easily convert raw Python data, such as a dictionary of lists, into a Pandas DataFrame using `pd.DataFrame(data)`.

### Inspecting Data
When loading a new dataset, use these basic inspection functions to understand its shape and contents:
- **`head(n)`**: Returns the first `n` rows of the DataFrame (defaults to 5).
- **`tail(n)`**: Returns the last `n` rows of the DataFrame (defaults to 5).
- **`columns`**: Returns a list of the column headers.
- **`dtypes`**: Shows the data type of each column.
- **`info()`**: Prints a detailed summary of the dataset including columns, non-null counts, types, and memory usage.
- **`describe()`**: Computes summary statistics (count, mean, standard deviation, min, max, quartiles) for numeric columns.

### Selecting Columns
- Select a single column using bracket syntax: `df["column_name"]` (returns a Pandas **Series**).
- Select multiple columns by passing a list of column names inside brackets: `df[["col1", "col2"]]` (returns a new **DataFrame**).

---

## Examples

### Example 1: Create a DataFrame
```python
import pandas as pd

data = {
    "name": ["Amol", "Snehal", "Rahul", "Priya", "Amit"],
    "salary": [500000, 250000, 700000, 450000, 300000],
    "city": ["Pune", "Mumbai", "Delhi", "Pune", "Bangalore"],
    "experience": [5, 2, 7, 4, 3]
}

df = pd.DataFrame(data)
print(df)
```

### Example 2: Inspect the DataFrame
```python
import pandas as pd

# Assume 'df' is defined as in Example 1
print("--- Head ---")
print(df.head(2))

print("\n--- Columns ---")
print(df.columns)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Info Summary ---")
df.info()

print("\n--- Summary Statistics ---")
print(df.describe())
```

### Example 3: Selecting Columns
```python
import pandas as pd

# Assume 'df' is defined as in Example 1

# Select single column
names = df["name"]
print("Single Column (Series):\n", names)

# Select multiple columns
subset = df[["name", "salary"]]
print("\nMultiple Columns (DataFrame):\n", subset)
```

---

## Notes

- Selecting a single column like `df["name"]` returns a 1D Pandas `Series`, while passing a list like `df[["name"]]` returns a 2D DataFrame.
- DataFrames align data automatically based on their indexes.

---

## Summary

- Pandas DataFrames store tabular data in rows and columns.
- Use `pd.DataFrame(dict)` to turn lists of dictionaries or dictionaries of lists into tables.
- Query datasets using `.head()`, `.tail()`, `.info()`, and `.describe()`.
- Slice columns out of a DataFrame using single brackets `df["col"]` or double brackets `df[["col1", "col2"]]`.

---

## Practice Exercises

1. Create a DataFrame containing details of 3 products: `Product Name`, `Price` (numeric), and `Stock` (integer).
2. Print the first 2 rows of your product DataFrame using `head()`.
3. Select and print only the `Product Name` column.
4. Select and print both the `Product Name` and `Price` columns together.
5. Inspect the summary statistics of the numeric columns in your DataFrame using `describe()`.

---

## Further Reading

- [Pandas Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [Pandas DataFrame reference](https://pandas.pydata.org/docs/reference/frame.html)
