from django.urls import path
from . import views
from django.views import View
urlpatterns = [
    path('homefun/',views.homefunc,name='homefun'),
    path('homec/',views.HomeClass.as_view(),name='homec'),
    path('contactfun/',views.contactfunc,name='contactfun'),
    path('contactc/',views.ContactClass.as_view(),name='contcatc'),

]