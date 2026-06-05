# Module 16: Pandas and DataFrames

**Automation using Python — Part 1**

In this module, you will learn the fundamentals of working with tabular data and arrays in Python. We will explore NumPy for high-performance numerical operations and Pandas for reading, writing, cleaning, selecting, filtering, grouping, and exporting structured datasets.

---

## Learning Outcomes

By the end of this module, you will be able to:
- Create, inspect, and reshape NumPy arrays.
- Perform mathematical and statistical operations on arrays.
- Instantiate Pandas DataFrames from dictionaries and lists.
- Load data from CSV files and export modified DataFrames back to CSV.
- Select specific rows, columns, and cell elements using label-based `loc` and index-based `iloc` slicing.
- Filter, clean, sort, and aggregate tabular datasets.

---

## Prerequisites

- Python 3.9 or newer installed.
- Required packages: `numpy` and `pandas`.
- Set up and install in your virtual environment:
  ```bash
  pip install numpy pandas
  ```

---

## Chapters

| # | Chapter | Topics |
|---|---------|--------|
| 1 | [Introduction to NumPy and Arrays](./introduction-to-numpy-and-arrays.md) | What NumPy is, 1D and 2D arrays, inspecting array shape, dimensions, size, and data types |
| 2 | [NumPy Operations and Math](./numpy-operations-and-math.md) | Array arithmetic, statistical functions, reshaping arrays, automatic generation (`zeros`, `ones`, `arange`, `linspace`) |
| 3 | [Introduction to Pandas and DataFrames](./introduction-to-pandas-and-dataframes.md) | What Pandas is, creating DataFrames from raw data, inspecting datasets (`head`, `tail`, `info`, `describe`), selecting columns |
| 4 | [Data Selection and Filtering](./data-selection-and-filtering.md) | Filtering rows on single/multiple conditions, selecting values using `loc` and `iloc` indexers |
| 5 | [Data Manipulation and Cleaning](./data-manipulation-and-cleaning.md) | Updating data cells, adding new calculated columns, dropping columns, sorting data, grouping and aggregation (`groupby`), handling missing data (`isnull`, `fillna`) |
| 6 | [File I/O and Real-World Case Study](./file-io-and-real-world-case-study.md) | Reading from CSV, exporting to CSV, complete end-to-end employee salary case study |

---

## Module Capstone Exercise

Build a standalone script `pandas_capstone.py` that accomplishes the following:

1. Create a dictionary representing student grade data:
   - Names: Amol, Snehal, Rahul, Priya, Amit, and a missing value (`None`).
   - Marks: 85, 92, 78, 88, 65, and a missing value (`None`).
   - City: Pune, Mumbai, Delhi, Pune, Bangalore, and Pune.
2. Load this dictionary into a Pandas DataFrame.
3. Clean the missing grade values by filling them with the average mark of all other students. Fill any missing name with "Unknown Student".
4. Add a new Boolean column `Passed` which is `True` if `marks >= 80`, else `False`.
5. Filter the DataFrame to keep only students living in "Pune".
6. Export the final filtered table to a file named `pune_results.csv` without indexes.
7. Print a summary showing the average mark of students in Pune.
