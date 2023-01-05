from django.core import validators
from django import forms
from . models import Student
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserChangeForm

class StudentRegistration(forms.ModelForm):
    class Meta:
        model= Student
        fields=['Name','Email','Phone','Address','Faculty']
        labels={'Name':'Enter Name','Email':'Enter Email','Phone':'Enter Mobile Number','Address':'Enter Address','Faculty':'Choose Faculty'}
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'}),
            'Faculty':forms.TextInput(attrs={'class':'form-control'})
        }

class EditProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}