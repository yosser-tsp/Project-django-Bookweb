
from django.db import models

# Model for Author
class Author(models.Model):
    name = models.CharField(max_length=255)
    age=models.IntegerField()

    def __str__(self):
        return self.name

# Model for Book
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title

# Model for Review
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    mail=models.CharField(max_length=255)

    def __str__(self):
        return f"Review of {self.book.title}"


