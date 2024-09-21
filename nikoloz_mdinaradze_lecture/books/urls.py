from django.urls import path

from books import views

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='books-create'),
    path('', views.BookListView.as_view(), name='books-list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='books-detail'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='books-update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='books-delete'),
]
