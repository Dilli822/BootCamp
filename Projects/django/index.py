
# from django.core.exceptions import ValidationError
# from django.http import HttpResponse
# from .forms import MyForm


# # Let's assume: URL /send/ points to this view func
# def send(request):
#     # this func will allow both GET and POST to land here
#     # so we might need to add some Validations


#     form = MyForm(request.POST)
#     if form.is_valid():
#         # process the data in form.cleaned_data as required
    
#     else:
#         return HttpResponse('Error')



# from django import forms

# class MyForm(froms.Form):
#     super().clean()
#     name = self.cleaned_data.get("name")
#     email = self.cleaned_data.get("email")


#     if email and not name:
#         raise forms.validateError(
#             "Name is required when email is provided"
#         )

# from django import forms

# class MyForm(forms.Form):
#     ...

#     def clean_name(self):
#         data = self.cleaned_data['name']
#         if len(data) > 100:
#             raise forms.ValidationError("Your name is really long")

        
#         # Always return a value to use as the new cleaned data, even if
#         # this method didn't change it

#         #Note: this method can change the data value
#         # That's why you can transform your value or validate them here
#         # eg: data = 'Ram Bahadur '
#         return data


# from django.db import models

# class MyModel(models.Mode):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=200)



# from django import forms
# from .models import MyModel

# class MyForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ['name', 'email']