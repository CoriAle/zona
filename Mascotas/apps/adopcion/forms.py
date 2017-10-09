from django import forms
from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.Modelform):
    class Meta:
        model = Persona
        fields=[
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'correo',
            'direccion',
        ]
        labels = {
                'nombre': 'Nombre',
                'apellidos': 'Apellidos',
                'edad': 'Edad',
                'telefono', 'Teléfono',
                'correo': 'Correo Electrónico',
                'direccion': 'Dirección',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':form-control}),
            'apellidos': forms.TextInput(attrs={'class':form-control}),
            'edad': forms.TextInput(attrs={'class':form-control}),
            'telefono': forms.TextInput(attrs={'class':form-control}),
            'correo': forms.TextInput(attrs={'class':form-control}),
            'direccion': forms.Textarea(attrs={'class':form-control}),
        }
