from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def layout(request):
    return render(request,'app.html')

def homePage(request):
    return render(request,'home.html')

def booksPage(request):
    return render(request,'books.html')

def loginPage(request):
    return render(request,'login.html')

def signPage(request):
    return render(request,'sign_up.html')