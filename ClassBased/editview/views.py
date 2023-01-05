from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,PersonForm
from . models import Person
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms
# Create your views here.

class ContactFormView(FormView):
    template_name='editview/contact.html'
    form_class =ContactForm
    success_url='../thankyou/'
    initial ={'name':'name'}
    def form_valid(self, form):
        # print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return super().form_valid(form)
        return HttpResponse('Thank You')

class ThankYouView(TemplateView):
    template_name='editview/thankyou.html'

# class PersonCreateView(CreateView):
#     model=Person
#     fields =['name','email','password']
#     success_url='../thankyou/'

#     def get_form(self):
#         form=super().get_form()
#         form.fields['password'].widget= forms.PasswordInput()
#         form.fields['name'].widget= forms.TextInput(attrs={'class':'myclass'})
#         return form

# class PersonUpdateView(UpdateView):
#     model=Person 
#     fields =['name','email','password']
#     success_url='../../thankyou/'
#     def get_form(self):
#         form=super().get_form()
#         form.fields['password'].widget= forms.PasswordInput()
#         return form
    
class PersonCreateView(CreateView):
    form_class=PersonForm
    template_name='editview/person_form.html'

class PersonUpdateView(UpdateView):
    model=Person
    form_class=PersonForm
    template_name='editview/person_form.html'

class PersonDetailView(DetailView):
    model=Person

