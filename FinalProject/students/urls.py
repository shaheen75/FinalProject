from django.urls import path
from students.views import layout

urlpatterns = [
    path('layout', layout),
]
