import django_filters
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# For retrieving all books.
class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filters.OrderingFilter = ['title', 'author', 'publication_year']
    filters.SearchFilter = ['title', 'author', 'publication_year']

    def get_queryset(self):
        """ This view should return a list of all the purchases for the currently authenticated user."""
        user = self.request.user
        return Book.objects.filter()

# For retrieving a single book by ID.
class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'

# For adding a new book.
class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# For modifying an existing book.
class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# For removing a book.
class DeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]