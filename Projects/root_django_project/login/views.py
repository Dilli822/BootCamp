
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.



# login required decorators
@login_required
def open(request):
    # for mail sending
    subject = 'Test'
    message = 'You have Successfully Logged in !'
    from_email = 'dillihangrae@gmail.com'
    # list of recipients
    recipients = ['eraeren715@gmail.com', ]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipients)
    # send_mail()
    return render (request, 'login/open.html')

    
def LoginView(request):
    return render(request, 'login/login.html')



def LogoutView(request):
    return render (request, 'login/logout.html')


# use middleware to avoid the excessive uses of
# decorators called @login_required

