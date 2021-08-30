
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from django.template import loader


def hello_template(request):
    # html_string = """
    # <html>
    # <body>
    #    <h1> hello </h1>
    # </body>
    # </html>
    # """
    template = loader.get_template('hello.html')
    context = {
        'name': 'Ram Bahadur Limbu'
    }

    template_data = template.render(context, request)
    return HttpResponse(template_data)



# shortcut technique or byusing render

def hello_render(request):
    context = {
        'name': 'albert',
    }
    return render(request,"hello.html", context, status=200)