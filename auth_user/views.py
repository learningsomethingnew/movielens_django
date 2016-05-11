from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.template import RequestContext
from auth_user.custom.registration_form import UserCreateForm

# Create your views here.
def login_user(request):
    return render(request, 'registration/login.html')


def accounts(request):

    options= {'fname':request.user.first_name, 'lname':request.user.last_name, 'email':request.user.email, 'user': request.user.username}
    context = {
        'authed': request.user.is_authenticated(),
        'username': request.user.username,
        'options': options
    }

    return render(request, 'accounts/profile.html', context)


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserCreateForm(request.POST)
        print(request.POST)

        if form.is_valid():
            print(form)
            new_user = form.save()
            return HttpResponseRedirect('/movie_data/')
    else:
        form = UserCreateForm()

    return render(
            request,
            "registration/register.html",
            {'form': form}
        )