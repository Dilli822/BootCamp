from modelrelation.models import User
from crud.models import UserInfo
from django.shortcuts import render, get_object_or_404
from .models import UserInfo

# Create your views here.

def list_all_user(request):
    # for storing dynamic data
    data = UserInfo.objects.all()
    # making set data type where we can pick up the data
    context = {
        'data': data
    }

    return render(request, 'crud/list.html', context=context)


# for dob views
def detail_view_of_users(request, user_id):
    # for non existed id and key value pair we can do try catch method
    # user_obj = UserInfo.objects.get(id=user_id)
    # django has shortcut method for error handling and non existed data's request from client
    # with shortcut method 
    user_obj = get_object_or_404(UserInfo, id=user_id)
    # passing in the form of context 
    return render(request, 'crud/details.html',context={
        'user_obj': user_obj
    })


# function '
def create_user_info(request):
    if request.method == 'POST':
        #form passess
        pass
        



