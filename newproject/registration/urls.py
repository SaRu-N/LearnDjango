from django.urls import path
from . import views
from . views import ProfileView,AboutView,ContactView
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.admin.views.decorators import staff_member_required
urlpatterns=[
    path('profile/',views.profile,name='profile'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('profilecl/',views.ProfileView.as_view(),name='proflecl'),
    path('aboutcl/',views.AboutView.as_view(),name='aboutcl'),
    path('contactcl/',views.ContactView.as_view(),name='contactcl'),
    path('profilecl/',login_required(ProfileView.as_view()),name='profilecl'),
    path('aboutcl/',staff_member_required(AboutView.as_view()),name='aboutcl'),
    path('contactcl/',permission_required("registration.can_add_user")(ContactView.as_view()),name='contactcl'),
]