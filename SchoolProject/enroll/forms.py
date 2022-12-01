from django import forms

class StudentRegistration(forms.Form):
    stuemail=forms.EmailField(label="Email",label_suffix=' ')
    stuid=forms.IntegerField(label="Id")
    stuname=forms.CharField(label="Name")
    # comment=forms.CharField(initial="Not Available", required=False, widget=forms.Textarea)
    stupass=forms.CharField(label="Password",widget=forms.PasswordInput)
    key=forms.CharField(required=False, widget=forms.HiddenInput)
    # photo=forms.CharField(widget=forms.FileInput)
    # citizen=forms.FileField()
    agree = forms.BooleanField(label='I Agree', error_messages={'required':"You must Agree"})
    price=forms.DecimalField(min_value=5,max_value=100,decimal_places=2)
    prices=forms.FloatField(min_value=5,max_value=100)
    new=forms.SlugField()
    
    def clean_stuname(self):
        val=self.cleaned_data['stuname']
        if len(val)<3:
            raise forms.ValidationError('Enter more than or 3 characters')
        return val
    def clean(self):
        cleaned_data=super().clean()
        val=self.cleaned_data['stupass']
        val2=self.cleaned_data['stuemail']
        if len(val)<8:
            raise forms.ValidationError('Password must be of length 8')
        val=self.cleaned_data['stuemail']
        if len(val2)<15:
            raise forms.ValidationError('Email must be of length 8')
        return val

