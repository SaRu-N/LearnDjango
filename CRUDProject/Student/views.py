from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from . forms import StudentRegistration, EditProfileForm
from . models import Student
# Create your views here.

def add_student(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            fm=StudentRegistration(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('../../student/home')
        else:
            fm=StudentRegistration()
        return render(request, 'student/add.html',{'form':fm})
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/student/login/')

def show_student(request):
    if request.user.is_authenticated:

        students=Student.objects.all()
        return render(request, 'student/show.html',{'stud':students})
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/student/login/')

def update_student(request,id):
    if request.method=='POST':
        st=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=st)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('../details')
        else:
            st=Student.objects.get(pk=id)
            fm=StudentRegistration(instance=st)
    return render(request, 'student/update.html',{'form':fm})

def delete_student(request,id):
    if request.method=='POST':
        st=Student.objects.get(pk=id)
        st.delete()
        return HttpResponseRedirect('../../student/details')


def sign_up(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Your Form has been Submitted Successfully")
            return HttpResponseRedirect('/student/login/')
    else:
        fm=UserCreationForm()

    return render(request, 'student/signup.html', {"form":fm})

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
                    return HttpResponseRedirect('/student/profile/')    
        else:
            fm= AuthenticationForm()
    else:
        messages.error(request,"You have to logout to re login!!!")

        return HttpResponseRedirect('/student/profile/')

    return render(request,'student/home.html',{'form':fm})

def profile(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            fm= EditProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Profile Udated Successfully')
        else:
            fm=EditProfileForm(instance=request.user)
        return render(request,'student/profile.html',{'name':request.user,'form':fm})
        
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/student/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/student/home/')
# change password with old password
def changepass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/student/details/')
        else:
            fm=PasswordChangeForm(user=request.user)
    else:
        messages.error(request,"Please Login First!!!")

        return HttpResponseRedirect('/enroll/login/')
    return render(request,'student/changepass.html',{'form':fm})
