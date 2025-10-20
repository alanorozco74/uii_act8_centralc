from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    PUESTOS = [
        ('Chofer', 'Chofer'),
        ('Administrativo', 'Administrativo'),
        ('Gerente', 'Gerente'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Ventas', 'Ventas'),
    ]
    
    id_empleado = models.CharField(max_length=10, unique=True, verbose_name="ID Empleado")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    rfc = models.CharField(max_length=13, verbose_name="RFC")
    puesto = models.CharField(max_length=20, choices=PUESTOS, verbose_name="Puesto")
    fecha_contratacion = models.DateField(verbose_name="Fecha de Contratación")
    
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    
    def __str__(self):
        return f"{self.id_empleado} - {self.nombre} {self.apellido}"