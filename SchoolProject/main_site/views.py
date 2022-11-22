from django.shortcuts import render
# from . import views
# Create your views here.
def home_page(request):
    return render(request,'main/home.html')
def info(request):
    return render(request,'main/info.html')