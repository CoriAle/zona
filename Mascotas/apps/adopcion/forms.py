from django import forms
from apps.adopcion.models import Persona, Solicitud

<<<<<<< HEAD
class PersonaForm(forms.ModelForm):
=======
class PersonaForm(forms.Modelform):
>>>>>>> origin/master
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
<<<<<<< HEAD
                'telefono': 'Teléfono',
=======
                'telefono', 'Teléfono',
>>>>>>> origin/master
                'correo': 'Correo Electrónico',
                'direccion': 'Dirección',
        }
        widgets = {
<<<<<<< HEAD
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
        }
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields =[
            'numero_mascotas',
            'razon',
        ]
        labels = {
            'numero_mascotas': 'Número de Mascotas',
            'razon': 'Razones para adoptar',
        }
        widgets = {
            '.numero_mascotas': forms.TextInput(attrs={'class':'form-control'}),
            'razon': forms.Textarea(attrs={'class':'form-control'}),
=======
            'nombre': forms.TextInput(attrs={'class':form-control}),
            'apellidos': forms.TextInput(attrs={'class':form-control}),
            'edad': forms.TextInput(attrs={'class':form-control}),
            'telefono': forms.TextInput(attrs={'class':form-control}),
            'correo': forms.TextInput(attrs={'class':form-control}),
            'direccion': forms.Textarea(attrs={'class':form-control}),
>>>>>>> origin/master
        }
