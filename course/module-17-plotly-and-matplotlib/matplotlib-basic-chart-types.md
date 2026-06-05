# Matplotlib Basic Chart Types

**Course:** Automation using Python — Part 1  
**Module 17:** Plotly and Matplotlib

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Construct vertical and horizontal bar charts in Matplotlib.
- Create pie charts with customized labels and percentage layouts.
- Generate histograms to represent frequency distributions.
- Create scatter plots to observe relationship patterns between variables.

---

## Introduction

Line charts are ideal for displaying values over continuous intervals or time, but different datasets call for different visualizations. In this chapter, we will look at how to represent categories with bar and pie charts, frequencies with histograms, and individual data point coordinates with scatter plots.

---

## Key Concepts

### Bar Charts
Bar charts are used to compare values across different categories.
- Vertical bar chart: `plt.bar(categories, values)`
- Horizontal bar chart: `plt.barh(categories, values)`

### Pie Charts
Pie charts display proportional shares of categories in a circular layout.
- Syntax: `plt.pie(values, labels=labels, autopct='%1.1f%%')`
- The `autopct` parameter formats the percentage label on each slice (e.g. `'%1.1f%%'` displays one decimal place).

### Histograms
Histograms represent frequency distributions of numeric values by dividing data into intervals ("bins").
- Syntax: `plt.hist(data, bins=n)`

### Scatter Plots
Scatter plots show individual points mapped on Cartesian coordinates, revealing correlation trends.
- Syntax: `plt.scatter(x, y)`

---

## Examples

### Example 1: Vertical Bar Chart
```python
import matplotlib.pyplot as plt

students = ["Amol", "Snehal", "Rahul", "Priya"]
marks = [85, 92, 78, 88]

plt.bar(students, marks, color='skyblue')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
```

### Example 2: Horizontal Bar Chart
```python
import matplotlib.pyplot as plt

courses = ["Python", "Java", "SQL", "AI"]
students = [120, 90, 70, 150]

plt.barh(courses, students, color='salmon')
plt.title("Course Enrollments")
plt.xlabel("Students Enrolled")
plt.ylabel("Courses")
plt.show()
```

### Example 3: Pie Chart
```python
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++", "AI"]
values = [40, 25, 15, 20]

plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightcoral', 'lightgreen'])
plt.title("Programming Language Usage")
plt.show()
```

### Example 4: Histogram
```python
import matplotlib.pyplot as plt

# Student marks dataset
marks = [55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Marks Ranges")
plt.ylabel("Frequency")
plt.show()
```

### Example 5: Scatter Plot
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

plt.scatter(x, y, color='red', marker='x')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

---

## Notes

- For bar charts, you can pass custom colors as a list to color each bar uniquely.
- Make sure to add `edgecolor='black'` to histograms to distinguish the boundaries of adjacent bins clearly.

---

## Summary

- Use `plt.bar()` and `plt.barh()` for categorical comparisons.
- Draw fractional share layouts using `plt.pie(..., autopct)`.
- Bin numeric arrays into distribution frequencies using `plt.hist()`.
- Display point relationships using `plt.scatter()`.

---

## Practice Exercises

1. Create a Matplotlib bar chart showing the population of 4 cities: Delhi (30M), Mumbai (20M), Bangalore (12M), Pune (7M). Label axes appropriately.
2. Create a pie chart showing a student's daily time distribution: Study (40%), Sleep (30%), Entertainment (15%), Others (15%). Include labels and percentage annotations.
3. Generate a scatter plot of study hours vs exam scores using the data:
   - Study Hours: `[2, 4, 5, 7, 8]`
   - Exam Scores: `[55, 70, 75, 90, 95]`
   Add labels and a title.

---

## Further Reading

- [Matplotlib Bar Chart guide](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
- [Matplotlib Pie Chart guide](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)
- [Matplotlib Histograms](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
