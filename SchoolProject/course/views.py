from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request,'course/home.html')
def django_tutorial(request):
    cname='Djnago'
    duration='4 months'
    seats=20
    courseinfo={'cn':cname,'du':duration,'sa':seats}
    return render(request,'course/tutorial.html',courseinfo)
def django_project(request):
    return render(request,'course/project.html')