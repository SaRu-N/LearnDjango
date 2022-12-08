from django.urls import path 
from . import views
urlpatterns=[
    path('reg/', views.sign_up,name='signup'),
    path('login/', views.log_in,name='login'),
    path('profile/',views.user_profile),
    path('logout/',views.user_logout, name='logout')
]
