from django.shortcuts import render

# Create your views here.
def layout(request):
    return render(request,'app.html')