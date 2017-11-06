from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.mascota.forms import MascotaForm, VacunaForm
from apps.mascota.models import Mascota, Vacuna
from django.views.generic import ListView
# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascotas_list')
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form': form})

def vacuna_view(request):
    if request.method == 'POST':
        form = VacunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mascota:mascotas_list')
    else:
        form = VacunaForm()
    return render(request, 'mascota/vacuna_form.html', {'form': form})


def mascotas_list(request):
    mascota_l = Mascota.objects.all().order_by('id')
    paginator = Paginator(mascota_l, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        mascota = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mascota = paginator.page(1)
    except EmptyPage:

        mascota = paginator.page(paginator.num_pages)
    contexto = {'mascotas': mascota}
    return render(request, 'mascota/mascotas_list.html', contexto)

def vacuna_list(request):
    vacuna= Vacuna.objects.all().order_by('id')
    contexto = {'vacunas': vacuna}
    return render(request, 'mascota/vacuna_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id= id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascotas_list')
    return render(request, "mascota/mascota_form.html", {'form': form})

def mascota_detalle(request,id_mascota):
    mascota = Mascota.objects.get(id= id_mascota)
    return render( request, "mascota/mascota_det.html", {'mascota': mascota})


def vacuna_edit(request, id_vacuna):
    vacuna = Vacuna.objects.get(id= id_vacuna)
    if request.method == 'GET':
        form = VacunaForm(instance=vacuna)
    else:
        form = VacunaForm(request.POST, instance=vacuna)
        if form.is_valid():
            form.save()
            return redirect('mascota:vacuna_list')
    return render(request, "mascota/vacuna_form.html", {'form': form})

def delete_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id= id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascotas_list')
    return render(request, "mascota/mascota_delete.html", {'mascota': mascota})

def delete_vacuna(request, id_vacuna):
    vacuna = Vacuna.objects.get(id= id_vacuna)
    if request.method == 'POST':
        vacuna.delete()
        return redirect('mascota:vacuna_list')
    return render(request, "mascota/vacuna_delete.html", {'vacuna': vacuna})

class MascotaList(ListView):
    model=Mascota
    template_name = 'mascota/mascotas_list.html'
