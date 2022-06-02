import filecmp
import mimetypes
import os

from wsgiref.util import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rhpositivooo import settings
from .models import *
from .forms import EvaluarProspecto, NuevoProspecto


def inicio(request):
    return render(request, 'prospectos/index.html')

def prospectos(request):
    prospectos = Prospecto.objects.all()
    return render(request, 'prospectos/prospectos.html', {'prospectos': prospectos})

def nuevoProspecto(request):

    form = NuevoProspecto(request.POST, request.FILES)

    if form.is_valid():

        form.save()
        form = NuevoProspecto()
        return redirect('/prospectos')
    else:
        print(form.errors.as_data())

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

def download(request, file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    wrapper = FileWrapper( open( file_path, "r" ) )
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % file_name 
    return response

