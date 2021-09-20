from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView

from .forms import StatusMessageModelForm 

from django.contrib.auth.decorators import login_required
#we cannot use decoratos directly to dispatch so we import
from django.utils.decorators import method_decorator


# this one is shortcut method with which part need to login_required
@method_decorator(login_required, name="dispatch")
class StatusMessageCreateView(CreateView):
    form_class = StatusMessageModelForm
    template_name = 'statusapp/create.html'
    success_url = '/accounts/profile-view/'

    # this will make user to log in with usename and pasword
    # but due to some missing links this will not work here
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    

