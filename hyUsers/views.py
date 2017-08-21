from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignupForm,forgotPassword
from django.views.generic import View
from django.http import HttpResponse
from . models import hyUser

class LoginFormView(View):
    form_class= LoginForm
    template_name='users/login.html'

    def get(self, request):
        form=self.form_class(None)
        return  render(request, self.template_name,{'form':form})
    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            #cleaned Normalised data
            username=form.cleaned_data['officeEmail']
            password=form.cleaned_data['password']

            #user.set_password(password)
            # Returns User objects if credentials are correct
            user=authenticate(officeEmail=username, password=password)
            print user,"Office Email ", username, " Password ",password

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("<h2>You are now Logged In</h2")
        return render(request,self.template_name,{'form':form})


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
            username=form.cleaned_data['officeEmail']
            password=form.cleaned_data['password']

            a=hyUser.objects.filter(officeEmail=username)
            print a.exists()
            if(a.exists()):
                error_message="This Email has already been used. If you don't remember the password then please click Forgot Password Button"
                print "Duplicate Email"
                return render(request, self.template_name, {'error_message':error_message,'form': form})
            else:

                user.save()
                return redirect("hyUsers:login")

class forgotPasswordView(View):
    form_class= forgotPassword
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
            username=form.cleaned_data['officeEmail']
            password=form.cleaned_data['password']
            password1=form.cleaned_data['newPassword1']
            password2 = form.cleaned_data['newPassword2']

            user.save()

            # Returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    if(password1==password2):
                        print "Password is changed"

        return render(request, self.template_name, {'form': form})

