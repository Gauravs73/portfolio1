from django import forms

# creating a form
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)


    message = forms.CharField(max_length=500)
