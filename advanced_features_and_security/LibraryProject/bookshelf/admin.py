from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('custom_field1', 'custom_field2')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('custom_field1', 'custom_field2')}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

class ModelAdmin(admin.ModelAdmin):
    admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Book, BookAdmin)
