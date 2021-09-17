from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, UserForm, ProfileForm

# Create your views here.

def layout(request):
    return render(request, 'app.html')


def homePage(request):
    return render(request, 'home.html')


def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')


def signPage(request):
    form = UserCreationForm
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            user = regform.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="sign_up.html", context={"register_form": form})


def editprofile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect("dashboard")
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your Booklist was successfully updated!'))
        else:
            messages.error(request, ('Unable to complete request'))
        return redirect("dashboard")
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', context={"user": request.user, "user_form": user_form, "profile_form": profile_form})


def dashboardPage(request):
    return render(request=request, template_name="dashboard.html")