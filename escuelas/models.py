from django.db import models


class Escuela(models.Model):
    """
    Representa una escuela con su información detallada.

    Attributes:
        nombre (str): El nombre de la escuela.
        cue_anexo (str): El CUE Anexo de la escuela.
        nivel (str): El nivel educativo que ofrece la escuela (e.g., Primario, Secundario).
        sector (str): El sector al que pertenece la escuela (e.g., Público, Privado).
        modalidad (str): La modalidad de la escuela (e.g., Común, Especial).
        domicilio (str): La dirección de la escuela.
        ambito (str): El ámbito de la escuela (e.g., Rural, Urbano).
        localidad (str): La localidad donde se encuentra la escuela.
        departamento (str): El departamento donde se encuentra la escuela.
        director (str): El nombre del director o directora de la escuela.
        latitud (float): La latitud de la ubicación de la escuela.
        longitud (float): La longitud de la ubicación de la escuela.
    """
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