from atexit import register
import re
from django.contrib import admin
from Book.models import Book

admin.site.register(Book)

# Register your models here.