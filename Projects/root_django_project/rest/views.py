
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from .serializers import AddTwoNumberSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Info
from .serializers import InfoSerializer

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
<<<<<<< HEAD
=======




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



@api_view(['GET','POST', 'PUT', 'DELETE'])
# pk only comes for put delete patch method
def info_view(request, pk=None):
    if request.method == 'GET':
        qs = Info.objects.all()
        # id_obj = Info.objects.get(id=1)
        # serializer = InfoSerializer(instance=id_obj)
        # qs = Info.objects.all()
        # result = []
        # for i in qs:
        #     serializer = InfoSerializer(instance=i)
        #     result.append(serializer.data)
        #return Response(result)

        # more shortcut method
        serializer = InfoSerializer(instance=qs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = InfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']
        # obj = Info.objects.create(
        #     name = name,
        #     address = address
        # )

        # from serializers.py 
        serializer.save()
        return Response({'status': 'ok from post method', 'result': serializer.data})

    # patch for partial update 
    # put for full method update
    elif request.method == 'PUT':
        try:
            obj = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'error': 'DoesNotExist'}, status=400)

        #serializer = InfoSerializer(data=request.data)
        # with instance django will know there is obj instance passed 
        serializer = InfoSerializer(data=request.data, instance=obj)
        serializer.is_valid(raise_exception=True)

        # name = serializer.validated_data['name']
        # address = serializer.validated_data['address']
        # obj.name = name
        # obj.address = address
        # obj.save()

        serializer.save()

        return Response({'status': 'ok from patch method!', 'result': serializer.data})
    

    #for deleting
    elif request.method == 'DELETE':
        try:
            obj = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'error': "User Doesnot Exist!"})
        
        obj.delete()
        return Response({'message': 'user deleted'})



>>>>>>> bb1cbd7ffd50b8b8bae39ac8fec06fc86b24ca8e
