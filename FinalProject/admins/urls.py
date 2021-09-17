from django.urls import path
from admins.views import layout,booksPage,bookDetailsPage,back_shelf

urlpatterns = [
    path('layout', layout),
    path('books', booksPage, name="books"),
    path('bookDetails/<int:book_id>', bookDetailsPage, name="bookDetails"),
    path('back_shelf/<int:book_id>', back_shelf, name="back_shelf"),
]
