from django.contrib import admin
from .models import Livre

from .models import Book, Author, Book_Author

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Book_Author)
