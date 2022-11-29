from django.shortcuts import render
from enroll.models import Student 
# Create your views here.
def stuinfo(request):
    stud=Student.objects.all()
    stu=Student.objects.get(pk=4)
    return render(request, 'enroll/stuinfo.html', {'stu':stud, 'st':stu})