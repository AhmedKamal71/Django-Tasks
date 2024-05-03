from os import name
from django.urls import path
from BookStore import views

app_name = "BookStore" # Alias Name For URL

urlpatterns = [
    path('', views.allBooks, name='index'),
    path('details/<int:book_id>', views.bookDetails, name = "details"),
    path('delete/<int:book_id>', views.delete_book, name = "delete"),
    path('update/<int:book_id>', views.update_book_data, name = "update"),
    path('update/<int:book_id>/post', views.update_book_post, name = "update_post"),
    path('add/', views.add_book, name = "add"),
]