from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
class SignUpForm(UserCreationForm):
    # password and confirm password are coming from UserCreationForm
    password2= forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
        
class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
        