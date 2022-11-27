from django.urls import path
from . import views
urlpatterns =[
    path('',views.home,name='studenthome'),
    path('details/',views.detail,name='studentdetail'),
]