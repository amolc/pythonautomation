# Introduction to Matplotlib and Line Charts

**Course:** Automation using Python — Part 1  
**Module 17:** Plotly and Matplotlib

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Set up Matplotlib and understand its scripting interface (`pyplot`).
- Create simple line charts using `plt.plot()`.
- Customize chart aesthetics, including titles, axis labels, grids, markers, and line styles.
- Save charts to files on your system.

---

## Introduction

Visualizing data is essential for communicating insights and understanding trends. **Matplotlib** is the oldest and most widely used library for creating static, animated, and interactive visualizations in Python. In this chapter, we will learn how to create a basic line chart, format its styling, and write it to disk.

---

## Key Concepts

### Matplotlib Pyplot
The `matplotlib.pyplot` module is a collection of functions that make Matplotlib work like MATLAB. It provides simple commands to build figures, draw lines, add labels, and format layouts.

### Creating a Line Chart
The most fundamental plot is the line chart, created using `plt.plot(x, y)`.

### Customizing Line Plots
We can customize lines and markers to distinguish dataset trends:
- **`marker`**: Defines data points (e.g. `'o'` for circles, `'s'` for squares, `'^'` for triangles).
- **`linestyle`**: Defines the line drawing type (e.g. `'-'` for solid, `'--'` for dashed, `':'` for dotted).
- **`color`**: Sets line colors (e.g. `'blue'`, `'red'`, or hex codes).

### Annotations and Layouts
- `plt.title()`: Adds a main chart title.
- `plt.xlabel()` and `plt.ylabel()`: Add axis labels.
- `plt.grid(True)`: Toggles coordinate grid lines.
- `plt.legend()`: Shows a key explaining each plotted line (requires setting the `label` parameter inside `plt.plot()`).

### Saving Plots
Use `plt.savefig("filename.png")` to export your charts to disk.

---

## Examples

### Example 1: Your First Line Chart
```python
import matplotlib.pyplot as plt

# 1. Define data points
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# 2. Draw line
plt.plot(x, y)

# 3. Add titles and labels
plt.title("Simple Line Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# 4. Display chart
plt.show()
```

### Example 2: Customizing Line Charts
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

# Plot with circular markers and dashed line
plt.plot(x, y, marker='o', linestyle='--', color='green')

plt.title("Customized Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)

plt.show()
```

### Example 3: Saving Charts to Disk
```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y, marker='s')
plt.title("Save Example")

# Save as PNG image in current directory
plt.savefig("line_chart.png")
print("Chart Saved Successfully")
```

---

## Notes

- `plt.show()` opens a window displaying your plot and pauses script execution until the window is closed. In non-interactive environments (like automated scripts), you will usually bypass `plt.show()` and use `plt.savefig()` instead.
- If you call `plt.plot()` multiple times without resetting, Matplotlib will draw them on the same figure automatically.

---

## Summary

- Import the scripting interface using `import matplotlib.pyplot as plt`.
- Draw line plots using `plt.plot(x, y)`.
- Configure plots with `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, and `plt.grid()`.
- Export static files using `plt.savefig()`.

---

## Practice Exercises

1. Create a script that plots a line chart showing a company's profit over 5 years (Year 1 to Year 5). Add axis labels and a title.
2. Modify the line chart from Exercise 1 to use red square markers and a dotted line. Enable the grid lines.
3. Save the modified chart from Exercise 2 as `profit_report.png` and confirm that the image file is created in your workspace.

---

## Further Reading

- [Matplotlib Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [matplotlib.pyplot.plot API](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)
- [Saving Figures in Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)
