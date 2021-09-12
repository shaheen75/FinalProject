from django.urls import path
from admins.views import layout,booksPage,bookDetailsPage

urlpatterns = [
    path('layout', layout),
    path('books', booksPage, name="books"),
    path('bookDetails/<book_id>', bookDetailsPage, name="bookDetails"),
]
