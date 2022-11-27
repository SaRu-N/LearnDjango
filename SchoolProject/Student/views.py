from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def detail(request):
    fname='Harry'
    lname='sharma'
    age=20
    student_detail={'fn':fname,'ln':lname,'a':age}
    return render(request,'student/detail.html',student_detail)
def home(request):
    return render(request,'student/home.html')

