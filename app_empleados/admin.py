from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'apellido', 'rfc', 'puesto', 'fecha_contratacion')
    list_filter = ('puesto',)
    search_fields = ('id_empleado', 'nombre', 'apellido')