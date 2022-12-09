from django.urls import path
from . import views
urlpatterns=[
        path('',views.log_in,name="homePage"),
        path('home/',views.log_in,name="login"),
        path('login/',views.log_in,name='login'),
        path('signup',views.sign_up, name='signup'),
        path('add/',views.add_student,name="addStudent"),
        path('details/',views.show_student,name="showStudent"),
        path('<int:id>/',views.update_student,name="updateStudent"),
        path('delete/<int:id>', views.delete_student, name='deleteStudent'),
        path('profile/',views.profile,name='profile'),
        path('logout',views.user_logout,name='logout'),
        path('changepass/',views.changepass,name='changepass')
]