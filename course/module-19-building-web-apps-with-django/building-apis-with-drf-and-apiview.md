# Building APIs with DRF and APIView

**Course:** Automation using Python — Part 1  
**Module 19:** Building Web Apps with Django

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Install and configure Django Rest Framework (DRF) inside a project.
- Write Serializer classes to handle validation and model-to-JSON serialization.
- Implement REST API endpoints for GET, POST, PUT, and DELETE actions using `APIView`.
- Set up URL patterns for class-based views.

---

## Introduction

While Flask uses the simple `jsonify()` helper to convert dictionary objects into JSON, Django has a more structured approach. To construct professional REST APIs, Django developers use the **Django Rest Framework (DRF)**.

DRF provides powerful tools, including:
1. **Serializers**: Classes that validate incoming input data and convert complex Django model objects into standard JSON arrays/objects.
2. **APIView**: A class-based view system that handles different HTTP verbs (GET, POST, etc.) inside structured class methods.

---

## Key Concepts

### Installing DRF

Install `djangorestframework` inside your virtual environment:
```bash
pip install djangorestframework
```

Add `'rest_framework'` to the list of `INSTALLED_APPS` inside `settings.py`:
```python
# myproject/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'reports',
]
```

### Serializers

Serializers are similar to Django models, but instead of mapping to database tables, they map tables to JSON structures. They handle both:
- **Serialization**: Converting a database query or model instance to a Python dictionary that can easily be sent as JSON.
- **Deserialization**: Validating incoming JSON data (e.g. from a POST request) and saving it back to a database model.

### APIView

Unlike function-based views where you use `if request.method == 'POST'`, `APIView` lets you write clean Python classes with methods named after HTTP verbs:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPI(APIView):
    def get(self, request):
        return Response({"message": "GET request received"})

    def post(self, request):
        return Response({"message": "POST request received"})
```

---

## Examples

### Example 1: Creating a Serializer

Create a new file `reports/serializers.py`:

```python
# reports/serializers.py
from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        # List the fields you want to expose in your JSON API
        fields = ['id', 'product_name', 'quantity', 'price', 'sale_date', 'category']
```

### Example 2: Implementing APIView CRUD

Open `reports/views.py` and implement the class-based views:

```python
# reports/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sale
from .serializers import SaleSerializer

# Handler for /api/sales/ (Get list, Create items)
class SaleListAPIView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        # many=True tells the serializer we are passing a list of objects
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Pass request body data to the serializer
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Inserts the record into the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Handler for /api/sales/<int:pk>/ (Get single item, Update item, Delete item)
class SaleDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return None

    def get(self, request, pk):
        sale = self.get_object(pk)
        if not sale:
            return Response({"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SaleSerializer(sale)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        sale = self.get_object(pk)
        if not sale:
            return Response({"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
        # Pass instance AND data to update it
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sale = self.get_object(pk)
        if not sale:
            return Response({"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
        sale.delete()
        return Response({"message": "Sale deleted successfully"}, status=status.HTTP_200_OK)
```

### Example 3: Routing Class-Based Views

To register class-based views in `reports/urls.py`, you must call the `.as_view()` method:

```python
# reports/urls.py
from django.urls import path
from .views import SaleListAPIView, SaleDetailAPIView

urlpatterns = [
    # Class-based views must use .as_view()
    path("api/sales/", SaleListAPIView.as_view(), name="sales-list"),
    path("api/sales/<int:pk>/", SaleDetailAPIView.as_view(), name="sales-detail"),
]
```

---

## Notes

- **Primary Key (`pk`)**: Django uses `pk` (primary key) by convention in URL routing and object retrievals to refer to the primary key column (which is typically `id`).
- **DRF Request & Response**: DRF request objects are different from Django's default HttpRequest. You access JSON request data directly via `request.data` (which handles parsing JSON automatically), instead of calling `request.get_json()`.

---

## Summary

- DRF is a powerful toolkit for building Web APIs in Django.
- ModelSerializers automatically create validation and mapping configurations based on your Model fields.
- `APIView` organizes CRUD endpoints using class methods named after HTTP verbs (get, post, put, delete).
- Access parsed JSON request bodies using `request.data` and return responses with the DRF `Response` object.

---

## Practice Exercises

1. Create a `Serializer` class for the `Analyst` model.
2. Build an `AnalystListAPIView` class that supports listing and creating Analysts. Ensure that it returns correct status codes on success and validation failure.
3. Configure your app-level URLs to routing `/api/analysts/` to your `AnalystListAPIView` endpoint.

---

## Further Reading

- [Django Rest Framework: Serializers](https://www.django-rest-framework.org/api-guide/serializers/)
- [Django Rest Framework: Class-based Views](https://www.django-rest-framework.org/api-guide/views/#class-based-views)
- [DRF Status Codes Reference](https://www.django-rest-framework.org/api-guide/status-codes/)
