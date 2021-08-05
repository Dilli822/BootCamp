
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home_template(request):
    template = loader.get_template('home.html')
    context = {
        'name': 'dilli hang'
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)


