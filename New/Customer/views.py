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