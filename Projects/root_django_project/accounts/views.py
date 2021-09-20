
# from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# to let the user know and get inside the site with login method
# for checking the user existance with authnicate method
from django.contrib.auth import authenticate, login, logout

# look the modelbackend which will handle the user authenication
# from django.contrib.auth import backends
from .forms import LoginForm, SignUpForm
# Create your views here.


# from where user models be imported
# from django.contrib.auth.models import User
# from user.models import User

# from django.contrib.auth.models import User, get_user_model
# User = get_user_model()

from django.contrib.auth import get_user_model

User = get_user_model()

# login_required decorators
# from django.contrib.auth.decorators import login_required
# for new user

# using decorators
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
                return render(request,'accounts/fail.html')

    elif request.method == 'GET':
        # if request.user.is_authenticated:
        #     return redirect('/accounts/profile-view/')
            
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
        # return render(request, 'accounts/fail.html')


       
    # for statusapp showing status 
    from statusapp.models import StatusMessage
    messages = StatusMessage.objects.filter(user=request.user) 
    return render(request, 'accounts/profile.html',{
        'messages': messages
    })


def fail_view(request):
    return render(request, 'accounts/fail.html')


def logout_view(request):
    # for throwing or removing the cookies from browser
    logout(request)
    return redirect('/accounts/login-view/')
    # return render (request, 'accounts/login.html')


# for new user sign up

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("congrats form is validated")
            print(form.cleaned_data)

            user = User(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                username = form.cleaned_data['user_name'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email']

                )

            user.save()
            return redirect('/accounts/login-view/')
            user.save()

    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'accounts/signup.html',{'form': form})