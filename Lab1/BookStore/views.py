from django.http import HttpResponse
from django.shortcuts import redirect, render


Data = [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'description': 'The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink',
        'price': 7.99,
        'rating': 5,
    },
    {
        'id': 2,
        'title': 'The Da Vinci Code',
        'author': 'Dan Brown',
        'description': 'The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink',
        'price': 8.99,
        'rating': 2,
    },
    {
        'id': 3,
        'title': 'Java Script',
        'author': 'Ahmed Kamal',
        'description': 'The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink',
        'price': 8.99,
        'rating': 4,
    },
    {
        'id': 4,
        'title': 'HTML5',
        'author': 'Ali Ibrahim',
        'description': 'The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink',
        'price': 3.7,
        'rating': 2,
    },
    {
        'id': 5,
        'title': 'Angular JS',
        'author': 'Sara Karim',
        'description': 'The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink',
        'price': 10,
        'rating': 3.5,
    },
    {
        'id': 6,
        'title': 'PHP',
        'author': 'Osama Ahmed',
        'description': 'The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted "gin was the national drink',
        'price': 12,
        'rating': 4.5,
    },
]


def allBooks(request):
    myContext = {
        'books': Data
    }
    return render(request, 'store/book.html', context=myContext)

def get_book(id):
    for book in Data:
        if "id" in book and book.get("id") == id:
            print(book)
            return book
    return None


def bookDetails(request, *args, **kwrgs):
    id = kwrgs.get("book_id")
    book = get_book(id)
    myContext = {
        "details": book
    }
    return render(request, "store/bookDetails.html", context=myContext)


def delete_book(request, *args, **kwrgs):
    id = kwrgs.get("book_id")
    book = get_book(id)
    if book:
        Data.remove(book)
        return redirect('BookStore:index')
    else:
        return HttpResponse("Book not found.")
        
def update_book_data( request, *args, **kwrgs):
    id = kwrgs.get("book_id")
    book = get_book(id)
    if book:
        myContext = {
            "book": book
        }
        return render(request, "store/edit.html", context=myContext)
    else:
        return HttpResponse("Book not found.")
    
def update_book_post(request, *args, **kwrgs):
    id = kwrgs.get("book_id")
    book = get_book(id)
    # print(request.Post)
    if book:
        book['title'] = request.POST.get('title')
        book['author'] = request.POST.get('author')
        book['description'] = request.POST.get('description')
        book['price'] = request.POST.get('price')
        book['rating'] = request.POST.get('rating')
        return redirect('BookStore:index')
    else:
        return HttpResponse("Book not found.")
    
def add_book(request):
    if request.method == "POST":
        book = {
            'id': len(Data) + 1,
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'description': request.POST.get('description'),
            'price': request.POST.get('price'),
            'rating': request.POST.get('rating'),
        }
        Data.append(book)
        return redirect('BookStore:index')
    return render(request, "store/create.html")
    

