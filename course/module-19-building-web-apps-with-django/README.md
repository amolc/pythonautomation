# Module 19: Building Web Apps with Django

**Automation using Python — Part 1**

In this module, you will learn how to build full-featured web applications and REST APIs using Django, one of Python's most popular and powerful web frameworks. We will explore Django's model-view-template (MVT) architecture, learn to run local servers and database migrations, import tabular CSV data into databases using the Django ORM, build RESTful endpoints using Django Rest Framework (DRF) and `APIView`, implement query pagination and ordering, and create a dashboard containing dynamic data visualization graphs.

---

## Learning Outcomes

By the end of this module, you will be able to:
- Install Django and create project and application structures.
- Map routes, implement views, render templates, and serve static assets.
- Define models and use Django's ORM to perform migrations and CRUD transactions.
- Ingest CSV file data using Pandas and save it to a database using Django models.
- Install and configure Django Rest Framework (DRF) to serialize data to JSON.
- Implement GET, POST, PUT, and DELETE routes using DRF's `APIView`.
- Configure query pagination and result sorting in API querysets.
- Extract aggregate database numbers and display them in HTML charts using Chart.js.

---

## Prerequisites

- Python 3.9 or newer installed.
- Required packages: `django`, `djangorestframework`, `pandas`.
- Set up and install these dependencies in your virtual environment:
  ```bash
  pip install django djangorestframework pandas
  ```

---

## Chapters

| # | Chapter | Topics |
|---|---------|--------|
| 1 | [Introduction to Django and Setup](./introduction-to-django-and-setup.md) | What Django is, MVC/MVT, starting projects and apps, settings, running development server, database migrations |
| 2 | [Designing Views, Routing, and Templates](./designing-views-routing-and-templates.md) | Django URL mapping, function-based views, rendering HTML, passing context variables, serving static assets |
| 3 | [CSV Import and Database CRUD](./csv-import-and-database-crud.md) | Creating models, running makemigrations/migrate, loading CSVs with Pandas, bulk-saving records to SQL via ORM |
| 4 | [Building APIs with DRF and APIView](./building-apis-with-drf-and-apiview.md) | Django Rest Framework setup, JSON Serializers, implementing GET, POST, PUT, DELETE operations using `APIView` |
| 5 | [Pagination, Filtering, and Ordering](./pagination-filtering-and-ordering.md) | Configuring `PageNumberPagination`, sorting querysets with `order_by()`, exposing pagination parameters via API |
| 6 | [Displaying Graphs in Templates](./displaying-graphs-in-templates.md) | Fetching aggregated data stats, passing them to HTML templates, and rendering dynamic charts using Chart.js |

---

## Module Capstone Exercise

Build a standalone Django application named `sales_dashboard` containing a single app `reports` that implements the following requirements:

1. **Database Model**: Define a `Sale` model with fields: `product_name` (char), `quantity` (int), `price` (float), `sale_date` (date), and `category` (char).
2. **CSV Data Import Command**: Write a management command or Python script to read a local `sales_data.csv` file, parse it using Pandas, and populate the SQLite database.
3. **API View**:
   - Create a DRF `APIView` endpoint at `/api/sales/` that supports GET (returns paginated list of sales, ordered by `sale_date` or `price`) and POST (adds a sale).
4. **Visual Dashboard Template**:
   - Create a web route at `/dashboard/` that renders an HTML template.
   - Query the database to calculate total sales by `category` and by `month`.
   - Pass these aggregated statistics to the template and render a Bar Chart and a Line Chart using Chart.js.
