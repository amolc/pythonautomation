# Matplotlib Subplots and Pandas Integration

**Course:** Automation using Python — Part 1  
**Module 17:** Plotly and Matplotlib

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Draw multiple data traces on the same figure and use legends.
- Arrange grids of distinct plots using `plt.subplot()`.
- Extract data from Pandas DataFrames and plot it directly in Matplotlib.

---

## Introduction

In sophisticated reporting systems, you will often need to overlay multiple data series on a single chart for comparison, or organize multiple charts side-by-side in a dashboard. In this chapter, we will learn how to plot multiple lines, create grids of charts, and directly visualize Pandas DataFrames.

---

## Key Concepts

### Multiple Lines & Legends
To plot multiple trends on the same grid, call `plt.plot()` repeatedly. Add `label="name"` inside each call, then call `plt.legend()` to display the key describing which line belongs to which series.

### Creating Subplots
Use `plt.subplot(rows, columns, active_index)` to build a grid of charts in a single figure window.
- **`rows`**: Number of rows in the subplot grid.
- **`columns`**: Number of columns in the subplot grid.
- **`active_index`**: The grid position (1-indexed, starting from top-left) where the next plot commands will be drawn.
- Use `plt.tight_layout()` to automatically clean up margins and prevent title overlap.

### Plotting with Pandas DataFrames
You can pass Pandas DataFrame columns (Series) directly into Matplotlib functions: `plt.plot(df["x_col"], df["y_col"])`.

---

## Examples

### Example 1: Multiple Lines with a Legend
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="Square", color='blue', marker='o')
plt.plot(x, y2, label="Linear", color='red', marker='s')

plt.title("Multiple Lines")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
```

### Example 2: Subplots Grid Layout
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

# Setup a grid with 1 row, 2 columns, and select the first panel
plt.subplot(1, 2, 1)
plt.plot(x, y1, color='blue')
plt.title("First Plot")

# Select the second panel in the 1x2 grid
plt.subplot(1, 2, 2)
plt.plot(x, y2, color='red')
plt.title("Second Plot")

# Optimize layout spacing
plt.tight_layout()
plt.show()
```

### Example 3: Plotting directly from a Pandas DataFrame
```python
import pandas as pd
import matplotlib.pyplot as plt

sales_data = {
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "sales": [1000, 1500, 1800, 2200]
}
sales_df = pd.DataFrame(sales_data)

# Pass DataFrame columns directly to matplotlib
plt.plot(sales_df["month"], sales_df["sales"], marker='o', color='purple')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()
```

---

## Notes

- Call `plt.subplot()` before applying any title, label, or plot commands, as those commands will only apply to the currently selected active panel.
- Slices in subplots start at index 1 (not 0). E.g. `plt.subplot(2, 2, 1)` to `plt.subplot(2, 2, 4)`.

---

## Summary

- Plot multiple traces on a single grid by calling `plt.plot()` sequentially and invoking `plt.legend()`.
- Divide a figure into a grid using `plt.subplot(rows, cols, active_index)`.
- Pass Pandas columns directly to Matplotlib plotting commands.

---

## Practice Exercises

1. Create a single plot containing three lines: `y = x`, `y = x**2`, and `y = x**3` for `x = [1, 2, 3, 4]`. Give each line a label, a different color, and show the legend.
2. Build a 2x1 vertical grid of subplots:
   - Upper panel: Bar chart showing course enrollments (Python: 120, SQL: 70).
   - Lower panel: Line plot of the same enrollment numbers.
   Use `tight_layout()` and add sub-titles to both.
3. Load a dictionary containing weekly hours worked by two employees:
   - Week: Week 1, Week 2, Week 3, Week 4
   - Employee A: 40, 42, 38, 40
   - Employee B: 35, 36, 40, 42
   Convert it to a DataFrame and plot both lines on the same Matplotlib chart directly from the DataFrame.

---

## Further Reading

- [Matplotlib Multiple Plots](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)
- [matplotlib.pyplot.subplot API](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
