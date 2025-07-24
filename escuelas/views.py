from django.shortcuts import render
from .models import Escuela

def mapa_escuelas(request):
    escuelas = Escuela.objects.all()

    niveles = Escuela.objects.order_by('nivel').values_list('nivel', flat=True).distinct()
    localidades = Escuela.objects.order_by('localidad').values_list('localidad', flat=True).distinct()

    return render(request, 'escuelas/mapa.html', {
        'escuelas': escuelas,
        'niveles': niveles,
        'localidades': localidades,
    })
