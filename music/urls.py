from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views
app_name = 'music'

urlpatterns = [

    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^signup/$', views.signupFormView.as_view(), name='logout'),
    url(r'^ChangePassword/$',views.changePasswordView.as_view(), name="ChangePassword"),

]
