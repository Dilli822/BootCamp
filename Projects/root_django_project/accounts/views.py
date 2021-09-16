
from django.shortcuts import render
# for checking the user existance with authnicate method
from django.contrib.auth import authenicate
from .forms import LoginForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        # for confirmation of post data
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            # if form is valid and user exists
            user = authenicate(user)
            #ok, and login form will pass
            print(form.cleaned_data)
            # pass
    elif request.method == 'GET':
        form = LoginForm()

    # for invalid case
    return render(request, 'accounts/login.html',
    {'form': form})


def profile_view(request):
    return render(request, 'accounts/profile.html')
