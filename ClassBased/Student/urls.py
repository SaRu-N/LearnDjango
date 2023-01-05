from django.urls import path
from . import views
urlpatterns=[
    path('',views.HomeView.as_view(),name='homePage'),
    path('add/',views.AddStudentView.as_view(),name='addStudent'),
    path('edit/<int:id>/',views.UpdateStudentView.as_view(),name='updateStudent'),
    path('details/',views.ShowStudentView.as_view(),name='showStudent'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('logout/',views.LogOutView.as_view(),name='logout'),
    path('delete/<int:id>/',views.DeleteStudentView.as_view(),name='deleteStudent'),
    path('signup/',views.SignUpView.as_view(),name='signup'),



]