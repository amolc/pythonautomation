# CSV Import and Database CRUD

**Course:** Automation using Python — Part 1  
**Module 19:** Building Web Apps with Django

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Define database structures by writing Django Model classes.
- Generate and apply SQL database migrations.
- Parse CSV files with Pandas and insert them into the database using Django's ORM.
- Perform standard Create, Read, Update, and Delete (CRUD) operations via the Django ORM.

---

## Introduction

Django features a built-in **Object-Relational Mapper (ORM)**. The ORM allows you to define database tables as standard Python classes (called **Models**) and run SQL queries using Python syntax, without writing raw SQL.

In this chapter, you will learn how to define a model, run migrations, and write a Python automation script that loads a CSV file into Pandas, cleans it, and bulk-inserts the rows directly into your Django database using the ORM.

---

## Key Concepts

### Defining Django Models

A model represents a single table in your database. Each property in the class represents a column. Models are declared in `models.py` and inherit from `django.db.models.Model`.

Common Django field types:
- `CharField`: For short text fields (requires `max_length`).
- `IntegerField` / `FloatField`: For numerical values.
- `DateField` / `DateTimeField`: For date/time values.
- `TextField`: For large, multi-line text blocks.

### The Migration Lifecycle

Whenever you create or edit a model class, you must synchronize the database structure:
1. **`python manage.py makemigrations`**: Scans `models.py` and creates a recipe file (in python) detailing the database changes.
2. **`python manage.py migrate`**: Executes those recipe files, running SQL commands (`CREATE TABLE`, `ALTER TABLE`) against the SQLite database.

### Bulk Data Ingestion

While you can insert rows one-by-one using `Model.objects.create()`, this is slow for large datasets because it makes a database network roundtrip for every row. 

Instead, you can load your CSV using Pandas, build a list of Django Model instances, and insert them in a single query using **`bulk_create()`**.

---

## Examples

### Example 1: Defining a Model

Open `reports/models.py` and write:

```python
# reports/models.py
from django.db import models

class Sale(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    sale_date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_name} ({self.quantity} sold)"
```

Create and run the database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Example 2: Importing CSV into the Model

Create a sample CSV `sales_data.csv` in your project folder:
```csv
Product,Qty,Price,Date,Category
Laptop,2,999.99,2026-06-01,Electronics
Mouse,5,24.99,2026-06-02,Electronics
Chair,1,149.99,2026-06-03,Furniture
Keyboard,3,49.99,2026-06-04,Electronics
```

To run a script that imports this data, we can write a custom Django management script. Create a file named `import_sales.py` in your project folder:

```python
# import_sales.py
import os
import django
import pandas as pd

# 1. Setup Django environment settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Import the model AFTER setting up Django
from reports.models import Sale

def run_import():
    csv_file = "sales_data.csv"
    if not os.path.exists(csv_file):
        print("CSV file not found!")
        return

    # 2. Read CSV with Pandas
    df = pd.read_csv(csv_file)
    
    # Clean up column names and fill missing data if any
    df['Qty'] = df['Qty'].fillna(0).astype(int)
    df['Price'] = df['Price'].fillna(0.0).astype(float)
    
    sales_to_create = []
    
    # 3. Iterate through DataFrame rows
    for index, row in df.iterrows():
        # Build Sale model instances
        sale = Sale(
            product_name=row['Product'],
            quantity=row['Qty'],
            price=row['Price'],
            sale_date=row['Date'],
            category=row['Category']
        )
        sales_to_create.append(sale)
        
    # 4. Bulk insert into the database
    Sale.objects.bulk_create(sales_to_create)
    print(f"Successfully imported {len(sales_to_create)} sales records into SQLite!")

if __name__ == "__main__":
    run_import()
```

Run the script from your terminal:
```bash
python import_sales.py
```

### Example 3: Querying the Database (CRUD)

Once data is imported, you can perform query operations:

```python
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from reports.models import Sale

# 1. Create a single sale
new_sale = Sale.objects.create(
    product_name="USB Hub", quantity=10, price=19.99, sale_date="2026-06-05", category="Electronics"
)

# 2. Read (Querying)
all_sales = Sale.objects.all()
electronics = Sale.objects.filter(category="Electronics")
expensive = Sale.objects.filter(price__gt=100.0) # price > 100.0

# 3. Update
sale_item = Sale.objects.get(id=1)
sale_item.price = 949.99  # discount
sale_item.save()

# 4. Delete
old_sale = Sale.objects.get(product_name="Chair")
old_sale.delete()
```

---

## Notes

- **`django.setup()`**: If you run a standalone Python script outside of `manage.py`, you must call `django.setup()` and define the environment variable `DJANGO_SETTINGS_MODULE` first. Otherwise, Django will raise an `AppRegistryNotReady` error because it does not know where your configuration files are.
- **Double Underscore Lookups**: Django ORM uses double underscores (`__`) for filtering conditions (e.g. `price__gt=100` means price greater than, `product_name__contains="Mouse"` means containing substring).

---

## Summary

- Django Models map Python classes directly to database tables.
- Generate migration scripts with `makemigrations` and execute them with `migrate`.
- Use Pandas to read and clean CSV data, then use `bulk_create` to insert data efficiently.
- Perform database tasks using the ORM: `create()`, `all()`, `filter()`, `get()`, `save()`, and `delete()`.

---

## Practice Exercises

1. Create a model in `reports/models.py` named `Analyst` containing fields `name` (Char), `department` (Char), and `active` (Boolean). Run the migrations.
2. Write a Python script to insert three Analysts into the database.
3. Write an ORM query to retrieve and print the names of all active Analysts.

---

## Further Reading

- [Django Official Documentation: Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django ORM Making Queries](https://docs.djangoproject.com/en/stable/topics/db/queries/)
- [Pandas DataFrame Iteration Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)
