from django.shortcuts import render
from django.views.generic.list import ListView
from . models import Person
# Create your views here.
class PersonListView(ListView):
    model=Person
    # template_name_suffix='_get'

class CustomPersonList(ListView):
    model=Person
    template_name='listview/person.html'
    def get_queryset(self):
        return Person.objects.filter(age=22)
    def get_context_data(self,*args,**kwargs):
        context= super().get_context_data(*args,**kwargs)
        context['eligible']=Person.objects.all().order_by('age')
        return context
    def get_template_names(self):
        # if self.request.COOKIES['person']=='saru':
        #     template_name='listview/saru.html'
        # else:
        #     template_name= self.template_name
        # return [template_name]
        if self.request.user.is_superuser:
            template_name='listview/superuser.html'
        elif self.request.user.is_staff:
            template_name='listview/staff.html'
        else:
            template_name =self.template_name
        return [template_name]