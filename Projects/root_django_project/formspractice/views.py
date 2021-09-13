from django.forms.forms import Form
from formspractice.forms import FormsModelForm, MyForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.

def forms_home(request):
    # applying logics 
    if request.method == 'GET':
        return render(request, 'formspractice/forms.html', {})
    
    else: # post 
        print(request.POST.get('name'))
        return HttpResponse("everyything is okay")


# FORMS WITH POST METHOD MUST HAVE CSRF TOKEN
def django_form(request):
    if request.method == 'GET':
        form = MyForm()
        return render(request, 'formspractice/django_form.html', {'form': form})
    
    else: #post 
        form = MyForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Okay")
        else:
            # return HttpResponse("Something went wrong!")
            # returning the templates which is benefical for s
            # track whats wrong and validaitons 
            return render(request, 'formspractice/django_form.html', {'form': form})



def django_model_form(request):
    if request.method == 'GET':
        # form = MyForm()
        # save method is only possibel if we have modelform
        form = FormsModelForm()
        return render(request, 'formspractice/forms_model.html', {'form': form})
    
    else: # post
        # form = MyForm(request.POST)
        form = FormsModelForm(request.POST)
        if form.is_valid():
            # if only validated then save the form
            form.save()
            print("this is after valiations on view", form.cleaned_data)
            return HttpResponse("Everythins is Okay!Thanks For Registering Your details.")
        else:
            # return HttpResponse("Something went wrong!")
            # returning the templates which is benefical for s
            # track whats wrong and validaitons 
            return render(request, 'formspractice/forms_model.html', {'form': form})



