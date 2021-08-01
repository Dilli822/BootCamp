# from django.shortcuts import render

# Create your views here.

# returning a simple hello world 
# returning view with taking req and responsing with view
from django.http import HttpResponse

def home(request):

    #using more feature like adding html string 
    html_content = """
    <html>
    <body>

      <h1>Hello world from django.</h1>
      <p>This is my first web application in django.</p>

    </body>
    </html>
    """
    response = HttpResponse()
    response.content = "Hello world"
    return response
    return HttpResponse(html_content)

