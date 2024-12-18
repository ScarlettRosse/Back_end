from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Estudiante
from Clases.models import Clases


def agregar_estudiante(request):
    Estu = Estudiante.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombreE')
        correo = request.POST.get('correo')
        clases_inscritas = request.POST.get('claseInscritas')
        Profesor.objects.create(nombre=nombre, correo=correo, clases_inscritas=clases_inscritas)
        return redirect( 'listarE')
    return render(request, 'crear_estudiante.html', {'Estu':Estu})


def listar_estudiante(request):
    Estu = Estudiante.objects.all()
    paginator = Paginator(Estu, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'listar_estudiantes.html', {'Estu':Estu})

def actualizar_Estudiante(request, id):
    Estu = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        Estu.nombre = request.POST.get('nombreE')
        Estu.correo = request.POST.get('correo')
        Estu.clases_inscritas = request.POST.get('claseInscritas')
        Estu.save()
        return redirect('listarE')
    return render(request, 'actualizar_estudiante.html', {'Estu':Estu})

def eliminar_estudiante(request, id):
    Estu = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        Estu.delete()
        return redirect('listarE')
    return render(request, 'eliminar_estudiante.html', {'Estu':Estu})
