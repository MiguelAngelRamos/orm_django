from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio.'
            },
            'precio': {
                'required': 'El precio es obligatorio.',
                'invalid': 'Ingrese un número válido para el precio.',
            },
        }