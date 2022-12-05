from django import forms
from . models import Teacher

class TeacherRegistration(forms.ModelForm):
    Phone=forms.CharField(min_length=10,max_length=10)
    class Meta:
        model=Teacher
        fields=['Name','Phone','Email','Password']
        labels={'Name':'Enter Name','Email':'Enter Email','Phone':'Enter Mobile Number'}
        help_texts={'Phone':'Number must be of 10 digits'}
        error_messages={
            'Name':{'required':'You must enter your Name'},
            'Phone':{'required':'You must enter your Name','min_length':'Minimum length is 10'},
            'Email':{'required':'You must enter your Email'},
            'Password':{'required':'You must enter your Password'}
            }
        widgets={'Password':forms.PasswordInput}