from lib2to3.pgen2.token import GREATER
from django.contrib import admin

from .models import Book, Genre


admin.site.register(Book)
admin.site.register(Genre)