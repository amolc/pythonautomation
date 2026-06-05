# Designing Views, Routing, and Templates

**Course:** Automation using Python — Part 1  
**Module 19:** Building Web Apps with Django

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Write function-based views to process requests and return HTTP responses.
- Set up a clean, modular routing architecture using project and app-level `urls.py` files.
- Create and render HTML templates using the Django Template Language (DTL).
- Configure static directories and load client-side stylesheets in your templates.

---

## Introduction

In Flask, routing is defined directly above functions using decorators. Django, however, enforces a clean separation of concerns: URLs are declared in dedicated routing modules (`urls.py`), logic is written in view modules (`views.py`), and presentation is stored in template files.

In this chapter, you will learn how to connect these pieces together to serve dynamic HTML pages styled with static CSS files.

---

## Key Concepts

### Function-Based Views (FBVs)

A Django view is a Python function that takes an `HttpRequest` object as its first argument and returns an `HttpResponse` object. The response can be raw text, a redirect, a JSON payload, or rendered HTML.

### Modular Routing with `urls.py`

Django maps URLs using the `path()` function. For clean organization, you should split your routing:
1. **Project-level `urls.py`**: Handles global paths and forwards specific sub-paths to their respective apps using the `include()` helper.
2. **App-level `urls.py`**: Manages the paths specific to that application.

### Templates and Namespace Isolation

Django templates are HTML files that utilize DTL (Django Template Language). 

By default, Django scans the `templates/` folder of all registered apps. To prevent multiple apps from having templates with the same name (e.g. `index.html`), Django best practice is to place templates inside an app-specific subfolder:
`reports/templates/reports/dashboard.html`

### Django Template Language (DTL)

Like Jinja2, DTL uses double braces and percent brackets:
- `{{ user_name }}` - Variable placeholder.
- `{% for sale in sales_list %}` - Control blocks.
- `{% load static %}` - Special Django tag used to enable loading files from static folders.

---

## Examples

### Example 1: Creating a View and App-level URLs

First, create a view in `reports/views.py`:

```python
# reports/views.py
from django.http import HttpResponse

def hello_report(request):
    return HttpResponse("Welcome to the Reports App!")
```

Next, create a routing file `reports/urls.py` inside the app folder:

```python
# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Match empty path (relative to the app namespace)
    path("", views.hello_report, name="hello_report"),
]
```

### Example 2: Forwarding from Project URLs

To connect the app routing to the main project, edit `myproject/urls.py`:

```python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include all paths from the reports app under the root URL
    path('', include('reports.urls')),
]
```

Run `python manage.py runserver`. When you visit `http://127.0.0.1:8000/`, your view will run and show `"Welcome to the Reports App!"`.

### Example 3: Rendering a Template and Serving Stylesheets

Let's render a page. Create a template file under:
`reports/templates/reports/home.html`

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Reports Dashboard</title>
    <!-- Use static template tag to generate the stylesheet path -->
    <link rel="stylesheet" href="{% static 'reports/style.css' %}">
</head>
<body>
    <h1>Report Overview</h1>
    <p>Logged in as: <strong>{{ analyst_name }}</strong></p>
</body>
</html>
```

Create a stylesheet under `reports/static/reports/style.css`:

```css
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f8fafc;
    padding: 30px;
}
h1 {
    color: #1e293b;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 8px;
}
```

Update your view in `reports/views.py` to render the template:

```python
# reports/views.py
from django.shortcuts import render

def home_view(request):
    context = {"analyst_name": "Amol Chawathe"}
    # render() automatically looks inside 'templates/' folders
    return render(request, "reports/home.html", context)
```

Finally, bind this view to a path in `reports/urls.py`:
```python
# reports/urls.py
path("home/", views.home_view, name="home"),
```

Visit `http://127.0.0.1:8000/home/` to see your styled page.

---

## Notes

- **URL Trailing Slashes**: By default, Django enforces trailing slashes on URL patterns (e.g. `path('home/', ...)`). If a user visits `/home`, Django will automatically issue a 301 Redirect to `/home/`.
- **Static files configuration**: During local development (`DEBUG = True`), Django automatically serves files inside any app's `static/` folder. For production, Django uses a command called `python manage.py collectstatic` to gather all static files into a single folder for high-performance serving by web servers (like Nginx).

---

## Summary

- Django views receive an `HttpRequest` and return an `HttpResponse`.
- Use `include()` in project-level `urls.py` to route requests to app-level `urls.py` files.
- Place HTML files inside `templates/<app_name>/` and reference them using `render(request, "app_name/file.html", context)`.
- Serve assets from `static/<app_name>/` and link them using `{% load static %}` and `{% static 'path' %}`.

---

## Practice Exercises

1. Add a dynamic route to `reports/urls.py` that captures a string parameter `category`: `path('category/<str:category>/', views.category_view, name='category')`.
2. Write the view `category_view` in `reports/views.py` to output: `"Displaying records for category: [category_name]"`.
3. Create a template `reports/detail.html` that renders a dictionary representing a report (containing `title`, `created_date`, and `row_count`). Style this template using a dedicated CSS stylesheet inside your static directory.

---

## Further Reading

- [Django Official Documentation: URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Official Documentation: Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Templates Introduction](https://docs.djangoproject.com/en/stable/topics/templates/)
