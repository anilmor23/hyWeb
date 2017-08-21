# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm, ForgotPassword_Form
from django.views.generic import View
from django.http import HttpResponse
from .models import HypoUser
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return HttpResponse("<h1>Main Page</h1>")

# Create your views here.
class signupFormView(View):
    form_class= SignupForm
    template_name='users/login.html'

    def get(self, request):
        form=self.form_class(None)
        return  render(request, self.template_name,{'form':form})
    def post(self, request):
        form=self.form_class(request.POST)
        print " Checking the validity of the form"
        if form.is_valid():
            user=form.save(commit=False)
            #cleaned Normalised data
            email=form.cleaned_data['email']

            a=User.objects.filter(email=email)
            print a.exists()
            if(a.exists()):
                error_message="This Email has already been used. If you don't remember the password then please click Forgot Password Button"
                print "Duplicate Email"
                return render(request, self.template_name, {'error_message':error_message,'form': form})
            elif(form.cleaned_data['password1']!=form.cleaned_data['password1']):
                error_message = "The two entered passwords does not match."
                print "Password DOES not match"
                return render(request, self.template_name, {'error_message': error_message, 'form': form})
            else :
                print "Going to save the detials"
                b=User()
                b.username=form.cleaned_data['username']
                b.first_name=form.cleaned_data['first_name']
                b.last_name=form.cleaned_data['last_name']
                b.set_password(form.cleaned_data['password1'])
                b.email=form.cleaned_data['email']
                b.save()
                c=HypoUser()
                c.user=b
                c.mob=form.cleaned_data['mobile']
                c.question=form.cleaned_data['requirement']
                c.save()
                subject='Welcome To Hypothizer Family'
                message="HI There, \n we welcome you to Hypothizer Family"
                from_user=settings.EMAIL_HOST_USER
                to_list=['anil.iitr12@gmail.com', 'pratap.singh167@gmail.com ']
                send_mail(subject,message,from_user,to_list,fail_silently=True)
                return HttpResponse("User Saved and Mail Sent")

        return render(request, self.template_name, {'error_message':'','form': form})


class LoginFormView(View):
       form_class = LoginForm
       template_name = 'users/login.html'
       def get(self, request):
           form = self.form_class(None)
           return render(request, self.template_name, {'form': form})

       def post(self, request):
           form = self.form_class(request.POST)

           if form.is_valid():
               user = form.save(commit=False)
               email = form.cleaned_data['email']
               password = form.cleaned_data['password']

               try:

                   check = User.objects.get(email=email)

               except(KeyError
                      , User.DoesNotExist):
                   return render(request,self.template_name, {
                       'form':form,
                       'error_message': "This Mail is not registered with us",
                   })
               else:
                    username=check.username
                    user = authenticate(username=username, password=password)
                    if user is not None:
                       if user.is_active:
                           login(request, user)
                           return HttpResponse("<h2>You are now Logged In</h2>")
           return render(request, self.template_name, {'form': form})

class changePasswordView(View):
    form_class = ForgotPassword_Form
    template_name = 'users/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['passold']

            try:
                check = User.objects.get(email=email)

            except(KeyError
                   , User.DoesNotExist):
                return render(request, self.template_name, {
                    'form': form,
                    'error_message': "This Mail is not registered with us",
                })
            else:
                username = check.username
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        pass1=form.cleaned_data['pass1']
                        pass2=form.cleaned_data['pass2']

                        if(pass1==pass2):
                            user.set_password(pass2)
                            user.save()
                            return HttpResponse("<h2>Password changed </h2>")
                        return HttpResponse("<h2>You are now Logged In</h2>")
                return HttpResponse("<h2>The Uername and password doesnot match</h2>")
        return render(request, self.template_name, {'form': form})

