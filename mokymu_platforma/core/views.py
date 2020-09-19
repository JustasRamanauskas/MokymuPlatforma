from django.shortcuts import render
from mokymu_platforma.core.models import User
from mokymu_platforma.core.models import Roles
from django.contrib.auth import authenticate

def registracija(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['inputName'], email=request.POST['inputLoginName'], password=request.POST['inputPassword'] )
        user.first_name = request.POST['inputName']
        user.last_name = request.POST['inputSurname']
        user.save()

        role = Roles()
        role.role_type = request.POST["inputRole"]
        role.user_id_id = user.id
        role.save()

        return render(request, "index.html")
    return render(request, "registracija.html")

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['inputEmailAddress'], password=request.POST['inputPassword'])
        if user is not None:
            return render(request, "index.html")
        else:
            return render(request, "login.html", context=({'errors':"Bad login information"}))
    return render(request, "login.html",context=({'errors':''}))

def password(request):
    return render(request, "password.html")

def index(request):
    return render(request, "index.html")