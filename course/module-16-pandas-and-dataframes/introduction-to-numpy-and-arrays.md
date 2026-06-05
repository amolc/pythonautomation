# Introduction to NumPy and Arrays

**Course:** Automation using Python — Part 1  
**Module 16:** Pandas and DataFrames

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Explain the role of NumPy in Python data science and automation.
- Create 1D and 2D NumPy arrays from standard Python lists.
- Retrieve array attributes such as shape, dimensions, data type, and size.

---

## Introduction

**NumPy** (Numerical Python) is the foundational package for scientific computing in Python. It provides a powerful N-dimensional array object, tools for integrating C/C++ code, and advanced mathematical functions. Pandas builds directly on top of NumPy, making it essential to understand how arrays behave before working with DataFrames.

---

## Key Concepts

### Why NumPy?
Standard Python lists are highly flexible but slow for numerical processing. NumPy arrays (`ndarrays`) store elements in contiguous blocks of memory, allowing vectorization and fast mathematical operations.

### 1D Arrays
A one-dimensional array is like a single row or column of numbers (a vector).

### 2D Arrays
A two-dimensional array is a grid of numbers containing rows and columns (a matrix).

### Array Attributes
NumPy arrays expose key properties to inspect their structure:
- **`shape`**: A tuple representing the size of the array along each dimension (e.g., `(rows, columns)`).
- **`ndim`**: The number of dimensions or axes (e.g., `1` for a 1D vector, `2` for a 2D matrix).
- **`dtype`**: The data type of the array elements. Unlike Python lists, NumPy arrays must have homogeneous types.
- **`size`**: The total number of elements in the array.

---

## Examples

### Example 1: Create a 1D NumPy Array
```python
import numpy as np

# Create a 1D array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)
```

### Example 2: Create a 2D NumPy Array
```python
import numpy as np

# Create a 2D array (matrix)
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D Array:")
print(arr2)
```

### Example 3: Inspect Array Attributes
```python
import numpy as np

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Shape:", arr2.shape)        # Output: (2, 3)
print("Dimensions:", arr2.ndim)    # Output: 2
print("Data Type:", arr2.dtype)    # Output: int64 (or int32 depending on OS)
print("Size:", arr2.size)          # Output: 6
```

---

## Notes

- NumPy is typically imported as `np` by convention.
- All elements in a NumPy array must be of the same data type. If you mix floats and integers, NumPy will automatically "upcast" them (e.g. converting integers to floats).
- Accessing attributes like `shape` does not require parentheses because they are attributes, not methods.

---

## Summary

- NumPy provides high-performance homogeneous numerical arrays.
- Create arrays from Python lists using `np.array()`.
- Inspect structures using `.shape`, `.ndim`, `.dtype`, and `.size`.

---

## Practice Exercises

1. Create a 1D NumPy array with the numbers 10, 20, 30, 40, 50 and print its shape.
2. Create a 2D NumPy array with 3 rows and 3 columns containing numbers 1 through 9. Print its dimensions (`ndim`) and total size.
3. Create an array containing both integers and floating-point numbers. Print its `dtype` to see how NumPy handles mixed types.

---

## Further Reading

- [NumPy Array Creation Quickstart](https://numpy.org/doc/stable/user/quickstart.html#array-creation)
- [NumPy ndarray Attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes)
