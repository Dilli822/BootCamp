from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

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
    context = {}
    template_data = template.render(context.request)
    return HttpResponse(template_data)