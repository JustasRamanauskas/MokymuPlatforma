from django.shortcuts import render, redirect
from mokymu_platforma.core.models import User, Roles
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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

        return redirect(login_view)
    return render(request, "registracija.html")

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['inputEmailAddress'], password=request.POST['inputPassword'])
        if user is not None:
            print(f"login autorizavosi {user.first_name}")
            login(request, user)
            return redirect(index)
        else:
            return render(request, "login.html", context=({'errors':"Bad login information!!"}))
    return render(request, "login.html",context=({'errors':''}))

def logout_view(request):
    logout(request)
    return redirect(login_view)

def password(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['inputEmailAddress'])
        if user is not None:
            send_mail(
                'New password',
                'Your new passwod is blabalbal',
                'from@mail.com',
                'inputEmailAddress'
            )
    return render(request, "password.html")

@login_required(login_url='/')
def index(request):
    vartotojas = User.objects.get(username=request.user.first_name)
    roles = Roles.objects.filter(user_id=vartotojas.id)
    return render(request, "index.html", context={'auth_user' : request.user, 'core_roles' : roles})

@login_required(login_url='/')
def settings(request):
    return render(request, "settings.html")