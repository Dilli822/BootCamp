from django.shortcuts import render

# Create your views here.

def list_all_user(request):
    # for storing dynamic data
    
    return render(request, 'crud/list.html')

