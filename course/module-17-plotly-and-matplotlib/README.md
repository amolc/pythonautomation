# Module 17: Plotly and Matplotlib

**Automation using Python — Part 1**

In this module, you will learn the art of data visualization in Python. We will explore **Matplotlib** for static plotting, subplots, and publication-ready charts, and **Plotly** for interactive, dashboard-friendly, and 3D visual representations.

---

## Learning Outcomes

By the end of this module, you will be able to:
- Generate and customize line, bar, pie, histogram, and scatter plots in Matplotlib.
- Control axes labels, titles, grids, legends, and line styling in Matplotlib.
- Arrange multiple charts in grid layouts using subplots.
- Plot data directly from Pandas DataFrames.
- Create interactive web-ready plots using Plotly Express.
- Construct complex multi-trace charts using Plotly Graph Objects.
- Set up dashboard layouts and export interactive diagrams to standalone HTML documents.

---

## Prerequisites

- Python 3.9 or newer installed.
- Required packages: `matplotlib`, `plotly`, `pandas`, `numpy`.
- Set up and install in your virtual environment:
  ```bash
  pip install matplotlib plotly pandas numpy
  ```

---

## Chapters

| # | Chapter | Topics |
|---|---------|--------|
| 1 | [Introduction to Matplotlib and Line Charts](./introduction-to-matplotlib-and-line-charts.md) | Initializing Matplotlib, writing line charts, configuring titles, grids, legends, markers, and saving plots |
| 2 | [Matplotlib Basic Chart Types](./matplotlib-basic-chart-types.md) | Constructing bar charts, horizontal bar charts, pie charts, histograms, and scatter plots |
| 3 | [Matplotlib Subplots and Pandas Integration](./matplotlib-subplots-and-pandas-integration.md) | Overlaying multiple traces, arranging multi-chart layouts (`subplot`), and integration with Pandas |
| 4 | [Introduction to Plotly and Basic Charts](./introduction-to-plotly-and-basic-charts.md) | Interactive visualization benefits, using Plotly Express to write interactive line, scatter, bar, and pie charts |
| 5 | [Plotly Histograms, Box Plots, and 3D Charts](./plotly-histograms-boxplots-and-3d-charts.md) | Visualizing distributions with box plots and histograms, and creating 3D scatter plots |
| 6 | [Plotly Graph Objects, Layouts, and Dashboards](./plotly-graph-objects-layouts-and-dashboards.md) | Advanced tracing with Graph Objects, making interactive dashboard subplots, and exporting charts to HTML |

---

## Module Capstone Exercise

Build a standalone script `visualization_capstone.py` that accomplishes the following:

1. Create a dictionary or load a dataset representing product sales:
   - Month: Jan, Feb, Mar, Apr, May, Jun
   - Electronics Sales: 15000, 18000, 16500, 22000, 19000, 24000
   - Clothing Sales: 10000, 12000, 11500, 15000, 14000, 16000
2. Load this data into a Pandas DataFrame.
3. Using **Matplotlib**:
   - Create a single figure containing a line plot of both Electronics and Clothing sales across the months.
   - Use distinct markers, line styles, a legend, a grid, and titles.
   - Save the plot as `monthly_sales_comparison.png`.
4. Using **Plotly Express**:
   - Create an interactive grouped bar chart comparing Electronics and Clothing sales by month.
   - Configure hover information to show the values clearly.
   - Save this interactive chart as a standalone webpage named `interactive_sales.html` using `fig.write_html()`.
