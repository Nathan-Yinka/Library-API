from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    # URL patterns for categories
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),  # List and create categories
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),  # Retrieve, update, or delete a specific category
    # URL patterns for books
    path('books/', BookListCreate.as_view(), name='book-list-create'),  # List and create books
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),  # Retrieve, update, or delete a specific book
]
