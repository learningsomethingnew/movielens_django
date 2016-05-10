from django.conf.urls import url, include
from .views import login_user, accounts

urlpatterns = [
    url(r'login/', login_user),
    url(r'profile/', accounts),
]