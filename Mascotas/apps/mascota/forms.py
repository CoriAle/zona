from django import forms
from apps.mascota.models import Mascota
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
        ]

        labels = {
            'Nombre',
            'Edad',
            'Fecha de rescate',
            'Género',
            'Adoptante',
            'Vacuna',
        }

        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'edad': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha_rescate': forms.TextInput(attrs = {'class': 'form-control'}),
            'genero': forms.TextInput(attrs = {'class': 'form-control'}),
            'persona': forms.Select(attrs = {'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }