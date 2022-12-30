from django.shortcuts import render
from django.http import HttpResponse
from . forms import ContactForm
from django.views import View
# Create your views here.
def homefunc(request):
    type="Function"
    return render(request,'base/home.html',{'type':type}) 
  
class HomeClass(View):
    type="Class"
    def get(self,request):
        return render(request,'base/home.html',{'type':self.type})   

def contactfunc(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('thank you for contacting us.')
    else:
        form=ContactForm()
        return render(request,'base/contact.html',{'form':form})

class ContactClass(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'base/contact.html',{'form':form})
    def post(self,request):
        form= ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('thank you for contacting us.')