# Pagination, Filtering, and Ordering

**Course:** Automation using Python — Part 1  
**Module 19:** Building Web Apps with Django

---

## Learning Objectives

By the end of this chapter, you will be able to:
- Explain the performance benefits of paginating API responses.
- Implement DRF's `PageNumberPagination` inside class-based views.
- Sort database querysets using Django's `.order_by()` ORM methods.
- Retrieve URL query parameters to apply dynamic filtering and sorting rules.

---

## Introduction

As your automation database grows, querying records becomes slower. Returning thousands of rows in a single HTTP response wastes server memory and network bandwidth. 

To build professional, high-performance APIs, you must implement:
1. **Pagination**: Breaking a large list of results down into smaller, page-sized chunks (e.g., 20 results per page).
2. **Ordering**: Letting the client sort the results by specific fields (e.g. sorting sales by price or newest date).
3. **Filtering**: Allowing clients to restrict results based on parameters (e.g., category or name).

In this chapter, you will learn how to add these capabilities to your DRF views.

---

## Key Concepts

### Database Pagination in DRF

DRF provides built-in pagination helper classes. The most common is **`PageNumberPagination`**, which uses a `?page=X` query parameter. 

To use pagination inside a basic `APIView`, you must manually initialize the pagination class, paginate the queryset, and return a paginated response wrapper using the helper method `get_paginated_response()`.

### Queryset Ordering

In Django's ORM, you sort records using the `.order_by()` method:
- `Sale.objects.all().order_by('sale_date')` - Sorts by sale date in **ascending** order.
- `Sale.objects.all().order_by('-sale_date')` - Sorts by sale date in **descending** order (prefixed with `-`).
- `Sale.objects.all().order_by('-price', 'product_name')` - Sorts by price descending, then alphabetically by name.

### Dynamic Filtering and Parameter Retrieval

You can inspect URL query parameters using `request.query_params` (which is DRF's equivalent of Flask's `request.args`). 

For example, if a client calls `/api/sales/?category=Electronics&ordering=-price`:
- `request.query_params.get('category')` resolves to `"Electronics"`.
- `request.query_params.get('ordering')` resolves to `"-price"`.

---

## Examples

### Example 1: Creating a Custom Pagination Class

Create a custom class to define the page size rules. Open `reports/pagination.py`:

```python
# reports/pagination.py
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    default_limit = 10  # Default number of items per page
    page_size = 5       # Default page size
    page_size_query_param = 'page_size'  # Let client specify page size (e.g. ?page_size=20)
    max_page_size = 100                  # Max page limit a client can request
```

### Example 2: Integrating Pagination, Ordering, and Filtering in APIView

Update `SaleListAPIView` inside `reports/views.py` to support filtering, sorting, and pagination:

```python
# reports/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sale
from .serializers import SaleSerializer
from .pagination import StandardResultsSetPagination

class SaleListAPIView(APIView):
    def get(self, request):
        # 1. Start with base queryset
        queryset = Sale.objects.all()

        # 2. Apply Filtering based on query parameter (?category=Electronics)
        category_filter = request.query_params.get("category")
        if category_filter:
            queryset = queryset.filter(category__iexact=category_filter)

        # 3. Apply Ordering based on parameter (?ordering=-price)
        # Default to sorting by sale_date descending if parameter is missing
        ordering = request.query_params.get("ordering", "-sale_date")
        
        # Enforce allowed fields for ordering to prevent SQL errors
        allowed_ordering_fields = ["price", "-price", "sale_date", "-sale_date", "quantity", "-quantity"]
        if ordering in allowed_ordering_fields:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by("-sale_date")

        # 4. Apply Pagination
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(queryset, request, view=self)
        
        if page is not None:
            serializer = SaleSerializer(page, many=True)
            # Returns a wrapper dict containing 'count', 'next', 'previous', and 'results'
            return paginator.get_paginated_response(serializer.data)

        # Fallback if pagination is disabled or fails
        serializer = SaleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Example 3: Verifying the API Output

If you start your server and call `GET http://127.0.0.1:8000/api/sales/?category=Electronics&ordering=-price&page=1`, the response JSON is automatically structured as follows:

```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "product_name": "Laptop",
            "quantity": 2,
            "price": 999.99,
            "sale_date": "2026-06-01",
            "category": "Electronics"
        },
        {
            "id": 4,
            "product_name": "Keyboard",
            "quantity": 3,
            "price": 49.99,
            "sale_date": "2026-06-04",
            "category": "Electronics"
        },
        {
            "id": 2,
            "product_name": "Mouse",
            "quantity": 5,
            "price": 24.99,
            "sale_date": "2026-06-02",
            "category": "Electronics"
        }
    ]
}
```

---

## Notes

- **UnorderedObjectListWarning**: If you apply pagination to a queryset without calling `.order_by()`, Django will issue a warning in the terminal. Without sorting, database rows can load in arbitrary order, causing duplicate or skipped items across page queries.
- **Lazy Evaluation**: Remember that Django querysets are lazy. Writing `queryset = queryset.filter(...)` or `queryset = queryset.order_by(...)` does not query the database immediately. The SQL query is only built and executed when the paginator evaluates the list.

---

## Summary

- Use pagination to split data payloads, improving server latency and response size.
- Implement DRF's `PageNumberPagination` by paginating the queryset and returning `get_paginated_response()`.
- Use `.order_by()` to sort records. Prefix fields with `-` for descending order.
- Inspect incoming query parameters via `request.query_params` to build dynamic SQL filters.

---

## Practice Exercises

1. Update the ordering rules in Example 2 to allow sorting alphabetically by product name (`product_name` and `-product_name`).
2. Write a custom pagination class named `TinyPagination` that sets a default page size of 2.
3. Apply `TinyPagination` to your active endpoints. Visit `/api/sales/?page=2` to verify that you receive records 3 and 4 of your inventory list.

---

## Further Reading

- [Django Rest Framework: Pagination](https://www.django-rest-framework.org/api-guide/pagination/)
- [Django QuerySet Reference: order_by](https://docs.djangoproject.com/en/stable/ref/models/querysets/#order-by)
- [Django QuerySet Reference: filter](https://docs.djangoproject.com/en/stable/ref/models/querysets/#filter)
