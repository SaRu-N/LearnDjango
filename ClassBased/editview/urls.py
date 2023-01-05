from django.urls import path
from . import views
urlpatterns=[
    path('contact/',views.ContactFormView.as_view(),name='contact'),
    path('thankyou/',views.ThankYouView.as_view(),name='thankyou'),
    path('create/',views.PersonCreateView.as_view(),name='create'),
    path('det/<int:pk>/',views.PersonDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.PersonUpdateView.as_view(),name='update'),
]