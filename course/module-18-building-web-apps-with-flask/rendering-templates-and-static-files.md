# Rendering Templates and Static Files

**Course:** Automation using Python — Part 1  
**Module 18:** Building Web Apps with Flask

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Render separate HTML documents using the `render_template` function.
- Inject dynamic Python variables and objects into your web pages.
- Use Jinja2 control structures (loops, conditionals) inside HTML templates.
- Link and serve static assets (such as CSS stylesheets, JavaScript files, and images).

---

## Introduction

Returning hardcoded HTML strings directly from your Python route functions quickly becomes messy and unmaintainable. To separate presentation from logic, Flask utilizes a template engine called **Jinja2**. This allows you to write standard HTML documents containing dynamic placeholders that Flask populates before sending the final page to the user's browser.

---

## Key Concepts

### Directory Structure

Flask expects a specific folder layout by default:
- **`templates/`**: This directory contains all your HTML files (e.g., `index.html`).
- **`static/`**: This directory contains your static client-side files, such as CSS, client-side JavaScript, and images.

```text
my_flask_project/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── images/
        └── logo.png
```

### Jinja2 Syntax

Jinja2 templates use specific delimiters to distinguish normal HTML text from template commands:
1. **`{{ expression }}`**: Variable placeholders. Used to print variables, object properties, or dictionary values directly onto the page.
2. **`{% block %}`**: Control flow statements. Used to declare loops (`for`), conditional blocks (`if`), or inheritance blocks.
3. **`{# comment #}`**: Template comments. These comments are stripped out and are not sent to the client's browser.

### Serving Static Files

To link a stylesheet or script, you should not hardcode the file path. Instead, use Flask's **`url_for`** utility function, which dynamically generates correct URLs for routes and static assets.

Example syntax in HTML:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

---

## Examples

### Example 1: Basic Template Rendering

First, create a template file under `templates/welcome.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Template</title>
</head>
<body>
    <h1>Welcome, {{ user_name }}!</h1>
    <p>Today is {{ day }}. Enjoy learning Flask!</p>
</body>
</html>
```

Next, write the Python logic in `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/welcome/<name>")
def welcome(name):
    # Pass variables as keyword arguments to render_template
    return render_template("welcome.html", user_name=name, day="Friday")
```

### Example 2: Loops and Conditionals in Jinja2

Create `templates/products.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>Available Products</h1>
    <ul>
        {% for product in product_list %}
            <li>
                <strong>{{ product.name }}</strong> - ${{ product.price }}
                {% if product.stock > 0 %}
                    <span style="color: green;">(In Stock: {{ product.stock }})</span>
                {% else %}
                    <span style="color: red;">(Out of Stock)</span>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

Python logic in `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/products")
def list_products():
    products = [
        {"name": "Laptop", "price": 999.99, "stock": 5},
        {"name": "Mouse", "price": 24.99, "stock": 0},
        {"name": "Keyboard", "price": 49.99, "stock": 12}
    ]
    return render_template("products.html", product_list=products)
```

### Example 3: Adding Static Stylesheet

Create a stylesheet under `static/style.css`:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f6f9;
    padding: 20px;
}
h1 {
    color: #1e3a8a;
}
```

Reference it in your HTML page (`templates/products.html`):

```html
<head>
    <title>Product List</title>
    <!-- Use url_for to dynamically build path to static folder -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
```

---

## Notes

- **XSS Protection**: Jinja2 automatically escapes variables before displaying them (e.g. converting `<` to `&lt;`). This prevents Cross-Site Scripting (XSS) attacks by default. If you need to render raw HTML code, you must explicitly mark it as safe using the `|safe` filter: `{{ my_html_string | safe }}`.
- **Auto-Reloading Templates**: By default, Flask caches templates. When running in debug mode (`debug=True`), the cache is bypassed, ensuring you see changes immediately after saving template files without needing to restart the server.

---

## Summary

- Store HTML files in the `templates/` folder and assets in the `static/` folder.
- Use `render_template("filename.html", **context)` to return formatted pages.
- Jinja2 expressions (`{{ ... }}`) render data; statements (`{% ... %}`) execute control logic.
- Use `url_for('static', filename='...')` to reference assets safely.

---

## Practice Exercises

1. Build a Flask route `/dashboard` that passes a dictionary of statistics (e.g., `{'users': 150, 'sales': 1200, 'errors': 3}`) to a template and displays them in an HTML table.
2. In the template from Exercise 1, use an `if` condition to apply a red class style to the error value if the number of errors is greater than 0.
3. Write a Flask route that passes a list of 5 computer server names. Display them inside an ordered list (`<ol>`) using a Jinja2 `for` loop, and load a custom logo image from the `static/` folder at the top of the page.

---

## Further Reading

- [Flask Templates Guide](https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates)
- [Jinja Template Designer Documentation](https://jinja.palletsprojects.com/en/stable/templates/)
