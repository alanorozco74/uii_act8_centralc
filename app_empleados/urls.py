from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
]