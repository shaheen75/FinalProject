from django.urls import path
from admins.views import layout

urlpatterns = [
    path('layout', layout),
]
