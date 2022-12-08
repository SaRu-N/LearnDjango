from django.urls import path 
from . import views
urlpatterns=[
    path('reg/', views.sign_up,name='signup'),
    path('login/', views.log_in,name='login'),
    path('profile/',views.user_profile,name='userprofile'),
    path('logout/',views.user_logout, name='logout'),
    path('changepass1/',views.user_changepass1,name='changepass1'),
    path('changepass/',views.user_changepass,name='changepass')
]
