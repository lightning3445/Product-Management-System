from django import forms
from .models import product

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'proid',
            'name',
            'image',
            'color',
            'size',
            'price',
        ]

        widgets={
            "size":forms.CheckboxSelectMultiple()
        }
        