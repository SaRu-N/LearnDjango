from django import forms
from .models import Person
class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    msg=forms.CharField(widget=forms.Textarea)

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','email','password']
        widgets={'password':forms.PasswordInput(attrs={'class':'myclass'})}
