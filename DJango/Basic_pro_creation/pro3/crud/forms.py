from django import forms
from .models import YourModel

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['name', 'description']
        labels = {
            'name': 'Your Custom Name Label',
            'description': 'Your Custom Description Label',
        }