# Introduction to Django and Setup

**Course:** Automation using Python — Part 1  
**Module 19:** Building Web Apps with Django

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Explain Django's "batteries-included" philosophy and MVT architecture.
- Initialize a Django project and create individual application components.
- Outline the purpose of key configuration files (`settings.py`, `urls.py`, `manage.py`).
- Run initial database migrations and start the Django development server.

---

## Introduction

In the previous module, you learned how to use Flask, a microframework that provides minimal structure, letting you choose your own tools. While this is great for simple APIs, larger enterprise applications often benefit from a **batteries-included** framework.

**Django** is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It comes pre-packaged with built-in tools for database management, an admin dashboard, user authentication, security controls, and URL routing. This makes Django highly productive for larger automation systems that require robust user management, reporting, and database storage.

---

## Key Concepts

### MVT (Model-View-Template) Architecture

Unlike the classic MVC (Model-View-Controller) design, Django uses the **MVT** pattern:
1. **Model (M)**: The data access layer. It defines your database structure using Python classes (ORM) and handles database transactions.
2. **View (V)**: The business logic layer. It receives HTTP requests, interacts with models to fetch/save data, and decides what response to return (e.g. rendering a template or returning JSON).
3. **Template (T)**: The presentation layer. It contains HTML and Django Template Language (DTL) tags to generate dynamic web pages.

### Django Project vs. Django App

A key design aspect of Django is separating code into projects and apps:
- **Project**: The overall web configuration and collection of apps. A project contains settings, database connection details, and global URL routings.
- **App (Application)**: A self-contained web package that performs a specific function (e.g., a blog, a user auth system, a CSV parser). A single Django project can contain multiple apps.

---

## Examples

### Example 1: Installing and Initializing a Project

To set up Django, first activate your virtual environment, then run the following commands:

```bash
# Install Django via pip
pip install django

# Create a project folder named 'myproject'
django-admin startproject myproject

# Move inside the project folder
cd myproject

# Create a self-contained app named 'reports'
python manage.py startapp reports
```

### Example 2: Project Layout

After running the commands, Django builds the following directory structure:

```text
myproject/
│
├── manage.py                # Command-line utility to interact with the project
│
├── myproject/               # Project configuration directory
│   ├── __init__.py
│   ├── settings.py          # Project settings and configurations
│   ├── urls.py              # Main URL routing declarations
│   └── wsgi.py / asgi.py    # Deployment entry points
│
└── reports/                 # Your custom application folder
    ├── __init__.py
    ├── admin.py             # Admin panel configurations
    ├── apps.py              # App config metadata
    ├── models.py            # Database tables defined as Python classes
    ├── tests.py             # Testing scripts
    └── views.py             # Route controller logic
```

### Example 3: Configuring Settings and Running migrations

Before running Django, you must register your app in `myproject/settings.py` so Django knows it exists. 

Open `myproject/settings.py` and add `'reports'` to the `INSTALLED_APPS` list:

```python
# myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Register your custom app here
    'reports',
]
```

Next, run the initial database migrations to configure Django's built-in tables (such as admin accounts and user authentication), and start the server:

```bash
# 1. Apply initial database structures to SQLite database (db.sqlite3)
python manage.py migrate

# 2. Start the development server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser. You will see Django's default welcome page confirming the installation succeeded!

---

## Notes

- **Default Database**: By default, Django is pre-configured to use SQLite (a local file named `db.sqlite3` created inside your project root). You can easily change this to PostgreSQL, MySQL, or Oracle by modifying the `DATABASES` dictionary in `settings.py`.
- **Port adjustments**: If port 8000 is occupied, you can start the server on a different port by appending it to the run command: `python manage.py runserver 8080`.

---

## Summary

- Django is a full-featured web framework using Model-View-Template (MVT) architecture.
- Projects contain global settings and URLs; Apps contain modular, feature-specific code.
- Add your app to `INSTALLED_APPS` inside `settings.py` to register it.
- Run migrations using `python manage.py migrate` and start the server with `python manage.py runserver`.

---

## Practice Exercises

1. Initialize a Django project named `company_portal` and create an application within it named `inventory`.
2. Add your `inventory` app to the list of `INSTALLED_APPS` inside the `settings.py` of `company_portal`.
3. Apply the initial migrations to the SQLite database and start the development server on port `9000`.

---

## Further Reading

- [Django Official Documentation: First Steps](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Settings Reference](https://docs.djangoproject.com/en/stable/ref/settings/)
