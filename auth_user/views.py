from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login_user(request):
    return render(request, 'registration/login.html')


def accounts(request):

    context = {
        'authed': request.user.is_authenticated(),
        'username': request.user.username
               }

    return render(request, 'accounts/profile.html', context)
