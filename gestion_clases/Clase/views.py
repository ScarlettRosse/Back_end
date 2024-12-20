from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Clase


@login_required
def agregar_clase(request):
    Clas = Clase.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombreC')
        horario = request.POST.get('horario')
        descripcion = request.POST.get('descripcion')
        Clase.objects.create(nombre=nombre, horario=horario, descripcion=descripcion)
        return redirect( 'listar_clases')
    return render(request, 'crear_clase.html', {'Clas':Clas})

@login_required
def listar_clase(request):
    Clas = Clase.objects.all()
    paginator = Paginator(Clas, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'listar_clase.html', {'Clas':Clas, 'page_obj':page_obj})
@login_required
def actualizar_clase(request, id):
    Clas = get_object_or_404(Clase, id=id)
    if request.method == 'POST':
        Clas.nombre = request.POST.get('nombreC')
        Clas.horario = request.POST.get('horario')
        Clas. descripcion = request.POST.get('descripcion')
        Clas.save()
        return redirect('listar_clases')
    return render(request, 'actualizar.html', {'Clas':Clas})
@login_required
def eliminar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    if request.method == 'POST':
        clase.delete()
        return redirect('listar_clases')
    return render(request, 'eliminar_clase.html', {'clase': clase})