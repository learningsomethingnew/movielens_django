from django.conf.urls import url, include
from .views import login_user, accounts, register

app_name = 'auth_user'

urlpatterns = [
    url(r'login/$', login_user, name='login'),
    url(r'profile/$', accounts, name='accounts'),
    url(r'register/$', register, name='register'),
]