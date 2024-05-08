from venv import create
from django.db import models

from Book import views


class Book(models.Model):
    title = models.CharField("Book Title",max_length=50)
    description = models.TextField("Book Description", max_length=500)
    rate = models.PositiveBigIntegerField("Book Rate")
    views = models.PositiveBigIntegerField("Book Views")
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    def __str__(self):
        return self.title

