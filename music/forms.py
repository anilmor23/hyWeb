from .models import HypoUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(label='User Name')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.CharField(label='Office Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    mobile=forms.IntegerField(label='Mobile')
    requirement=forms.CharField(label='What is Your requirement')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','mobile','requirement']

class LoginForm(forms.ModelForm):
    email = forms.CharField(label="Email Address")
    password = forms.CharField(label='Enter Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['email','password']

class ForgotPassword_Form(forms.ModelForm):
    email = forms.CharField(label="Email Address")
    passold = forms.CharField(label='Current Password',widget=forms.PasswordInput)
    pass1= forms.CharField(label='New Password',widget=forms.PasswordInput)
    pass2= forms.CharField(label='Re-Enter New Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['email','passold','pass1','pass2']