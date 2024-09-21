from django.http import HttpResponse
from django.shortcuts import render

from books.forms import BookForm


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
