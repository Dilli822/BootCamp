
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader

def home(request):
    return HttpResponse("Welcome to main page section")

# making dynamic url and request and response


def int_converter(request, int_data):
    result = "congrats on converting the string to integer.You converter the int: {}".format(int_data)
    print(result)
    print(type(result))

    try:
        _ = int(int_data)
    except ValueError:
        return HttpResponse("SOMETHING IS WRONG", status=404)

    return HttpResponse(result)

def users(request, name):
    data = {
        "ram": "ram bahadur",
        "hari": "hari bahdaur",
        "madan": "madan bahadur"
    }
    full_name = data[name]
    print("the requested username is: ", name)
    user_data = f"your name is: { full_name }"
    return HttpResponse(user_data)

def user(request, name2):
    users_name = f"you had requested to our server and your name is: {name2}"
    print("requested user's name is: ", name2)

    return HttpResponse(users_name)





