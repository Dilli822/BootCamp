
from django.http import HttpResponse

from django.template import loader

from django.shortcuts import  render

def blog_template(request):
    template = loader.get_template('blog.html')
    context = {
        'name': 'hangko',
        'age': 15
    }
    template_data = template.render(context, request)
    return HttpResponse(template_data)


# now we use shortcut method for it

def contact_template(request):
    context = {
        'name': 'dilli hang rai',
        'age': 22
    }
    return render(request, "contact.html", context)

# here we have similar so we make new
# base.html which will be dynamic templates
# that serves as main skeleton templates
# for other child templates

def services_template(request):
    context = {
        'name': 'services',
        'type': 'blog',
        'version': 1.0,
    }
    return render(request, "services.html", context)

