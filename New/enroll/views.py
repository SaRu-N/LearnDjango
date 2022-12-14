from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        fm =SignUpForm(request.POST)
        # fm=UserCreationForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name ='Editor')
            user.groups.add(group)
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
                    return HttpResponseRedirect('/enroll/dashboard/')
                
        else:
            fm= AuthenticationForm()
    else:
        messages.error(request,"You have to logout to re login!!!")

        return HttpResponseRedirect('/enroll/profile/')

    return render(request,'enroll/userlogin.html',{'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(request.POST,instance=request.user)
                users= User.objects.all()
            else:  
                users = None
                fm=EditUserProfileForm(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Profile Updated Successfully")
        else:
            if request.user.is_superuser ==True:
                users= User.objects.all()
                fm=EditAdminProfileForm(instance=request.user)
            else:
                users = None
                fm=EditUserProfileForm(instance=request.user)
        return render(request,'enroll/profile.html',{'name':request.user.first_name,'form':fm,'users':users})
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/enroll/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')
# change password with old password
def user_changepass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/enroll/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/enroll/login/')
    return render(request,'enroll/changepass.html',{'form':fm})
# change password without using old password
def user_changepass1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/enroll/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/enroll/login/')
    return render(request,'enroll/changepass1.html',{'form':fm})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html',{'name':request.user.username})
    else:
        return HttpResponseRedirect('enroll/login/')

def user_detail(request,id):
    if request.user.is_authenticated:
        us= User.objects.get(pk=id)
        fm=EditAdminProfileForm(instance=us)
        return render(request,'enroll/userdetail.html',{'form':fm})
    else:
        messages.error(request,'please login first!')
        return HttpResponseRedirect('enroll/login')