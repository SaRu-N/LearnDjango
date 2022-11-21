from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request,'home.html')
def django_tutorial(request):
    return render(request,'tutorial.html')
def django_project(request):
    return render(request,'project.html')