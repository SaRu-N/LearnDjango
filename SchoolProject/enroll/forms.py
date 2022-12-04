from django import forms
from django.core import validators

# class StudentRegistration(forms.Form):
    # def start_with_a(value):
    #     if value[0]!='a':
    #         raise forms.ValidationError("Name must start with a")
    # def start_with_2(value):
    #     if value[0]!='2':
    #         raise forms.ValidationError("Value must start with 2")

    # stuemail=forms.EmailField(label="Email",label_suffix=' ')
    # stuid=forms.IntegerField(label="Id")
    # stuname=forms.CharField(label="Name",validators=[start_with_a])
    # stuaddress=forms.CharField(label="Address",validators=[validators.MinLengthValidator(8)])
    # # comment=forms.CharField(initial="Not Available", required=False, widget=forms.Textarea)
    # stupass=forms.CharField(label="Password",widget=forms.PasswordInput)
    # key=forms.CharField(required=False, widget=forms.HiddenInput)
    # # photo=forms.CharField(widget=forms.FileInput)
    # # citizen=forms.FileField()
    # agree = forms.BooleanField(label='I Agree', error_messages={'required':"You must Agree"})
    # price=forms.DecimalField(min_value=5,max_value=100,decimal_places=2)
    # prices=forms.FloatField(min_value=5,max_value=100)
    # new=forms.SlugField(validators=[start_with_2])
    
    # def clean_stuname(self):
    #     val=self.cleaned_data['stuname']
    #     if len(val)<3:
    #         raise forms.ValidationError('Enter more than or 3 characters')
    #     return val
    # def clean(self):
    #     cleaned_data=super().clean()
    #     val=self.cleaned_data['stupass']
    #     val2=self.cleaned_data['stuemail']
    #     if len(val)<8:
    #         raise forms.ValidationError('Password must be of length 8')
    #     val=self.cleaned_data['stuemail']
    #     if len(val2)<10:
    #         raise forms.ValidationError('Email must be of length 10')
    #     return val


    # New registration form
class StudentRegistration(forms.Form):
    # writing hooks
    # error_css_class='error'
    # required_css_class='required'

    username=forms.CharField(error_messages={'required':"Enter Your Name"},validators=[validators.MinLengthValidator(8)])
    email=forms.EmailField(error_messages={'required': "Enter Your Email"},min_length=5)
    password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':"Enter Your Password"},min_length=8)
    repassword=forms.CharField(widget=forms.PasswordInput)

    def clean_repassword(self):
        # cleaned_data=super().clean()
        value=self.cleaned_data['password']
        revalue=self.cleaned_data['repassword']

        if value!=revalue:
            raise forms.ValidationError("Password didn't match")
    # def clean_password(self):
    #     value =self.cleaned_data['password']
    #     if len(value)<8:
    #         raise forms.ValidationError("Password must be of length greater than 8")
    #     return value

class StudentSave(forms.Form):
    name=forms.CharField(label="Name")
    email=forms.EmailField(label="Email")
    password=forms.CharField(widget=forms.PasswordInput)