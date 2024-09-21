from django.urls import path

from books import views

urlpatterns = [
    path('create/', views.creat_book, name='books-create'),
    path('', views.list_books, name='books-list'),
]
