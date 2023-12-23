# myapp/urls.py
from django.urls import path
from .views import read_operation, read_operation_with_primary_key, create_operation, update_operation, delete_operation

urlpatterns = [
    path('', read_operation, name='read_operation'),
    path('data/<int:pk>/', read_operation_with_primary_key, name='read_operation_with_primary_key'),
    path('data/new/', create_operation, name='create_operation'),
    path('data/<int:pk>/edit/', update_operation, name='update_operation'),
    path('data/<int:pk>/delete/', delete_operation, name='delete_operation'),
]
