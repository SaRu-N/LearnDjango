from django.urls import path
from . import views
urlpatterns =[

    path('djangofees/',views.fees_django),
]