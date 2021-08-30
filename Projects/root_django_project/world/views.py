
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse

def home(request):
    return HttpResponse("hello world")


def profile(request,username):

    #printing dynamic name of any user entering in the site
    print("Name is",username)
    

    # let's create a small db type data set
    data = {
        'ram': 'Ram Bahahdur limbu',
        'madan': 'Madan Bahadur',
        'hari': 'Hari Bahadur ',
    }

    # returning f string and returning httpresponse
    # full_name = data[username]
    full_name = data.get(username)

    if not full_name:
        return HttpResponseNotFound("The UserName does not exist", status=400)
    
    string_data = f"Your Full Name is: {full_name}"
    return HttpResponse(string_data)

    # this was static repsonse
    # return HttpResponse("This is a profile section!")

    # this is dynamic httpresponse with dyanmic string name
    # return HttpResponse("Your name is: {}".format(username))


# static example ram profile

def RamProfile(request):
    return HttpResponse("This is Ram's Profile!")



# we are creating a function which returns json reponse
def profile_json(r, username):
    print("profile-json user is--->", username)
    data = {
        'ram': 'Ram Bahahdur limbu',
        'madan': 'Madan Bahadur',
        'hari': 'Hari Bahadur ',
    }
    
    full_name = data.get(username)
    
    if not full_name:
        return HttpResponse("The UserName does not exist", status=400)

    
    dict_data = {
        'full_name': full_name
    }
    # we are returning the jsonreponse not the normal httpresponse
    return JsonResponse(dict_data)


# for integer path converter

def int_converter_view(r, int_data):
    print("This int_data is --->", int_data)
    print(type(int_data))

    # try catcb error
    try:
        #converted_int_data = int(int_data)
        # not used so _ is used
        _ = int(int_data)

    except ValueError:
        return HttpResponse("Semething is wrong", status=404)

    return HttpResponse("Everthing is okay")


# requests attributes
# if httpresponse not returned this error will
# ValueError: The view world.views.debug_request didn't return 
# an HttpResponse object. It returned None instead.

def debug_request(request):
    # this will return req method as GET 

    # we are printing the request method
    # all attributes like
    # Request method: GET

    #http://127.0.0.1:8000/test-path/?name=ram
    # note django url conf will not look param
    # like in the above url it will ignore query name ram 
    # and direct the url to test-path/
    print("Request method:", request.method)
    print("Scheme:", request.scheme)
    print("Headers:", request.headers)
    print("REQUEST GET PARAMETERS:", request.GET)

    return HttpResponse("OK from debug page!")