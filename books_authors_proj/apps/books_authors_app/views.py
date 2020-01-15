from django.shortcuts import render, redirect
from .models import Book
from .models import Author

def index(request):
    context = {
      "all_books": Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def authors(request):
    context = {
      "all_authors": Author.objects.all()
    }
    return render(request, 'books_authors_app/authors.html', context)

def view_book(request, book_id):
    context = {
      "book": Book.objects.get(id=book_id),
      "all_authors": Author.objects.all()
    }
    return render(request, 'books_authors_app/viewbook.html', context)

def view_author(request, author_id):
    context = {
      "author": Author.objects.get(id=author_id)
    }
    return render(request, 'books_authors_app/viewauthor.html', context)

def add_book(request):
    print(request.POST['bookTitle'])
    print(request.POST['bookDescription'])
    Book.objects.create(
        title=request.POST['bookTitle'], desc=request.POST['bookDescription'])
    return redirect('/')

def edit_book(request, book_id):
    context = {
      "book2edit": Book.objects.get(id=book_id)
    }
    return render(request, 'books_authors_app/editbook.html', context)

def update_book(request):
    request.POST['book2updateId']
    print(request.POST['book2updateId'])
    print(request.POST['bookTitle'])
    print(request.POST['bookDescription'])
    current_book = Book.objects.get(id=request.POST['book2updateId'])
    current_book.title = request.POST['bookTitle']
    current_book.desc = request.POST['bookDescription']
    current_book.save()
    return redirect('/')

def delete_book(request, book_id):
    deleted_book = Book.objects.get(id=book_id)
    deleted_book.delete()
    return redirect('/')

def add_author_to_book(request):
    print("this is the book's id " + request.POST["book_id"])
    bookId = request.POST["book_id"]
    book_added = Book.objects.get(id=request.POST["book_id"])
    print("this is the author's id " + request.POST["selected_author_id"])
    current_author = Author.objects.get(id=request.POST["selected_author_id"])
    current_author.books.add(book_added)
    return redirect(f'/books/{bookId}')
