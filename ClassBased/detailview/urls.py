from django.urls import path
from . import views

urlpatterns=[
        path('list/',views.PersonListView.as_view(),name='list'),
        path('<int:pk>/',views.PersonDetailView.as_view(),name='detail'),
]