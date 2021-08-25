

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


from rest_framework.parsers import JSONParser


@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Welcome to add two numbers'})


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print("request.POST--->", request.POST)
        print("data--->", data)
        # print(request.POST)

        # now we add the numbers

        result = data['number1'] + data['number2']

        return JsonResponse({'result': result})
        

        # return JsonResponse({'message': 'okay'})