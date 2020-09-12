from django.contrib import admin
from django.urls import path, include
from mokymu_platforma.core.views import registracija

urlpatterns = [
    path('registracija/', registracija),
]
