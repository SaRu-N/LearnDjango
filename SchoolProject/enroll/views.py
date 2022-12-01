from django.shortcuts import render
from . forms import StudentRegistration
from enroll.models import Student 
from django.http import HttpResponseRedirect
# Create your views here.
def stuinfo(request):
    stud=Student.objects.all()
    stu=Student.objects.get(pk=4)
    return render(request, 'enroll/stuinfo.html', {'stu':stud, 'st':stu})

def stuform(request):
    fm=StudentRegistration(auto_id=True,initial={'stuemail':'sh@gmail.com'})
    fm.order_fields(field_order=['stuid','stuname','stuemail'])
    return render(request, 'enroll/sturegistration.html', {'form':fm})
def success(request):
    return render(request, 'enroll/success.html')
def showdata(request):
    fm=StudentRegistration(auto_id=True,initial={'stuemail':'sh@gmail.com'})
    fm.order_fields(field_order=['stuid','stuname','stuemail'])
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        fm.order_fields(field_order=['stuid','stuname','stuemail'])
        if fm.is_valid():
            print("Form Validated")
            # name=fm.cleaned_data['new']
            # print('Slug',name)
            return HttpResponseRedirect('/enroll/success/')
            # return render(request, 'enroll/success.html', {'nm':name})

        else:
            print("Not Validated")
    else:
        fm=StudentRegistration()
        print("GET Method")
    return render(request, 'enroll/sturegistration.html', {'form':fm})
