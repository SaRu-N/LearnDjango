from django.urls import path 
from . import views
urlpatterns=[
    path('set/',views.setcookie, name='setcookie'),
    path('get/',views.getcookie, name='getcookie'),
    path('del/',views.delcookie, name='delcookie'),
    path('setsigned',views.signedcookie,name='setsigned'),
    path('getsigned',views.getsignedcookie,name='getsigned'),
    path('setsession/',views.setsession,name='setsession'),
    path('getsession/',views.getsession,name='getsession'),
    path('getmethodsession/',views.getsession_methods,name='getmethodsession'),
    path('delsession/',views.delsession,name='delsession'),
    path('settest/',views.settestcookie,name='settestcookie'),
    path('deltest/',views.deltestcookie,name='deltestcookie'),
    path('checktest/',views.checktestcookie,name='gettestcookie'),
]
