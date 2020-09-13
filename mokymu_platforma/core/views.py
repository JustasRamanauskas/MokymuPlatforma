from django.shortcuts import render

# Create your views here.
from mokymu_platforma.core.models import User


def registracija(request):
    if request.method == "POST":
        user = User()
        user.login_name = request.POST['inputEmailAddress']
        if request.POST['inputPassword'] == request.POST['inputPassword2']:
            user.login_password = request.POST['inputEmailAddress']

    return render(request, "registracija.html")

def login(request):
    return render(request, "login.html")

def password(request):
    return render(request, "password.html")

def index(request):
    return render(request, "index.html")