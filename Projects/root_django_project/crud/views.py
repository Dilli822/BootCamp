from crud.models import UserInfo
from django.shortcuts import render

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

