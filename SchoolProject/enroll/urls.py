from django.urls import path
from . import views

urlpatterns =[
    path('register/',views.showdata,name='stuform'), 
    path('save/',views.stusaveform,name='stusaveform'), 
    path('success/',views.success,name='stuinfo'),
    path('details/',views.stuinfo,name='stuinfo'),
]