from django.shortcuts import render
from .models import Escuela


def mapa_escuelas(request):
    """
    Renderiza el mapa de escuelas con filtros.

    Esta vista recupera todas las escuelas de la base de datos y también obtiene
    listas de niveles educativos y localidades para usar como filtros en la
    plantilla.

    Args:
        request: El objeto HttpRequest.

    Returns:
        Una respuesta HttpResponse que renderiza la plantilla 'escuelas/mapa.html'
        con los datos de las escuelas, niveles y localidades en el contexto.
    """
    escuelas = Escuela.objects.all()

    niveles = Escuela.objects.order_by('nivel').values_list('nivel', flat=True).distinct()
    localidades = Escuela.objects.order_by('localidad').values_list('localidad', flat=True).distinct()

    return render(request, 'escuelas/mapa.html', {
        'escuelas': escuelas,
        'niveles': niveles,
        'localidades': localidades,
    })
