
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .serializers import AddTwoNumberSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

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




# # FOR GLOBAL USE
# from rest_framework.decorators import render_classes,
# @render_classes ([JSONParser])

# passing list of methods
@api_view (['GET', 'POST'])
def add_two_numbers_in_rest(request):
    if request.method == 'GET':
        return Response({'messgae': 'adding two numbers'})
    
    elif request.method == 'POST':
        serializer = AddTwoNumberSerializer(data=request.data)
        # if serializer.is_valid():
        #     number1 = serializer.validated_data['number1']
        #     number2 = serializer.validated_data['number2']
        #     # now let's add the  numbers
        #     result = number1 + number2
        #     return Response({'result': result})

        # print("ERROR IS -->", serializer.errors)
        # # if not then return error        
        # return Response(serializer.errors, status=400)

        serializer.is_valid(raise_exception=True)
        number1 = serializer.validated_data['number1']
        number2 = serializer.validated_data['number2']
        # now let's add the  numbers
        result = number1 + number2
        return Response({'result': result})



@api_view(['GET'])
def info_view(request):
    if request.method == 'GET':
        from .models import Info
        from .serializers import InfoSerializer
        qs = Info.objects.all()

        return Response({'msg': 'ok'})
