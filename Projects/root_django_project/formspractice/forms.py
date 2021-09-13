
# let's write code for forms 
from django import forms
from .models import FormsModel

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    # name = forms.CharField(max_length=5)

    # validating the form field
    def clean_name(self):
        print("I 'm form ", self.cleaned_data)
        name = self.cleaned_data['name']
        # we can validations or cleanthe name
        return name.lower()


class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name', 'email']

