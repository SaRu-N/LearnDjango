from django.shortcuts import render
from . models import Student
from datetime import date, time
from django.db.models import Avg,Min,Max,Sum,Count,StdDev,Q
# Create your views here.
def home(request):
    sd=Student.objects.all()
    # sd=Student.objects.filter(name__exact='Admin')
    # sd=Student.objects.filter(name__iexact='admin')
    # sd=Student.objects.filter(name__contains='a')
    # sd=Student.objects.filter(id__in=[2,4,7])
    # sd=Student.objects.filter(marks__gt=32)
    # sd=Student.objects.filter(marks__gte=32)
    
    # sd=Student.objects.filter(marks__lt=32)
    # sd=Student.objects.filter(marks__lte=32)

    # sd=Student.objects.filter(name__startswith='s')
    # sd=Student.objects.filter(name__endswith='y')

    # sd=Student.objects.filter(passed_date__range=('2020-01-01','2022-12-19'))
    # sd=Student.objects.filter(adm_time__date=date(2022,7,19))
    # sd=Student.objects.filter(adm_time__date__lt=date(2022,7,19))
    # sd=Student.objects.filter(passed_date__year=2021)
    # sd=Student.objects.filter(passed_date__year__gte=2021)
    # sd=Student.objects.filter(passed_date__month=1)
    # sd=Student.objects.filter(passed_date__month__gt=5)
    # sd=Student.objects.filter(passed_date__day=9)
    # sd=Student.objects.filter(passed_date__day__gt=15)
    # sd=Student.objects.filter(passed_date__week=12)
    # sd=Student.objects.filter(passed_date__week__lt=12)
    # sd=Student.objects.filter(passed_date__week_day=4)
    # sd=Student.objects.filter(passed_date__week_day__gte=4)
    # sd=Student.objects.filter(passed_date__quarter=1)

    # sd=Student.objects.filter(adm_time__time__gt=time(10,00))
    # sd=Student.objects.filter(adm_time__hour__gt=9)
    # sd=Student.objects.filter(adm_time__minute__gt=40)

    # sd=Student.objects.filter(roll__isnull=False)



    print("SQL Query",sd.query)
    print("\nReturn:",sd)
    return render(request, 'school/home.html',{'stu':sd})

def aggregation(request):
    sd =Student.objects.all()
    average= sd.aggregate(Avg('marks'))
    sum= sd.aggregate(Sum('marks'))
    max= sd.aggregate(Max('marks'))
    min= sd.aggregate(Min('marks'))
    coount= sd.aggregate(Count('marks'))
    stddev=sd.aggregate(StdDev('marks'))
    print("\nReturn:",sd)
    print("\nSQL Query",sd.query)

    context={'stu':sd,'avg':average,'sum':sum,'min':min,'max':max,'count':coount,'stddev':stddev}
    return render(request, 'school/agg.html',context)

def qobject(request):
    # sd =Student.objects.filter( Q(id=3) & Q(roll=103))
    # sd =Student.objects.filter( Q(id=3) | Q(roll=104))
    sd =Student.objects.filter( ~Q(id=3))
    q=Q(id=3)|Q(roll=102)
    print("Result",q)
    print("SQL",sd.query)
    return render(request, 'school/qobj.html',{'stu':sd})
def limitQS(request):
    sd =Student.objects.all()[:3]
    sd =Student.objects.all()[2:]
    sd =Student.objects.all()[5:9]
    # sd =Student.objects.all()[:3:3]
    print("SQL",sd.query)
    return render(request, 'school/limitqs.html',{'stu':sd})
