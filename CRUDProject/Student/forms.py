from django.core import validators
from django import forms
from . models import Student

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