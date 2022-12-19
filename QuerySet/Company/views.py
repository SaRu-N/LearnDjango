from django.shortcuts import render
from . models import Customer, Employee
# Create your views here.
def Home(request):
    emp = Employee.objects.all()
    cs = Customer.objects.all()
    print("SQL Query:",cs.query)
    return render(request, 'company/home.html',{'cs':cs,'emp':emp})
def customer(request):
    # cs = Customer.objects.get(pk=1)

    # cs = Customer.objects.first()
    # cs = Customer.objects.order_by('name').first()
    # cs = Customer.objects.last()
    # cs = Customer.objects.latest('name')
    # cs = Customer.objects.earliest('name')

    # cs= Customer.objects.all()
    # print(cs.exists())
    
    # cs= Customer.objects.all()
    # onecs = Customer.objects.get(pk=1)
    # print(cs.filter(pk=onecs.pk).exists())

    # cs =Customer.objects.create(name='name',csid=145,address='Bhaktapur',email='n@gmail.com',phone='9080706050')

    # cs,created =Customer.objects.get_or_create(name='name2',csid=140,address='Bhaktapur',email='n@gmail.com',phone='9080706050')
    # print("created:", cs,created)

    # cs= Customer.objects.filter(id=5).update(name='Alisha')
    # cs=Customer.objects.filter(address='Bhaktapur').update(phone='9876543210')

    # cs,created = Customer.objects.update_or_create(id=3,name='sabina', defaults={'name':'Sabina Kaki'})
    # print(created)

    # objs=[
    #     Customer(name='Atif',csid=179,address='Lalitpur',email='a@gmail.com',phone='9080706050'),
    #     Customer(name='Suraj',csid=149,address='Bhaktapur',email='aa@gmail.com',phone='9800000000'),
    #     Customer(name='Neha',csid=122,address='Kathmandu',email='na@gmail.com',phone='9888888888'),
    #     Customer(name='Nora',csid=173,address='Lalitpur',email='an@gmail.com',phone='9777777777'),
    # ]
    # cs=Customer.objects.bulk_create(objs)

    # all_cs =Customer.objects.all()
    # for cs in all_cs:
    #     cs.address='Kathmandu'
    # cs =Customer.objects.bulk_update(all_cs,['address'])

    # cs =Customer.objects.in_bulk([1,2])
    # print(cs[1].name)
    # print(cs[2].name)

    # cs =Customer.objects.in_bulk([])

    # cs =Customer.objects.get(pk=7).delete()
    # cs =Customer.objects.filter(phone='9080706050').delete()
    # cs =Customer.objects.all().delete()

    # cs=Customer.objects.all()
    # print(cs.count())

    cs=print(Customer.objects.filter(address='kathmandu').explain())

    # print("Return",cs)
    # print("SQL Query:",cs.query)

    return render(request,'company/customer.html',{'cs':cs})


