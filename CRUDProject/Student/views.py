from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import StudentRegistration
from . models import Student
# Create your views here.
def home_page(request):
    return render(request, 'student/home.html')

def add_student(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('../../student/home')
    else:
        fm=StudentRegistration()
    return render(request, 'student/add.html',{'form':fm})

def show_student(request):
    students=Student.objects.all()
    return render(request, 'student/show.html',{'stud':students})

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