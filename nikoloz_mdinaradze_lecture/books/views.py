from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from books.forms import BookForm
from books.models import Book


# Create your views here.
def creat_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success !!!")
    else:
        form = BookForm()
        return render(request, "books/books_create.html", {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", {'books': books})


def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/books_detail.html", {'book': book})


def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse("Success !!!")
    else:
        form = BookForm(instance=book)
    return render(request, "books/books_update.html", {'form': form})

