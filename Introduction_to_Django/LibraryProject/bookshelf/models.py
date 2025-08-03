from django.db import models

class Book(models.Model):
    """Model representing a book model"""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField