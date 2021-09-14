

# ccv.co.uk site for more details
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .forms import UserInfoModelForm

from .models import UserInfo
# we use reverse_lazy to load in alazy behaviour so i gets load at last
from django.urls import reverse, reverse_lazy

class Create(CreateView):
   # we need form 
   form_class = UserInfoModelForm
   template_name = 'classbased/create.html'
   # success url --> # classbased:list
   # #success_url = '/c/list/'
   # using reverse function
   success_url = reverse_lazy('classbased:list')

# this is long method up reverse_lazy function will do same work in a shortcut way
#    def get_success_url(self):
#        return reverse('classbased:list')

# after submitting the form
# user's submitted form is stored in db classbased_userinfo
# but with redirection of success url we will face
# NO URL to redirect ---> error 

# for list view
class List(ListView):
    #attributes and Methods it takes see on ccbv.co.uk or docs
    # we need list as template view
    template_name = 'classbased/list.html'

    # which model list will load
    model = UserInfo

    # on which context it needs to be sent
    # def get_context_object_name() will call the list data
    # see details in the ccbv.co.uk
    # shortcut for queryset and this is default helper method
    context_object_name = 'data'

    # we can even override the quert_set 
    # queryset = UserInfo.objects.all()
    # def get_queryset(self):
    # if we need to do certain specific works or 
    # apply logics then we can override the method and
    # put logics like this
    # if self.request.user.id==1:
    #     return UserInfo.objects.all()
    # else:
    #     return UserInfo.objects.filter(is_active=True)


    # sending extra data
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)



# for details view
class Detail(DetailView):
    # we could give queryset but django handles it
    model = UserInfo
    template_name = 'classbased/details.html'
     # pk overrided to id
    # better to keep pk
    pk_url_kwarg = 'id'

    context_object_name = 'user_obj'

# For update
class Update(UpdateView):
    return()

   

   
