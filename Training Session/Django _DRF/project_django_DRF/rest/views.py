
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

        print(serializer.errors)
        return JsonResponse({'error': 'Something went wrong'},status=400)

####################################################################

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def add_two_numbers_in_rest(request):
    if request.method == 'GET':
        return Response({'message': 'Welcome to add two numbers'})


    elif request.method == 'POST':
        data = request.data

        #deserializing
        serializer = AddTwoNumbersSerializer(data=data)

        # serializer = AddTwoNumbersSerializer(data=data)
        # if serializer.is_valid():
        #     number1 = serializer.validated_data['number1']
        #     number2 = serializer.validated_data['number2']
            
        #     # now we add the numbers
        #     result = number1 + number2
        #     return Response({'result': result})

        # print(serializer.errors)
        # return Response(serializer.errors, status=400)
        # # return Response({'error': 'Something went wrong'},status=400)



        serializer.is_valid(raise_exception=True)
        number1 = serializer.validated_data['number1']
        number2 = serializer.validated_data['number2']
        # now we add the numbers
        result = number1 + number2
        return Response({'result': result})