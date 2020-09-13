from django.shortcuts import render

# Create your views here.
def registracija(request):
    return render(request, "registracija.html")

def login(request):
    return render(request, "login.html")

def password(request):
    return render(request, "password.html")

def index(request):
    return render(request, "index.html")