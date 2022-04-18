#from cProfile import label
#from email.policy import default
#from typing_extensions import Required
from django import forms
from django.forms import ModelForm
from .models import ContactFormModel

''' Form without ModelForm

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)
    message = forms.CharField(label="Message", max_length=500, required=True)
    cc_myself = forms.BooleanField(label="Receive a copy?", required=False, initial=True)
'''

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactFormModel
        fields = '__all__'
        labels = {
            "name" : "",
            "email" : "",
            "message" : "",
            "cc_myself" : "Receive a Copy?"
        }
        widgets = {
            "name" : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Name"}),
            "email" : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Email"}),
            "message" : forms.Textarea(attrs = {
                "class" : "form-control", 
                "placeholder" : "Message" , 
                "rows" : "5", 
                "cols" : "100"
            }),
        }