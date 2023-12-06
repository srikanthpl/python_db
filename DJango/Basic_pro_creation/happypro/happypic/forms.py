from django import forms

from happypic import happypic

class ProductForm(forms.ModelForm):
    class Meta:
        model = happypic
        fields = '__all__'
        