from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            id_empleado=request.POST['id_empleado'],
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            rfc=request.POST['rfc'],
            puesto=request.POST['puesto'],
            fecha_contratacion=request.POST['fecha_contratacion']
        )
        return redirect('listar_empleados')
    return render(request, 'agregar_empleado.html')

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.id_empleado = request.POST['id_empleado']
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.rfc = request.POST['rfc']
        empleado.puesto = request.POST['puesto']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.save()
        return redirect('listar_empleados')
    return render(request, 'editar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return render(request, 'borrar_empleado.html', {'empleado': empleado})