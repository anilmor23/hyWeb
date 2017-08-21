from django.conf.urls import url
from . import views
app_name = 'hyUsers'

urlpatterns = [
    url(r'^login', views.LoginFormView.as_view(), name='login'),
    url(r'^signup', views.signupFormView.as_view(), name='logout'),
    url(r'^fgp',views.forgotPasswordView.as_view(), name="forgot-password"),
]
