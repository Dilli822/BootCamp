# we imported function loader and HttpResponse
from django.http import HttpResponse

from django.template import loader

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def hello_templates(request):
    template = loader.get_template('hello.html')
    context = {
        'name': 'dilli hang'
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)

# def hello_render(request):
#     context = {
#         'name': 'Dilli Hang rai'
#     }
#     return render(request, "hello.html", context)
# we have return render because render is also doing
# all the required necessary things
# def render(request, template_name, context=None, content_type=None, status=None, using=None)
           # content = loader.render_to_string(template_name, context, request, using=using)
           # return HttpResponse(content, content_type, status)
# def redirect(to, *args, permanent=False, **kwargs):
        #redner()
def hello_render(request):
    context = {
        'name': 'Dilli Hang rai'
    }
    return render(request, "hello_render.html", context)