from django.urls import path;
from Book import views;
from os import name;

app_name = "Book"

urlpatterns = [
    path('', views.all_books, name='index'),
    path('details/<int:book_id>', views.book_details, name = "details"),
    path('delete/<int:book_id>', views.delete_book, name = "delete"),
    path('add/', views.add_book, name = "add"),
    path('update/<int:book_id>', views.update_book_data, name = "update"),
]
