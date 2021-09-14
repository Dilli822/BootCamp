# Create your views here.
# we use classbased views rather then funciton based views
# for creating complex and scalable views
from django.http.response import HttpResponse
from django.shortcuts import render 

from django.views import View
# for rendering the templates types views
from django.views.generic import TemplateView, RedirectView

class FirstView(View):
    # for get method--> get()
    # function for get
    
    def get(self,request, *args, **kwargs):
        return HttpResponse("Helllo this is first class based views")


    # for post method --> post()

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is Post function of classbased function!')

    

# we can use inheritance, mixins to create more complex views
# inheriting the templateView
class FirstTemplate(TemplateView):
    template_name = 'classbased/template.html'

    # passing the context in the generic class views
    # for tht we function get_context-data()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context is dictdata type
        context['msg'] = "Hello World"
        return context
        print("context", context)


# for redirect url 
# how does this redirection works 
# webiste cctv.co.uk maybe better for understanding mechanism
# important to know and learn the calls of function and method
class FirstTemplateRedirect(RedirectView):
    url = '/c/template/'

