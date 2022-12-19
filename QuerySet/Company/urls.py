from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='homepage'),
    path('customer/',views.customer,name='customer'),
]