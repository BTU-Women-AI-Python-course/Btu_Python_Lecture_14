from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from books.models import Book


# Create your views here.
class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = "books/books_create.html"
    success_url = reverse_lazy("books-list")


class BookListView(ListView):
    model = Book
    template_name = "books/books_list.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/books_detail.html"
    context_object_name = "book"


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "books/books_update.html"
    success_url = reverse_lazy("books-list")
    context_object_name = "book"


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("books-list")
    context_object_name = "book"
    template_name = "books/books_delete.html"
