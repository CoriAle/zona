from django import forms
from apps.mascota.models import Mascota, Vacuna

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'edad',
            'fecha_rescate',
            'genero',
            'persona',
            'vacuna',
            'imagen',
        ]

        labels = {
            'Nombre',
            'Edad',
            'Fecha de rescate',
            'Género',
            'Adoptante',
            'Vacuna',
            'Foto',
        }

        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'edad': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs = {'class': 'form-control'}),
            'genero': forms.TextInput(attrs = {'class': 'form-control'}),
            'persona': forms.Select(attrs = {'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }

class VacunaForm(forms.ModelForm):

    class Meta:
        model = Vacuna

        fields = [
            'nombre',
            'fecha_vencimiento' ,
            'funcion',

        ]

        labels = {
            'Nombre',
            'Fecha de caducidad'
            'Indicaciones',

        }

        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha_vencimiento': forms.DateInput(format = ('%d-%m-%Y'), attrs = {'class': 'form-control'}),
            'funcion': forms.Textarea(attrs = {'class': 'form-control'}),
        }
