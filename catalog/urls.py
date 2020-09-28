from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="book"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("book/create/", views.BookCreate.as_view(), name="book_create"),
    path("authors/", views.AuthorListView.as_view(), name="author"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    path("author/create/", views.AuthorCreate.as_view(), name="author_create"),
    path("author/<int:pk>/update/", views.AuthorUpdate.as_view(), name="author_update"),
    path("author/<int:pk>/delete/", views.AuthorDelete.as_view(), name="author_delete"),
    path("mybooks/", views.LoanedBooksByUserListView.as_view(), name="my-borrowed"),
    path("allbooks/", views.LoanedBooksAllView.as_view(), name="all-borrowed"),
    path("book/<uuid:pk>/renew/", views.renew_book_librarian, name="renew-book-librarian"),
]

