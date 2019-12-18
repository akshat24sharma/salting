from django import forms 
from .models import salting 

class saltingform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

