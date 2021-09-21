from django.urls import path
from admins.views import layout,booksPage,bookDetailsPage,back_shelf,add_book,index,users,view_user,\
    BookCreate,BookDelete,BookUpdate,changePass,SearchResultsView

urlpatterns = [
    path('layout', layout),
    path('index', index, name="index"),
    path('books', booksPage, name="books"),
    path('bookDetails/<int:book_id>', bookDetailsPage, name="bookDetails"),
    path('back_shelf/<int:book_id>', back_shelf, name="back_shelf"),
    path('add_book/<int:book_id>', add_book, name="add_book"),
    path('users', users, name="users"),
    path('view_user', view_user, name="view_user"),
    path('changePass', changePass, name="changePass"),
    path('book/create/', BookCreate, name='book_create'),
    path('book/<int:pk>/update/', BookUpdate, name='BookUpdate'),
    path('book/<int:pk>/delete/', BookDelete, name='book_delete'),
    path('search/', SearchResultsView.as_view(), name='search_results')


]
