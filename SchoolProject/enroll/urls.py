from django.urls import path
from . import views

urlpatterns =[
    path('register/',views.stuform,name='stuform'), 
    path('details/',views.stuinfo,name='stuinfo'),
]