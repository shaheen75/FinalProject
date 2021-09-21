from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db.models import Q
from .forms import *
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.

def index(request):
    books = Book.objects.all()
    if not request.user.is_superuser:
        messages.info(request, 'You should be login as Admin to enter Admin Dashboard')
        return redirect('login')
    else:
        return render(request, 'index.html', context={"books": books})


def layout(request):
    return render(request, 'app.html')


def booksPage(request):
    books = Book.objects.all()
    paginator = Paginator(books, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="books.html", context={"page_obj": page_obj})


def bookDetailsPage(request, book_id):
    books = Book.objects.filter(id=book_id)
    context = {'bookDetailsPage': books}
    return render(request, 'bookDetails.html', context)


def back_shelf(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "GET":
        request.user.profile.books.remove(book)
        messages.success(request, (f'{book} delete from booklist.'))
        return redirect('dashboard')


def add_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "GET":
        request.user.profile.books.add(book)
        messages.success(request, (f'{book} add to booklist.'))
        return redirect('dashboard')


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', context={"users": users})


def view_user(request):
    users = User.objects.all()
    return render(request, 'viewuser.html', context={"users": users})


def BookCreate(request):
    if not request.user.is_superuser:
        return redirect('login')
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request=request, template_name="editbook.html", context={"editbook_form": form})


def BookUpdate(request, pk):
    if not request.user.is_superuser:
        return redirect('login')
    obj = Book.objects.get(id=pk)
    form = BookForm(instance=obj)
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect(index)
    return render(request, 'editbook.html', context={"editbook_form": form})


def BookDelete(request, pk):
    if not request.user.is_superuser:
        return redirect('login')
    obj = get_object_or_404(Book, pk=pk)
    obj.delete()
    return redirect('index')


def changePass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changePass')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


class SearchResultsView(ListView):
    model = User
    template_name = 'search_results.html'
    queryset = User.objects.filter(id__icontains='')

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(
            Q(id__icontains=query)
        )
        return object_list