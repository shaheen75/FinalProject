from django.shortcuts import render, redirect, get_object_or_404
from admins.models import Book
# Create your views here.
def layout(request):
    return render(request,'app.html')

def booksPage(request):
    books = Book.objects.all()
    context = {'booksPage': books}
    return render(request, 'books.html', context)

def bookDetailsPage(request,book_id):
    books = Book.objects.filter(id=book_id)
    context = {'bookDetailsPage': books}
    return render(request, 'bookDetails.html',context)