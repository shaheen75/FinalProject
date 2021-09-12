from django.urls import path
from students.views import layout, loginPage, signPage, homePage, profile, dashboardPage

urlpatterns = [
    path('layout', layout),
    path('login', loginPage, name="login"),
    path('sign_up', signPage, name="sign_up"),
    path('home', homePage, name="home"),
    path('profile', profile, name="profile"),
    path('dashboard/<Users_id>', dashboardPage, name="dashboard"),
]
