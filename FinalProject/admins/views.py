from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Book
from django.contrib import messages

# Create your views here.

def layout(request):
    return render(request,'app.html')


def booksPage(request):
    if request.method == "POST":
        book_id = request.POST.get("book_pk")
        book = Book.objects.get(id=book_id)
        request.user.profile.books.add(book)
        messages.success(request, (f'{book} add to booklist.'))
        messages.success(request, (f'{book} returned at 'f'{book.return_date}.'))
        return redirect('dashboard')
    books = Book.objects.all()
    paginator = Paginator(books, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="books.html", context={"page_obj": page_obj})


def bookDetailsPage(request,book_id):
    books = Book.objects.filter(id=book_id)
    context = {'bookDetailsPage': books}
    return render(request, 'bookDetails.html',context)


def back_shelf(request,book_id):
    if request.method == "GET":
        book = Book.objects.get(id=book_id)
        request.user.profile.books.remove(book)
        messages.success(request, (f'{book} delete from booklist.'))
        return redirect('dashboard')

