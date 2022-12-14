from django.urls import path 
from . import views
urlpatterns=[
    path('set/',views.setcookie, name='setcookie'),
    path('get/',views.getcookie, name='getcookie'),
    path('del/',views.delcookie, name='delcookie'),
    path('setsigned',views.signedcookie,name='setsigned'),
    path('getsigned',views.getsignedcookie,name='getsigned'),
]
