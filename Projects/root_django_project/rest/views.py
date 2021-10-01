
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .serializers import AddTwoNumberSerializer

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

        serializer = AddTwoNumberSerializer(data=data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            # now let's add the  numbers
            result = number1 + number2
            return JsonResponse({'result': result})

        print("ERROR IS -->", serializer.errors)
        # if not then return error        
        return JsonResponse({'error': 'Something went wrong!' }, status=400)
