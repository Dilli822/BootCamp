

# ccv.co.uk site for more details
from django.views.generic import CreateView

from .forms import UserInfoModelForm

class Create(CreateView):
   # we need form 
   form_class = UserInfoModelForm
   template_name = 'classbased/create.html'



# after submitting the form
# user's submitted form is stored in db classbased_userinfo
# but with redirection of success url we will face
# NO URL to redirect ---> error 


   
