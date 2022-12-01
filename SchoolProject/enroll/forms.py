from django import forms

class StudentRegistration(forms.Form):
    stuemail=forms.EmailField(label="Email",label_suffix=' ')
    stuid=forms.IntegerField(label="Id")
    stuname=forms.CharField(label="Name",help_text="Enter your full name")
    comment=forms.CharField(initial="Not Available", required=False, widget=forms.Textarea)
    stupass=forms.CharField(label="Password",widget=forms.PasswordInput)
    key=forms.CharField(widget=forms.HiddenInput)
    photo=forms.CharField(widget=forms.FileInput)
    citizen=forms.FileField()
