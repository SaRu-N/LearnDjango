from django.urls import path
from . import views
urlpatterns=[
        path('',views.home_page,name="homePage"),
        path('home/',views.home_page,name="homePage"),
        path('add/',views.add_student,name="addStudent"),
        path('details/',views.show_student,name="showStudent"),
        path('<int:id>/',views.update_student,name="updateStudent"),
        path('delete/<int:id>', views.delete_student, name='deleteStudent'),
]