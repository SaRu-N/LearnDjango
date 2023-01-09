from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . forms import LoginForm
urlpatterns=[
    path('',TemplateView.as_view(template_name='myapp/home.html'),name='home'),
    path('dashboard/',TemplateView.as_view(template_name='myapp/dashboard.html'),name='dashboard'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
    path('changepass/',auth_views.PasswordChangeView.as_view(template_name='myapp/changepass.html'),name='changepass'),
    path('changepassdone/',auth_views.PasswordChangeDoneView.as_view(template_name='myapp/changepassdone.html'),name='password_change_done'),
]