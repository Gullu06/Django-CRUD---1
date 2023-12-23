# myapp/forms.py
from django import forms
from .models import CURD_table

class Userform(forms.ModelForm):
    class Meta:
        model = CURD_table
        fields = ['title', 'description']
