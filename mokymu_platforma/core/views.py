import json

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from mokymu_platforma.core.models import User, Roles, Client, Company, Teacher, Course, Student
from mokymu_platforma.core.models import CoursesCompany, CoursesGroup, ScheduleCourse, ContractStudent


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
    student = Student.objects.filter(role_id=roles.first()).first()
    studentu_sarasas = User.objects.filter(roles__role_type='student').distinct().all()
    courses = Course.objects.all()
    instructor_users = User.objects.filter(roles__role_type="instructor").distinct().all()
    schedule_courses = ScheduleCourse.objects.all()

    for course in schedule_courses:
        course.id

    return render(request, "index.html",
                  context={'auth_user': request.user, 'core_roles': roles, "plain_roles": plain_roles,
                           'client': client, 'company': company, 'teacher': teacher, "courses": courses,
                           "student": student, 'instructor_users': instructor_users,
                           'studentu_sarasas': studentu_sarasas, 'schedule_courses': schedule_courses})

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

        if role.role_type == 'student':
            student = Student()
            student.role_id = role
            student.student_personalCode= request.POST.get('student_personal_code')
            student.save()

        # return HttpResponse("Duomenys išsaugoti")  # Čia tik tam kad parodyti kad veikia
        return redirect(index)


@login_required(login_url='/')
def course(request):
    if request.method == "GET":
        courses = Course.objects.all()
        return render(request, "course.html", context={"courses": courses})

    if request.method == "POST":
        vartotojas = User.objects.get(username=request.user.first_name)
        company = Company.objects.get(roles_id__user_id=vartotojas)
        course = Course()
        course.course_category = request.POST.get("input_course_category")
        course.course_description = request.POST.get("input_course_description")
        course.save()

        course_company = CoursesCompany()
        course_company.company_id = company
        course_company.course_id = course
        course_company.save()

        courses_group = CoursesGroup()
        courses_group.course_company_id = course_company
        courses_group.course_teacher_id = Teacher.objects.get(role_id__user_id = int(request.POST.get("input_teacher")))
        courses_group.course_group_description = request.POST.get("input_course_description")
        courses_group.course_group_price = request.POST.get("input_course_price")
        courses_group.save()

        schedule_course = ScheduleCourse()
        schedule_course.course_group_id = courses_group
        schedule_course.start_date = request.POST.get('input_start_theory_date')
        schedule_course.finish_date = request.POST.get('input_exam_date')
        schedule_course.start_theory_date = request.POST.get('input_start_theory_date')
        schedule_course.finish_theory_date = request.POST.get('input_finish_theory_date')
        schedule_course.start_practice_date = request.POST.get('input_start_practice_date')
        schedule_course.finish_practice_date = request.POST.get('input_finish_practice_date')
        schedule_course.exam_date = request.POST.get('input_exam_date')
        schedule_course.save()

        return redirect(index)

@login_required(login_url='/')
def dashboard(request):
    redirect(index)


@login_required(login_url='/')
def instructor(request):
    pass

@login_required(login_url='/')
def studentai(request):
    pass

@login_required(login_url='/')
def register_student_for_course(request):
    if request.method == "POST":
        data = json.loads(request.body)
        schedule_course = ScheduleCourse.objects.get(id=data['course_id'])
        user = request.user
        contract_student = ContractStudent()
        contract_student.schedule_course_id = schedule_course
        contract_student.student_id = Student.objects.get(role_id__user_id=user)
        contract_student.price = schedule_course.course_group_id.course_group_price
        contract_student.save()
        return HttpResponse(status=200)