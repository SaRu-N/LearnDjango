from django.shortcuts import render

# Create your views here.
def setsession(request):
   request.session['name']='Session name'
   request.session['lname']='Session last name'
   return render(request,'customer/setsession.html')
def getsession(request):
      name=request.session.get('name')
      lname=request.session.get('lname')
    
      return render(request,'customer/getsession.html',{'name':name,'lname':lname,})
   
def delsession(request):

   # using Flush
   request.session.flush()
   # this will delete all expired sessions
   request.session.clear_expired()
   return render(request,'customer/delsession.html')
