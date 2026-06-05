# Displaying Graphs in Templates

**Course:** Automation using Python — Part 1  
**Module 19:** Building Web Apps with Django

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Run database aggregation and grouping queries using Django's ORM.
- Format database results into arrays compatible with JavaScript charts.
- Render dynamic graphs (such as Bar and Line charts) in templates using **Chart.js**.
- Pass data lists safely to the frontend without character escaping issues.

---

## Introduction

Data ingestion and API construction are major parts of automation. However, managers and operators often need a clean visual representation of the metrics. Rather than logging stats or exporting raw Excel sheets, you can build a reporting web page.

In this chapter, you will learn how to write Django queries that calculate aggregates (such as summing total sales by category), pass these numbers to a Django template, and render beautiful, interactive canvas charts using Chart.js.

---

## Key Concepts

### ORM Aggregation and Grouping

To calculate summary statistics in Django, you import aggregate functions (`Sum`, `Count`, `Avg`, `Max`) from `django.db.models`.

To group data (similar to a SQL `GROUP BY`), you combine the `.values()` and `.annotate()` methods:
```python
from django.db.models import Sum
from reports.models import Sale

# Calculate sum of 'price * quantity' (or sum of quantity) grouped by category
stats = Sale.objects.values('category').annotate(total_qty=Sum('quantity'))
```
This returns a list of dictionaries, such as:
`[{'category': 'Electronics', 'total_qty': 10}, {'category': 'Furniture', 'total_qty': 1}]`

### Rendering Charts with Chart.js

**Chart.js** is a lightweight, open-source JavaScript library that renders charts inside HTML5 `<canvas>` tags. You do not need to install it via pip or npm; you can load it directly into your HTML page from a Content Delivery Network (CDN) script link:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

### Passing Python Lists to JavaScript

When passing lists of strings (e.g. `['Electronics', 'Furniture']`) from a Django view into JavaScript, the Django template engine will automatically escape characters like single quotes into HTML entities (e.g. `&#x27;`). 

To prevent this escaping and allow JavaScript to parse the array correctly, use Django's **`|safe`** filter:
```javascript
const categories = {{ categories_list|safe }};
```

---

## Examples

### Example 1: The Aggregation View

Open `reports/views.py` and write the dashboard logic:

```python
# reports/views.py
from django.shortcuts import render
from django.db.models import Sum
from .models import Sale
import json

def dashboard_view(request):
    # 1. Query sum of quantities sold, grouped by category
    category_data = Sale.objects.values('category').annotate(total_sold=Sum('quantity'))
    
    # 2. Separate query results into two parallel lists for Chart.js
    categories = []
    quantities = []
    
    for entry in category_data:
        categories.append(entry['category'])
        quantities.append(entry['total_sold'])
        
    # Convert lists to JSON strings to ensure safe formatting in JS
    context = {
        "categories_js": json.dumps(categories),
        "quantities_js": json.dumps(quantities),
        "total_sales_count": Sale.objects.count()
    }
    
    return render(request, "reports/dashboard.html", context)
```

Bind this view inside `reports/urls.py`:
```python
# reports/urls.py
path("dashboard/", views.dashboard_view, name="dashboard"),
```

### Example 2: The HTML Template with Chart.js

Create a new file `reports/templates/reports/dashboard.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Reports Dashboard</title>
    <!-- 1. Load Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f1f5f9;
            margin: 30px;
        }
        .container {
            max-width: 800px;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }
        h1 {
            color: #1e3a8a;
        }
        .chart-box {
            margin-top: 20px;
            position: relative;
            height: 400px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Sales Analytics</h1>
    <p>Total transaction items: <strong>{{ total_sales_count }}</strong></p>
    
    <!-- 2. Create canvas element for the chart -->
    <div class="chart-box">
        <canvas id="salesChart"></canvas>
    </div>
</div>

<script>
    // 3. Retrieve variables passed from Django view (using |safe filter)
    const chartLabels = {{ categories_js|safe }};
    const chartDataValues = {{ quantities_js|safe }};

    // 4. Configure and render Chart.js
    const ctx = document.getElementById('salesChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartLabels,
            datasets: [{
                label: 'Total Quantity Sold',
                data: chartDataValues,
                backgroundColor: [
                    'rgba(59, 130, 246, 0.7)',  // blue
                    'rgba(245, 158, 11, 0.7)',  // amber
                    'rgba(16, 185, 129, 0.7)',  // emerald
                    'rgba(239, 68, 68, 0.7)'    // red
                ],
                borderColor: [
                    'rgb(59, 130, 246)',
                    'rgb(245, 158, 11)',
                    'rgb(16, 185, 129)',
                    'rgb(239, 68, 68)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>

</body>
</html>
```

Start the Django server (`python manage.py runserver`) and open `http://127.0.0.1:8000/dashboard/`. You will see a beautiful bar chart displaying your aggregated sales statistics!

---

## Notes

- **`json.dumps()`**: Converting lists to JSON strings in Python using `json.dumps()` is safer than sending a raw list. It ensures brackets, quotes, and strings are correctly encoded for Javascript parser compatibility.
- **Canvas Size**: Always wrap the Chart.js `<canvas>` element in a parent `<div>` with specified width and height. Chart.js requires this wrapper container to correctly calculate scales when performing responsive screen resizing.

---

## Summary

- Import database aggregates (like `Sum` or `Count`) from `django.db.models` to summarize record numbers.
- Group rows using `.values('group_field').annotate(summary_name=Sum('sum_field'))`.
- Use a Chart.js script CDN link to build frontend canvas charts without packages.
- Apply the `|safe` filter to variables passed to Javascript to avoid string formatting encoding issues.

---

## Practice Exercises

1. Modify the `dashboard_view` in `reports/views.py` to calculate the total sales income (`quantity * price`) per category. Expose this list to Javascript.
2. Add a second chart canvas container in your dashboard template and render a Pie Chart showing the distribution of total sales value.
3. Write a query to get sales quantities grouped by date, and plot this as a Line Chart to see the timeline progression of sales volumes.

---

## Further Reading

- [Django DB Aggregation Documentation](https://docs.djangoproject.com/en/stable/topics/db/aggregation/)
- [Chart.js Official Getting Started Guide](https://www.chartjs.org/docs/latest/getting-started/)
