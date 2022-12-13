from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from . models import Post
from django.utils.translation import gettext, gettext_lazy as _
class SignUpForm(UserCreationForm):
    password2 =forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 =forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        
        }

class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        labels={'title':'Post Title','descriiption':'Post Description'}
        widgets={
            'title':forms.TextInput(attrs=({'class':'form-control'})),
            'description':forms.Textarea(attrs=({'class':'form-control'}))
        }