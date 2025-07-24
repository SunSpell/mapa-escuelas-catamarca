from django.db import models

class Escuela(models.Model):
    nombre = models.CharField(max_length=255)
    cue_anexo = models.CharField(max_length=20)
    nivel = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    modalidad = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=255)
    ambito = models.CharField(max_length=50)
    localidad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return self.nombre