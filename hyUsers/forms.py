from .models import hyUser
from django import forms

class LoginForm(forms.ModelForm):
    officeEmail = forms.CharField(label='Office Email Address', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = hyUser
        fields = ['officeEmail','password']



class SignupForm(forms.ModelForm):
    officeEmail = forms.CharField(label='Office Email Address', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    where=forms.CharField(label='What is you Business Requirement', required=False)
    mob = forms.CharField(label='Mobile Number', required=True)
    lname = forms.CharField(label='Last Name', required=True)
    fname = forms.CharField(label='First Name', required=True)
    company = forms.CharField(label='Company Name', required=True)
    class Meta:
        model = hyUser
        fields = ['fname','lname','company','officeEmail','mob','password','where']

class forgotPassword(forms.ModelForm):
    officeEmail = forms.CharField(label='Office Email Address', required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Current Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newPassword1=forms.CharField(label='New Password', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    newPassword2 = forms.CharField(label='Confirm New Password', required=True,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=hyUser
        fields = ['officeEmail','password','newPassword1','newPassword2' ]
