from django.urls import path
from . import views
urlpatterns=[
    path('',views.PersonListView.as_view(),name='personList'),
    path('cs/',views.CustomPersonList.as_view()),

]