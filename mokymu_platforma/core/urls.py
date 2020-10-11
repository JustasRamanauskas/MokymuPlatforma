from django.contrib import admin
from django.urls import path, include
from mokymu_platforma.core.views import *

urlpatterns = [
    path('registracija/', registracija),
    path('logout/', logout_view),
    path('', login_view),
    path('password/', password),
    path('index/', index),
    path('settings/', settings),
    path('course/', course),
    path('dashboard/', dashboard),
    path('instructor/', instructor),
    path('studentai/', studentai),
    path('kurso-registracija/', register_student_for_course),
    path('studentai/', studentai),
    path('course_list/', course),
    path('new_course_input/', new_course_input)
]
