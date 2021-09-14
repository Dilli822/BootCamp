# Create your views here.
# we use classbased views rather then funciton based views
# for creating complex and scalable views
from django.http.response import HttpResponse
from django.shortcuts import render 

from django.views import View
# for rendering the templates types views
from django.views.generic import TemplateView

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
