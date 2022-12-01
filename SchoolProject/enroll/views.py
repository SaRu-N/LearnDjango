from django.shortcuts import render
from . forms import StudentRegistration
from enroll.models import Student 
# Create your views here.
def stuinfo(request):
    stud=Student.objects.all()
    stu=Student.objects.get(pk=4)
    return render(request, 'enroll/stuinfo.html', {'stu':stud, 'st':stu})

def stuform(request):
    fm=StudentRegistration(auto_id=True,initial={'stuemail':'sh@gmail.com'})
    fm.order_fields(field_order=['stuid','stuname','stuemail'])
    return render(request, 'enroll/sturegistration.html', {'form':fm})
