from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Name of the category
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the category was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the category was last updated

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('updated_at', 'created_at')  # Order categories by their last update time
        indexes = [
            models.Index(fields=['name']),  # Index for faster lookup by name
        ]
        verbose_name_plural = "Categories"  # Plural name for the Category model in admin interface
        

class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    author = models.CharField(max_length=100)  # Author of the book
    no_of_pages = models.IntegerField()  # Number of pages in the book
    description = models.TextField()  # Description of the book
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # Category the book belongs to
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the book was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the book was last updated

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('updated_at', 'created_at')  # Order books by their last update time
        indexes = [
            models.Index(fields=['category','title']),  # Index for faster lookup by category and title
        ]
