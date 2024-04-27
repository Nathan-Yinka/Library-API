from rest_framework import serializers
from .models import Category, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Serialize all fields of the Category model

class BookSerializer(serializers.ModelSerializer):
    # Serialize the Book model
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=True)  # Use PrimaryKeyRelatedField for the category field

    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of the Book model
        
    def to_representation(self, instance):
        # Convert the representation of the instance
        representation = super().to_representation(instance)
        # If the category is None, represent it as "None"
        if representation['category'] is None:
            representation['category'] = "None"
        return representation
