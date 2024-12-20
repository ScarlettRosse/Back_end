from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Estudiante
from Clase.models import Clase

def agregar_estudiante(request):
    Clas = Clase.objects.all()
    Estu = Estudiante.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombreE')
        correo = request.POST.get('correo')
        clases_id = request.POST.get('clasesInscritas')  
        clases_inscritas = Clase.objects.get(id=clases_id) if clases_id else None
        
        if not nombre or not correo:
            return HttpResponse("Nombre y correo son requeridos", status=400)
        
        if not clases_inscritas:
            return HttpResponse("Clase inscrita es requerida", status=400)
        
        Estudiante.objects.create(nombre=nombre, correo=correo, clases_inscritas=clases_inscritas)
        return redirect('listar_estudiantes')
    return render(request, 'crear_estudiante.html', {'Estu': Estu, 'Clas': Clas})

def listar_estudiante(request):
    Estu = Estudiante.objects.select_related('clases_inscritas').all()
    paginator = Paginator(Estu, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'listar_estudiantes.html', {'Estu':Estu, 'page_obj':page_obj})

def actualizar_Estudiante(request, id):
    Estu = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        Estu.nombre = request.POST.get('nombreE')
        Estu.correo = request.POST.get('correo')
        clases_id = request.POST.get('claseInscritas')
        clases_inscritas = clases_id.objects.get(id=clases_id) if clases_id  else None
        Estu.clases_inscritas = clases_inscritas
        Estu.save()
        return redirect('listarE')
    return render(request, 'actualizar_estudiante.html', {'Estu':Estu})

def eliminar_estudiante(request, id):
    Estu = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        Estu.delete()
        return redirect('listarE')
    return render(request, 'eliminar_estudiante.html', {'Estu':Estu})
