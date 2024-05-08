from django import views
from django.shortcuts import render, redirect
from django.http import HttpResponse



def all_books(request):
    from Book.models import Book
    books = Book.objects.all()
    return render(request, 'book/allBooks.html', {'books': books})

def book_details(request, book_id):
    from Book.models import Book
    book = Book.objects.get(id=book_id)
    return render(request, "book/bookDetails.html", {'book': book})

def add_book(request):
    from Book.models import Book
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        rate = request.POST.get('rate')
        views = request.POST.get('views')
        book = Book(title=title, description=description, rate=rate, views=views)
        book.save()
        return redirect('Book:index')
    return render(request, 'book/addBook.html')


def delete_book(request, book_id):
    from Book.models import Book
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('Book:index')

def update_book_data(request, book_id):
    from Book.models import Book
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        rate = request.POST.get('rate')
        views = request.POST.get('views')
        book.title = title
        book.description = description
        book.rate = rate
        book.views = views
        book.save()
        return redirect('Book:index')
    return render(request, 'book/updateBook.html', {'book': book})


