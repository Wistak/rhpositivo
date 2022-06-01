from cgitb import text
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import *
from django.http import HttpResponse
from .forms import EvaluarProspecto, NuevoProspecto

def inicio(request):
    return render(request, 'prospectos/index.html')

def prospectos(request):
    prospectos = Prospecto.objects.all()
    return render(request, 'prospectos/prospectos.html', {'prospectos': prospectos})

def nuevoProspecto(request):
    form = NuevoProspecto(request.POST)
    print(request.POST)

    if form.is_valid():
        print("valido")
        form.save()
        form = NuevoProspecto()
        return redirect('/prospectos')
    else:
        print(form.errors.as_data()) # here you print errors to terminal

    context = {'form':form}
    return render(request, 'prospectos/nuevo_prospecto.html', context)


def evaluarProspecto (request, pk):
    prospecto = Prospecto.objects.get(id=pk)
    nombre = prospecto.nombre
    apellidos = prospecto.apepat + ' ' + prospecto.apemat
    observaciones = prospecto.observaciones
    form = EvaluarProspecto(instance=prospecto)

    if request.method == 'POST':
        estatus_obj = Estatus.objects.get(id=request.POST['estatus'])
        observaciones_post = request.POST['observaciones']
        form = EvaluarProspecto(request.POST, instance=estatus_obj)
        if form.is_valid():
            Prospecto.objects.filter(pk=pk).update(estatus=estatus_obj, observaciones=observaciones_post)
            return redirect('/prospectos')
    
    estatuses = Estatus.objects.all()

    context = {'form':form, 'estatus': estatuses, 'nombre': nombre, 'apellidos': apellidos, 'observaciones': observaciones}
    return render(request, 'prospectos/evaluar_prospecto.html', context)