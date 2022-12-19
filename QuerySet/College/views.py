from django.shortcuts import render
from . models import Student, Teacher
from django.db.models import Q
# Create your views here.
def home(request):
    st = Student.objects.all()
    print("SQL Query:",st.query)
    return render(request, 'college/home.html',{'stu':st})
def passed(request):
    # st = Student.objects.filter(marks=98)
    # st=Student.objects.exclude(marks=12)

    # st =Student.objects.order_by('-marks')
    # st =Student.objects.order_by('marks')
    # st =Student.objects.order_by('?')

    # st =Student.objects.order_by('id').reverse()[:3]
# this returns in the form of dictonary
    # st=Student.objects.values()
    # st=Student.objects.values('name','address')
# this returns in the form of tuples
    # st=Student.objects.values_list()
    # st=Student.objects.values_list('id','name')
    # st=Student.objects.values_list('id','name',named=True)
    
    # st= Student.objects.using('default')

    # st= Student.objects.dates('dob','year')
    # st= Student.objects.dates('passed_date','month')

    # #################### AND or OR operator
    # st=Student.objects.filter(address='Kathmandu')& Student.objects.filter(name='Name')
    # st=Student.objects.filter(address='Kathmandu',name='Name')
    # st=Student.objects.filter( Q(address='Kathmandu') & Q(name='Name'))
   
    # st=Student.objects.filter(address='Kathmandu') | Student.objects.filter(name='Name')
    st=Student.objects.filter( Q(address='Kathmandu') | Q(name='Name'))

   
    print("SQL Query:",st.query)
    print(st)

    return render(request, 'college/home.html',{'stu':st})
def teacher(request):
    qs1=Student.objects.values_list('id','name', named=True)
    qs2=Teacher.objects.values_list('id','name', named=True)
    # t= qs2.union(qs1,all=True)
    # t= qs2.intersection(qs1)
    # t= qs2.difference(qs1)
    # t= qs1.difference(qs2)


    return render(request, 'college/home.html',{'stu':t})
