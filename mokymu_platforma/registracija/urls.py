from django.contrib import admin
from django.urls import path, include
from mokymu_platforma.registracija.views import registracija

urlpatterns = [
    path('registracija/', registracija),
]
