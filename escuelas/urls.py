from django.urls import path
from .views import mapa_escuelas

urlpatterns = [
    path('', mapa_escuelas, name='mapa_escuelas'),
]
