
#A simple view example
from django.http import HttpResponse
import datetime

from django.views.decorators.http import condition

def current_datetime(request):
    now = datetime.datetime()
    html = "<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)

from django.http import HttpResponse, HttpResponseNotFound

def my_view(request):
    
    if condition: #foo or any condition
        return HttpResponseNotFound('<h1>Page Not Found!</h1>')
    else:
        return HttpResponse('<h1> Page was found!</h1>')

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    pass
