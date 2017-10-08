from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

def mascotas_list(request):
    mascota = Mascota.objects.all()
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascotas_list.html', contexto)

def mascota_edit(request, id):
    mascota = Mascota.object.get(id)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascotas_list')
    return render(request, "mascota/mascota_form.html", {'form': form})
