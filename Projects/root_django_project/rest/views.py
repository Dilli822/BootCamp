
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
# Create your views here.
# for csrf
@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'messgae': 'adding two numbers'})

    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("request.POST--->", request.POST)

        print("data --->", data)

        # now let's add the post numbers
        result = data['number1'] + data['number2']
        
        
        return JsonResponse({'result': result })
