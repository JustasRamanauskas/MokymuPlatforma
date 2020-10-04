from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from mokymu_platforma.core.models import User, Roles, Client, Company, Teacher, Course


def registracija(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['inputName'], email=request.POST['inputLoginName'],
                                        password=request.POST['inputPassword'])
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
            return render(request, "login.html", context=({'errors': "Bad login information!!"}))
    return render(request, "login.html", context=({'errors': ''}))


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
    plain_roles = [r.role_type for r in roles]
    client = Client.objects.filter(role_id=roles.first()).first()
    company = Company.objects.filter(roles_id=roles.first()).first()
    teacher = Teacher.objects.filter(role_id=roles.first()).first()
    users = User.objects.filter(roles__role_type="instructor").distinct().all()

    return render(request, "index.html",
                  context={'auth_user': request.user, 'core_roles': roles, "plain_roles": plain_roles,
                           'client': client, 'company': company, 'teacher': teacher, 'users': users})


@login_required(login_url='/')
def settings(request):
    if request.method == "POST":

        vartotojas = User.objects.get(username=request.user.first_name)
        role = Roles.objects.filter(user_id=vartotojas.id).first()

        if role.role_type == 'client_company':
            client = Client()
            client.role_id = role
            client.company_name = request.POST.get('client_company_name')
            client.company_code = request.POST.get('client_company_code')
            client.company_address = request.POST.get('client_company_address')
            client.save()

        if role.role_type == 'provider_company':
            company = Company()
            company.roles_id = role
            company.company_name = request.POST.get('provider_company_name')
            company.company_description = request.POST.get('provider_company_description')
            company.save()

        if role.role_type == 'instructor':
            teacher = Teacher()
            teacher.role_id = role
            teacher.other_info = request.POST.get('teacher_description')
            teacher.rating = request.POST.get('rating')
            teacher.save()

        # return HttpResponse("Duomenys išsaugoti")  # Čia tik tam kad parodyti kad veikia
        return redirect(index)


@login_required(login_url='/')
def course(request):
    if request.method == "POST":
        course = Course()
        vartotojas = User.objects.get(username=request.user.first_name)
        role = Roles.objects.filter(user_id=vartotojas.id).first()  # parenkama pirmoji rolė

        course.course_category = request.POST.get("input_course_category")
        course.course_description = request.POST.get("input_course_description")
        course.save()
        return redirect(index)


def dashboard(request):
    return render(request, "dashboard.html")


@login_required(login_url='/')
def instructor(request):
    pass
    # users = User.objects.filter(roles__role_type="instructor").distinct().all()
    # return render(request, "instructor.html",
    #              context={'users': users})
