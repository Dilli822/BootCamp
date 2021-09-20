from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView

from .forms import StatusMessageModelForm
class StatusMessageCreateView(CreateView):
    form_class = StatusMessageModelForm
    template_name = 'statusapp/create.html'
    success_url = '/accounts/profile-view/'

    

