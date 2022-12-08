from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        fm =SignUpForm(request.POST)
        # fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Your Form has been Submitted Successfully")
    else:
        # fm=UserCreationForm()
        fm=SignUpForm()


    return render(request, 'enroll/signup.html', {"form":fm})

def log_in(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            fm= AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user= authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Successful Login")
                    return HttpResponseRedirect('/enroll/profile/')
                
        else:
            fm= AuthenticationForm()
    else:
        messages.error(request,"You have to logout to re login!!!")

        return HttpResponseRedirect('/enroll/profile/')

    return render(request,'enroll/userlogin.html',{'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/enroll/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')