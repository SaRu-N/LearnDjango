from django.urls import path
from . import views 
urlpatterns=[
    path('',views.home),
    path('agg/',views.aggregation),
    path('qobj/',views.qobject),
    path('limitqs/',views.limitQS),
]