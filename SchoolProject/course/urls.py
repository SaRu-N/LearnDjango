from django.urls import path
from . import views
urlpatterns =[
   path('',views.home_page),
    path('tutorial/',views.django_tutorial),
    path('project/',views.django_project),
]