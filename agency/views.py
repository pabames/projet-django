from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.

def index(request):
    about = About.objects.all()
    data = {'about': about}
    return render(request, 'view/index.html', data)

def about(request):
    return render(request, "view/about.html")

def visa(request):
    return render(request, "view/visa.html")

def marketing(request):
    return render(request, "view/marketing.html")

def actualites(request):
    return render(request, "view/actualite.html")


""" section des pages statiques """

def web(request):
    return render(request, 'view/web.html')

def design(request):
    return render(request, 'view/design.html')

def application(request):
    return render(request, 'view/application.html')
