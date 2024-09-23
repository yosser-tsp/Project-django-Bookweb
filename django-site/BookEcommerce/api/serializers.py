# api/serializers.py

from rest_framework import serializers
from .models import Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested Author details
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested Reviews

    class Meta:
        model = Book
        fields = '__all__'
