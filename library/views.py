from rest_framework import generics
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    """
    API view for listing and creating categories.
    """
    queryset = Category.objects.all()  # Queryset to retrieve all categories
    serializer_class = CategorySerializer  # Serializer class for categories

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific category.
    """
    queryset = Category.objects.all()  # Queryset to retrieve all categories
    serializer_class = CategorySerializer  # Serializer class for categories

class BookListCreate(generics.ListCreateAPIView):
    """
    API view for listing and creating books.
    """
    queryset = Book.objects.all()  # Queryset to retrieve all books
    serializer_class = BookSerializer  # Serializer class for books

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific book.
    """
    queryset = Book.objects.all()  # Queryset to retrieve all books
    serializer_class = BookSerializer  # Serializer class for books
