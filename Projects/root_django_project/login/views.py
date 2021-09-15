
from django.shortcuts import render

# Create your views here.


def LoginView(request):
    return render(request, 'login/login.html')



def LogoutView(request):
    return render (request, 'login/logout.html')



def open(request):
    return render (request, 'login.html')