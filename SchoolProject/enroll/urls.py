from django.urls import path
from . import views

urlpatterns =[
    path('register/',views.showdata,name='stuform'), 
    path('success/',views.success,name='stuinfo'),
    path('details/',views.stuinfo,name='stuinfo'),
]