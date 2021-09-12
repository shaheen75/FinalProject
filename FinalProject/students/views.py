from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from students.models import Users

# Create your views here.

def layout(request):
    return render(request, 'app.html')

def homePage(request):
    return render(request, 'home.html')

def loginPage(request):
    if request.method == 'POST':
       Email = request.POST.get('Email')
       password = request.POST.get('password')
       try:
           # User_obj = Users.objects.filter(id=users_id)
           user = Users.objects.get(Email=Email, password=password)
           if user is not None:
               return render(request, 'dashboard.html', {'dashboardPage': User_obj})
           else:
               print("Email or Password is wrong ,Please try again")
       except Exception as identifier:
           return redirect('login')
    return render(request, 'login.html')

def signPage(request):
    if request.POST:
        usr = Users()
        usr.UserName = request.POST["UserName"]
        usr.Email = request.POST["Email"]
        usr.password = request.POST["password"]
        usr.confirm_password = request.POST["password"]
        usr.city = request.POST["city"]
        usr.save()
        return redirect("profile")
    return render(request, 'sign_up.html')

def profile(request):
    user = Users.objects.all()
    context = {'profile': user}
    return render(request, 'profile.html', context)

def dashboardPage(request,Users_id):
    user = Users.objects.filter(id=Users_id)
    context = {'dashboardPage': user}
    return render(request, 'dashboard.html', context)

