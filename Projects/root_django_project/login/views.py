
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.




# login required decorators
@login_required
def open(request):
    return render (request, 'login/open.html')

    
def LoginView(request):
    return render(request, 'login/login.html')



def LogoutView(request):
    return render (request, 'login/logout.html')