from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # Route for the ListView
    path('books/', ListView.as_view(), name = 'book-list'),

    # Route for the DetailView
    path('books/<int:pk>/detail/', DetailView.as_view(), name = 'book-detail'),

    # Route for the CreateView
    path('books/create/', CreateView.as_view(), name = 'book-create'),

    # Route for the UpdateView
    path('books/update/', UpdateView.as_view(), name = 'book-update'),

    # Route for the DestroyView
    path('books/delete/', DeleteView.as_view(), name = 'book-delete'),
]