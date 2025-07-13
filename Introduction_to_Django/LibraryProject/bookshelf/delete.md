from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
print("Book deleted successfully.")

# (1, {'myapp.Book': 1})
# Book deleted successfully.
