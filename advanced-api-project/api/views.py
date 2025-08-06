from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# For retrieving all books.
class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# For retrieving a single book by ID.
class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

# For adding a new book.
class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# For modifying an existing book.
class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# For removing a book.
class DeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer