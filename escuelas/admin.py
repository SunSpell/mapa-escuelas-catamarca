from django.contrib import admin
from .models import Escuela


@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    """
    Configuración del modelo Escuela en el panel de administración de Django.

    Permite que el modelo Escuela sea gestionado a través de la interfaz de
    administración, mostrando campos de solo lectura como 'latitud' y 'longitud'.
    """
    list_display = ('nombre', 'nivel', 'localidad', 'departamento')
    search_fields = ('nombre', 'director', 'localidad', 'departamento')
    list_filter = ('nivel', 'sector', 'modalidad', 'ambito', 'localidad')
    readonly_fields = ('latitud', 'longitud')
