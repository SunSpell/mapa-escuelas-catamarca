from django.apps import AppConfig


class EscuelasConfig(AppConfig):
    """
    Configuración de la aplicación 'escuelas'.

    Esta clase define la configuración para la aplicación Django 'escuelas',
    incluyendo el tipo de campo de autoincremento por defecto y el nombre
    de la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'escuelas'
