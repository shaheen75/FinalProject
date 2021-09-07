from django.urls import path
from students.views import layout, booksPage, loginPage, signPage

urlpatterns = [
    path('layout', layout),
    path('books', booksPage, name="books"),
    path('login', loginPage, name="login"),
    path('sign_up', signPage, name="sign_up"),
]
