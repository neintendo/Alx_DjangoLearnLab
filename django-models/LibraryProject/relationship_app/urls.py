from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views
from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard

urlpatterns = [
    path('books/', list_books, name = 'list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('librarian/dashboard/', librarian_dashboard, name='librarian-dashboard'),
    path('member/dashboard/', member_dashboard, name='member-dashboard'),
]
