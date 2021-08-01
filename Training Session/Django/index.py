
#A simple view example
from django.http import HttpResponse, response
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


from django.http import HttpResponse
response = HttpResponse("Here's the text of our webpage and applied one of the HttpResponse Objects method.")
response = HttpResponse("DJano helper content type accept only text", content_type="text/plain")
response = HttpResponse(b'Byteststrings are also accepted.')


#examples
response = HttpResponse()
response.write("<p>Here is additional response.</p>")
# do some calculations here
response.write("<p>Here's another field for you.")

# JsonResponse objects
from django.http import JsonResponse
response = JsonResponse({"name": "dilli"})
response.content
b'{"name": "dilli"}'
response = JsonResponse([1,2,3,4,5], safe=False)