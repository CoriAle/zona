from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import RegistroForm
# Create your views here.

def RegistroUsuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascotas_list')
    else:
        form = RegistroForm()
    return render(request, 'usuario/registrar.html', {'form': form})
