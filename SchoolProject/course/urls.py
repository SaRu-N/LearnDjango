from django.urls import path
from . import views
urlpatterns =[
    path('tutorial/',views.django_tutorial),
    path('info/',views.django_info,name='courseinfo'),
    path('project/',views.django_project),
]