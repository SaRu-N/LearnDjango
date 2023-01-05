from django.urls import path
from . import views
urlpatterns=[
    path('contact/',views.ContactFormView.as_view(),name='contact'),
    path('thankyou/',views.ThankYouView.as_view(),name='thankyou'),
]