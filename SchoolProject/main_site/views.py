from django.shortcuts import render
# from . import views
# Create your views here.
def home_page(request):
    return render(request,'main/home.html',{'f':'Flutter'})
def info(request):
    return render(request,'main/info.html')
def about_page(request):
    return render(request,'main/about.html')
