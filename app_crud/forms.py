from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio', 'stock']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}), #<input type="text" class="form-control">
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), #<textarea class="form-control" rows="3"></textarea>
            'precio': forms.NumberInput(attrs={'class': 'form-control'}), #<input type="number" class="form-control">
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}), #<input type="number" class="form-control" min="0">
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


        #* TODO VALIDACIONES EXPLICITAS 