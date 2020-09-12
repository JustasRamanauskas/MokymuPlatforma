from django.shortcuts import render

# Create your views here.
def registracija(request):
    return render(request, "index.html")