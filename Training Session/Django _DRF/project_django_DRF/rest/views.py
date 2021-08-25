
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers

from rest_framework.parsers import JSONParser

from .serializers import AddTwoNumbersSerializer


@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Welcome to add two numbers'})


    elif request.method == 'POST':
        data = JSONParser().parse(request)

        print("request.POST--->", request.POST)
        print("data--->", data)

        #deserializing
        serializer = AddTwoNumbersSerializer(data=data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            
            # now we add the numbers
            result = number1 + number2
            return JsonResponse({'result': result})
        return JsonResponse({'error': 'Something went wrong'})

