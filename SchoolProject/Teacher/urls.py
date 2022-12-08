from django.urls import path, register_converter
from . import views,converters

register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns=[
    path('',views.Home, {'check':'ok'}, name='home'),
    # path('register/', views.RegTeacher),
    # path('details/<int:my_id>/',views.show_details,name='details'),
    # path('details/<int:my_id>/<int:my_subid>',views.show_subdetails,name='subdetails'),
    # path('session/<yyyy:year>',views.show_date,name='showdate'),
    path('regstudent/',views.stuform),
    path('regteacher/',views.teacherform)

]