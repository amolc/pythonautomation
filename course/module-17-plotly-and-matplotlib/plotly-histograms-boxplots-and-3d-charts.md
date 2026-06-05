# Plotly Histograms, Box Plots, and 3D Charts

**Course:** Automation using Python — Part 1  
**Module 17:** Plotly and Matplotlib

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Construct interactive histograms to observe dataset frequencies.
- Create box plots (`px.box`) to analyze data ranges, quartiles, and outliers.
- Render interactive 3D scatter plots to visualize relationships between three variables.

---

## Introduction

Beyond line and bar charts, data analysts rely on distributions and multi-dimensional analysis. In this chapter, we will learn how to build interactive histograms and box plots to see how values are distributed, and how to rotate, zoom, and inspect data points in a 3D coordinate space.

---

## Key Concepts

### Histograms
Like Matplotlib's static histograms, Plotly's `px.histogram()` groups continuous numbers into bins, but adds interactive hover counts.

### Box Plots
Box plots represent numerical distributions by highlighting the minimum, first quartile (Q1), median, third quartile (Q3), maximum, and any statistical outliers.
- Syntax: `px.box(df, y="numeric_column")`
- Hovering over a Plotly box plot reveals the exact quartile and median values.

### 3D Scatter Plots
To analyze three numeric variables simultaneously, we can map points in a 3-dimensional space.
- Syntax: `px.scatter_3d(df, x="col1", y="col2", z="col3", title="title")`
- Users can click and drag in the browser to rotate the 3D grid and observe points from different angles.

---

## Examples

### Example 1: Interactive Histogram
```python
import plotly.express as px
import pandas as pd

hist_df = pd.DataFrame({
    "marks": [55, 60, 70, 75, 80, 85, 90, 95]
})

fig = px.histogram(hist_df, x="marks", nbins=5, title="Marks Distribution")
fig.show()
```

### Example 2: Interactive Box Plot
```python
import plotly.express as px
import pandas as pd

box_df = pd.DataFrame({
    "salary": [25000, 30000, 35000, 45000, 50000, 60000]
})

fig = px.box(box_df, y="salary", title="Salary Distribution")
fig.show()
```

### Example 3: 3D Scatter Plot
```python
import plotly.express as px
import pandas as pd

three_d_df = pd.DataFrame({
    "x": [1, 2, 3, 4],
    "y": [10, 20, 30, 40],
    "z": [5, 15, 25, 35]
})

fig = px.scatter_3d(three_d_df, x="x", y="y", z="z", title="3D Scatter Plot")
fig.show()
```

---

## Notes

- 3D plots require a GPU-enabled web browser to render smoothly.
- Box plots are extremely useful in automated data pipelines for identifying data entry errors and anomalies (outliers that fall outside the maximum/minimum range).

---

## Summary

- Display counts of range intervals interactively using `px.histogram()`.
- Unpack data quartiles, medians, and outliers using `px.box()`.
- Plot three coordinates in space using `px.scatter_3d()`, allowing complete browser rotation.

---

## Practice Exercises

1. Create a Plotly histogram representing the distribution of exam scores of a large class: `[62, 65, 78, 82, 85, 88, 92, 95, 98]`. Set the number of bins to 4.
2. Build a box plot of employee age data: `[22, 25, 28, 30, 32, 45, 52, 61, 80]`. Observe what is flagged as an outlier (if anything).
3. Create a 3D scatter plot showcasing real estate properties:
   - x: `Square Footage [1000, 1500, 2000, 2500]`
   - y: `Number of Bedrooms [2, 3, 3, 4]`
   - z: `Price in Thousands [150, 220, 310, 420]`

---

## Further Reading

- [Plotly Box Plots Guide](https://plotly.com/python/box-plots/)
- [Plotly Histograms Guide](https://plotly.com/python/histograms/)
- [Plotly 3D Scatter Plots](https://plotly.com/python/3d-scatter-plots/)
