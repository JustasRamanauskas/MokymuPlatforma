from django.shortcuts import render

# Create your views here.
from mokymu_platforma.core.models import User


def registracija(request):
    if request.method == "POST":
        user = User()
        user.name = request.POST['inputName']
        user.surname = request.POST['inputSurname']
        user.login_name = request.POST['inputLoginName']
        user.login_password = request.POST['inputPassword']
        user.save()
        return render(request, "index.html")
    return render(request, "registracija.html")

def login(request):

    return render(request, "login.html")

def password(request):
    return render(request, "password.html")

def index(request):
    return render(request, "index.html")