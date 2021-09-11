from django.shortcuts import render

# Create your views here.

def forms_home(request):
    return render(request, 'formspractice/forms.html', {})
