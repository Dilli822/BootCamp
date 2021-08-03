# we imported function loader and HttpResponse
from django.http import HttpResponse

from django.template import loader


def hello_templates(request):
    template = loader.get_template('hello.html')
    context = {}
    template_data = template.render(context, request)
    return HttpResponse(template_data)
