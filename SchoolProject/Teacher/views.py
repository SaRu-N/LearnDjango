from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import TeacherRegistration
from . models import Teacher
# Create your views here.
def RegTeacher(request):
    if request.method=='POST':
      #adding pi as instance 
        pi=Teacher.objects.get(pk=2)
        fm=TeacherRegistration(request.POST,instance=pi)
        # fm=TeacherRegistration(request.POST)

        if fm.is_valid():
            #updating data using instance
            fm.save()

            # nm=fm.cleaned_data['Name']
            # em=fm.cleaned_data['Email']
            # ph=fm.cleaned_data['Phone']
            # pw=fm.cleaned_data['Password']

            # To display the values in terminal
            # print("Name:",nm)
            # print("Email:",em)
            # print("Phone:",ph)

            #to save datas in database
            # reg=Teacher(Name=nm,Email=em,Phone=ph,Password=pw)
            # reg.save()

            #to update teacher having id 2
            # reg=Teacher(id=2,Name=nm,Email=em,Phone=ph,Password=pw)
            # reg.save()

            #to delete teacher having id 3
            # reg1=Teacher(id=3)
            # reg1.delete()
            return HttpResponseRedirect('/enroll/success/')
    else:
        fm=TeacherRegistration()

    return render(request,'teacher/teacherReg.html' ,{"form":fm})
