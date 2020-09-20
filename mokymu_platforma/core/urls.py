from django.contrib import admin
from django.urls import path, include
from mokymu_platforma.core.views import *

urlpatterns = [
    path('registracija/', registracija),
    path('logout/',logout_view),
    path('', login_view),
    path('password/', password),
    path('index/', index)
]
