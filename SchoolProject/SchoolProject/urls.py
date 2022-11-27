"""SchoolProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from course import views 
from main_site import views

urlpatterns = [
    # default view 
    path('',views.home_page,name='djangohome'),
    path('info/',views.info),
    path('admin/', admin.site.urls),
    path('course/',include('course.urls')),
    path('fees/',include('fees.urls')),
    path('students/',include('Student.urls')),
    path('about/',views.about_page,name="aboutdjango"),

]
