from django.urls import path
from students.views import layout, loginPage,user_logout, signPage, homePage, editprofile, dashboardPage

urlpatterns = [
    path('', homePage, name="home"),
    path('layout', layout),
    path('login', loginPage, name="login"),
    path('logout', user_logout, name="logout"),
    path('sign_up', signPage, name="sign_up"),
    path('dashboard', dashboardPage, name="dashboard"),
    path('editprofile', editprofile, name="editprofile"),
]
