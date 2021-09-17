
# from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# to let the user know and get inside the site with login method
# for checking the user existance with authnicate method
from django.contrib.auth import authenticate

# look the modelbackend which will handle the user authenication
# from django.contrib.auth import backends
from .forms import LoginForm
# Create your views here.

# login_required decorators
# from django.contrib.auth.decorators import login_required


# using decorators here
# @login_required
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
    if request.user.is_authenticated:
        # pass
        # print 
        print("I am authenicated!")
    else:
        # we have put conditionals but
        # with decorators login_required
        # we can do this in more shortcuts way
        # no auth give error
        # pass
        print("---I am not authenicated!---")
        return HttpResponse("Invalid User")

    return render(request, 'accounts/profile.html')
