from django.views.generic import ListView
from .models import *
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

