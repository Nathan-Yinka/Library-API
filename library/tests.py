from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category, Book

class CategoryBookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample category
        self.category = Category.objects.create(name='Test Category')

        # Create sample book
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            no_of_pages=100,
            description='Test description',
            category=self.category
        )

    def test_category_list(self):
        # Test if categories can be listed
        url = reverse('category-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one category was created initially

    def test_category_create(self):
        # Test if a new category can be created
        initial_category_count = Category.objects.count()
        new_category_data = {'name': 'New Test Category'}
        url = reverse('category-list-create')
        response = self.client.post(url, new_category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), initial_category_count + 1)

    def test_book_list(self):
        # Test if books can be listed
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one book was created initially

    def test_book_create(self):
        # Test if a new book can be created
        initial_book_count = Book.objects.count()
        new_book_data = {
            'title': 'New Test Book',
            'author': 'New Test Author',
            'no_of_pages': 200,
            'description': 'New test description',
            'category': self.category.pk
        }
        url = reverse('book-list-create')
        response = self.client.post(url, new_book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), initial_book_count + 1)

    def test_category_retrieve_update_destroy(self):
        # Test category retrieval, update, and deletion
        url = reverse('category-retrieve-update-destroy', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Category')

        updated_data = {'name': 'Updated Category'}
        response = self.client.put(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Category')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if associated books have their category field set to None
        books_with_deleted_category = Book.objects.filter(category=None)
        self.assertEqual(books_with_deleted_category.count(), 1)

    def test_book_retrieve_update_destroy(self):
        # Test book retrieval, update, and deletion
        url = reverse('book-retrieve-update-destroy', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

        updated_data = {'title': 'Updated Book'}
        response = self.client.patch(url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book')

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
