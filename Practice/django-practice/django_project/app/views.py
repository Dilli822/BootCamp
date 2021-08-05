
# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("welcome to home section")
def blog(request, name):
    print("welcome to our blog: {}", name)
    return HttpResponse(f"Welcome---- { name }-----to our blog section.")