from django.shortcuts import render


def forms_home(request):
    return render(request, 'djangoforms/forms.html', {})
