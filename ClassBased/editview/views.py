from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from django.views.generic import TemplateView
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