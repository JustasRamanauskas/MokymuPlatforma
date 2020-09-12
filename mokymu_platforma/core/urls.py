from django.contrib import admin
from django.urls import path, include
from mokymu_platforma.core.views import registracija
from mokymu_platforma.core.views import login
from mokymu_platforma.core.views import password

urlpatterns = [
    path('registracija/', registracija),
    path('', login),
    path('password/', password)
]
