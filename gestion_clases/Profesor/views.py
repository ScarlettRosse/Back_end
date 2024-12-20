from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from gestion_clases.form import RegistroForm
from django.http import HttpResponse 
from .models import Profesor
from Clase.models import Clase

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def pagina_principal(request):
    return render(request, 'index.html')
@login_required
def agregar_profe(request):
    Clas = Clase.objects.all()
    Profe = Profesor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombreP')
        especialidad = request.POST.get('especialidad')
        clases_id = request.POST.get('clasesImpartidas')
        clases_impartidas = Clase.objects.get(id=clases_id) if clases_id else None
        
        if not nombre or not especialidad:
            return HttpResponse("Nombre y especialidad son requeridos", status=400)
        
        if not clases_impartidas:
            return HttpResponse("Clase impartida es requerida", status=400)
        
        Profesor.objects.create(nombre=nombre, especialidad=especialidad, clases_impartidas=clases_impartidas)
        return redirect('listar_prof')
    return render(request, 'crear_profe.html', {'Profe': Profe, 'Clas': Clas})
@login_required
def listar_profe(request):
    Profe = Profesor.objects.select_related('clases_impartidas').all()
    paginator = Paginator(Profe, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'listar_profesores.html', {'Profe': Profe, 'page_obj': page_obj})
@login_required
def actualizar_profe(request, id):
    Profe = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        Profe.nombre = request.POST.get('nombreP')
        Profe.especialidad = request.POST.get('especialidad')
        clases_id = request.POST.get('claseImpartidas')
        clases_impartidas = Clase.objects.get(id=clases_id) if clases_id else None
        Profe.clases_impartidas = clases_impartidas
        Profe.save()
        return redirect('listar_profe')
    return render(request, 'actualizar_prof.html', {'Profe': Profe})
@login_required
def eliminar_profe(request, id):
    Profe = get_object_or_404(Profesor, id=id)
    if request.method == 'POST':
        Profe.delete()
        return redirect('listar_prof')
    return render(request, 'eliminar_prof.html', {'Profe':Profe})