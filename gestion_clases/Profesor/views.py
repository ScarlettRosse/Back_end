from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Profesor
from Clase.models import Clase


def agregar_profe(request):
    Profe = Profesor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombreP')
        especialidad = request.POST.get('especialidad')
        clases_id = request.POST.get('claseImpartidas')
        clases_impartidas = clases_id.objects.get(id=clases_id) if clases_id  else None
        Profesor.objects.create(nombre=nombre, especialidad=especialidad, clases_impartidas=clases_impartidas)
        return redirect( 'listarP')
    return render(request, 'crear_profe.html', {'Profe':Profe})


def listar_profe(request):
    Profe = Profesor.objects.select_related('Clase').all()
    paginator = Paginator(Profe, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'Listar_profesores.html', {'Profe':Profe})

def actualizar_profe(request, id):
    Profe = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        Profe.Profesor = request.POST.get('nombreP') 
        Profe.especialidad = request.POST.get('especialidad')
        clases_id = request.POST.get('claseImpartidas')
        clases_impartidas = clases_id.objects.get(id=clases_id) if clases_id  else None
        Profe.clases_impartidas = clases_impartidas
        Profe.save()
        return redirect('listarP')
    return render(request, 'actualizar_prof.html', {'Profe':Profe})

def eliminar_profe(request, id):
    Profe = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        Profe.delete()
        return redirect('listarP')
    return render(request, 'eliminar_prof', {'Profe':Profe})