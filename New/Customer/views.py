from django.shortcuts import render
from datetime import timedelta,datetime
# Create your views here.
def setcookie(request):
   response = render(request, 'customer/setcookie.html')
   response.set_cookie('fname','Customer', expires=datetime.utcnow()+timedelta(days=2))
#    max_age and expires can not be used together
   response.set_cookie('lname','One', max_age=60)
   return response
def getcookie(request):
    # name=request.COOKIES['fname']
    name =request.COOKIES.get('fname','no fname')
    lname= request.COOKIES.get('lname','no lname')
    return render(request, 'customer/getcookie.html',{'name':name,'lname':lname})
def delcookie(request):
    response =render(request, 'customer/delcookie.html')
    response.delete_cookie('fname')
    response.delete_cookie('lname')
    return response 
def signedcookie(request):
   response=render(request,'customer/setcookie.html')
   response.set_signed_cookie('age','55',salt='ag', expires=datetime.utcnow()+timedelta(days=1))
   return response
def getsignedcookie(request):
   age = request.get_signed_cookie('age',default='no age',salt='ag')
   return render (request, 'customer/getcookie.html', {'age':age})

# Session
def setsession(request):
   request.session['name']='Session name'
   # setting expiry 0 will make expire_at_browser_close = TRUE
   request.session.set_expiry(600)
   request.session['lname']='Session last name'
   return render(request,'customer/setsession.html')
def getsession(request):
   # name=request.session['name']
   # using get method
   name=request.session.get('name','no session')
   lname=request.session.get('lname','no session lastname')
   keys=request.session.keys()
   items=request.session.items()
   # can set and get value
   age= request.session.setdefault('age','55')
   return render(request,'customer/getsession.html',{'name':name,'lname':lname,'keys':keys,'items':items,'age':age})
def delsession(request):
   # if 'name' in request.session:
   #    del request.session['name']
   # if 'name' in request.session:
   #    del request.session['lname']

   # using Flush
   request.session.flush()
   # this will delete all expired sessions
   request.session.clear_expired()
   return render(request,'customer/delsession.html')

# to use various methods
def getsession_methods(request):
   name= request.session['name']
   return render(request,'customer/getmethodsession.html',{'name':name})

def settestcookie(request):
   request.session.set_test_cookie()
   return render(request, 'customer/settestcookie.html')

def checktestcookie(request):
   value=request.session.test_cookie_worked()
   return render(request, 'customer/checktestcookie.html',{'res':value})

def deltestcookie(request):
   request.session.delete_test_cookie()
   return render(request, 'customer/deltestcookie.html')