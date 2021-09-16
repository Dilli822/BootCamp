
from django.shortcuts import redirect, render

# to let the user know and get inside the site with login method
# for checking the user existance with authnicate method
from django.contrib.auth import authenticate, login

# look the modelbackend which will handle the user authenication
# from django.contrib.auth import backends
from .forms import LoginForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        # for confirmation of post data
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            # if form is valid and user exists
            user = authenticate(
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                print(" A user is found--->", user)
                # redirection after login
                return redirect('/accounts/profile-view/')
            else:
                print("auth credentials donot match!")
            #ok, and login form will pass
                print(form.cleaned_data)

        form = LoginForm()

    elif request.method == 'GET':
        form = LoginForm()

    # for invalid case
    return render(request, 'accounts/login.html',
    {'form': form})


def profile_view(request):
    # if request.user.is_authenicated:
        # pass
        # pass
    # else:
        # no auth give error
        # pass
    return render(request, 'accounts/profile.html')
