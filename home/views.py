from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def personal_page(request):
    return render(request, 'home/index.html')