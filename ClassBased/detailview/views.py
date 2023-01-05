from django.shortcuts import render
from listview.models import Person
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class PersonDetailView(DetailView):
    model=Person
    template_name='detailview/person_detail.html'
    context_object_name='per'  
    
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['all']=self.model.objects.all().order_by('name')
        return context

class PersonListView(ListView):
    model=Person  
