from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('This is the homepage of the django project')
def django_tutorial(request):
    return HttpResponse('Welcome to Django Tutorial')
def django_project(request):
    return HttpResponse('<h4>Welcome to Django Project</h4>')