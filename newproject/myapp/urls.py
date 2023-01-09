from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . forms import LoginForm
urlpatterns=[
    path('',TemplateView.as_view(template_name='myapp/home.html'),name='home'),
    path('dashboard/',TemplateView.as_view(template_name='myapp/dashboard.html'),name='dashboard'),
    path('login/',views.MyLoginView.as_view(),name='login'),
    path('logout/',views.MyLogoutView.as_view(),name='logout'),
    path('changepass/',views.MyPasswordChangeView.as_view(),name='changepass'),
    path('changepassdone/',views.MyPasswordChangeDoneView.as_view(),name='password_change_done'),
]