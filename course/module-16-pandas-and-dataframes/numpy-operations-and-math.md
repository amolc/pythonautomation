# NumPy Operations and Math

**Course:** Automation using Python — Part 1  
**Module 16:** Pandas and DataFrames

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Perform element-wise mathematical operations on NumPy arrays.
- Calculate basic statistics (mean, median, sum, min, max) using NumPy functions.
- Reshape arrays between different dimensions.
- Use built-in helper functions to generate arrays automatically.

---

## Introduction

NumPy arrays allow fast mathematical computations without writing `for` loops. This capability is called vectorization. In this chapter, we will learn how to perform element-wise arithmetic, compute key summary statistics, reshape arrays to change their layout, and generate synthetic data arrays.

---

## Key Concepts

### Element-Wise Mathematical Operations
When you apply standard arithmetic operators (`+`, `-`, `*`, `/`) to two arrays of the same shape, NumPy performs the operation on corresponding elements.

### Reshaping Arrays
Use `.reshape(rows, cols)` to change the dimensions of an array without changing its data. The total number of elements must remain the exact same.

### Automated Array Generation
NumPy provides functions to initialize arrays quickly:
- **`np.zeros(shape)`**: Creates an array filled with zeros.
- **`np.ones(shape)`**: Creates an array filled with ones.
- **`np.arange(start, stop, step)`**: Returns evenly spaced values within a given interval (similar to Python's `range()`).
- **`np.linspace(start, stop, num)`**: Returns evenly spaced numbers over a specified interval.

### Statistical Functions
NumPy has fast built-in functions to compute statistics across a whole array or along specific axes:
- `np.mean()`: Arithmetic mean.
- `np.median()`: Median value.
- `np.max()` / `np.min()`: Maximum and minimum values.
- `np.sum()`: Sum of elements.

---

## Examples

### Example 1: Mathematical Operations
```python
import numpy as np

arr_a = np.array([10, 20, 30])
arr_b = np.array([1, 2, 3])

print("Addition:", arr_a + arr_b)          # Output: [11, 22, 33]
print("Subtraction:", arr_a - arr_b)       # Output: [9, 18, 27]
print("Multiplication:", arr_a * arr_b)    # Output: [10, 40, 90]
print("Division:", arr_a / arr_b)          # Output: [10.0, 10.0, 10.0]
```

### Example 2: Statistical Functions
```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(numbers))      # Output: 30.0
print("Median:", np.median(numbers))  # Output: 30.0
print("Maximum:", np.max(numbers))    # Output: 50
print("Minimum:", np.min(numbers))    # Output: 10
print("Sum:", np.sum(numbers))        # Output: 150
```

### Example 3: Reshaping Arrays
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print("Reshaped Array:")
print(reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

### Example 4: Generating Arrays Automatically
```python
import numpy as np

# 2x2 array of zeros
print("Zeros:\n", np.zeros((2, 2)))

# 3x3 array of ones
print("Ones:\n", np.ones((3, 3)))

# Range from 1 to 9 (exclusive)
print("Arange:", np.arange(1, 10))

# 5 linear points between 1 and 100
print("Linspace:", np.linspace(1, 100, 5))
```

---

## Notes

- When reshaping, the product of the new dimensions must equal the total size of the original array (e.g. an array of size 6 can be reshaped to `(2,3)`, `(3,2)`, `(1,6)`, or `(6,1)`).
- NumPy statistical functions can be called as functions (e.g., `np.mean(arr)`) or as methods on the array object (e.g., `arr.mean()`).

---

## Summary

- Basic operators (+, -, *, /) act element-wise on arrays of matching shape.
- Use `np.mean`, `np.median`, `np.sum`, `np.max`, and `np.min` for rapid calculations.
- Reshape layouts using `.reshape()`.
- Automatically initialize arrays using `zeros()`, `ones()`, `arange()`, or `linspace()`.

---

## Practice Exercises

1. Create a 1D array of 6 elements from 10 to 60. Calculate its mean and sum.
2. Reshape the 6-element array from Exercise 1 into a 2x3 2D array. Print the reshaped array.
3. Automatically generate an array containing 10 numbers evenly spaced between 0 and 1.
4. Multiply all elements of a 1D array `np.array([1, 2, 3, 4])` by 5 and print the result.

---

## Further Reading

- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [NumPy Array Reshaping](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
- [NumPy Statistics](https://numpy.org/doc/stable/reference/routines.statistics.html)
