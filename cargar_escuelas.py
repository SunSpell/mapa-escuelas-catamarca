import pandas as pd
from escuelas.models import Escuela


def convertir_float(valor):
    """
    Convierte un valor a float, manejando comas como separadores decimales.

    Si el valor es una cadena, reemplaza la coma por un punto antes de
    convertirlo a float.

    Args:
        valor: El valor a convertir, puede ser una cadena o un número.

    Returns:
        El valor convertido a float.
    """
    if isinstance(valor, str):
        return float(valor.replace(',', '.'))
    return valor


def run():
    """
    Carga los datos de las escuelas desde un archivo Excel a la base de datos.

    Lee el archivo 'Mapaeducativo.xlsx', itera sobre sus filas y crea un
    objeto Escuela por cada una, guardándolo en la base de datos.
    Imprime un mensaje de error si alguna fila no puede ser procesada.
    """
    df = pd.read_excel('Mapaeducativo.xlsx', engine='openpyxl')

    for _, row in df.iterrows():
        try:
            Escuela.objects.create(
                nombre=row['Localización'],
                cue_anexo=row['CUE-Anexo'],
                nivel=row['Nivel'],
                sector=row['Sector'],
                modalidad=row['Modalidad'],
                domicilio=row['Domicilio'],
                ambito=row['Ambito'],
                localidad=row['Localidad'],
                departamento=row['Departamento'],
                director=row['Director/a'],
                latitud=convertir_float(row['latitud']),
                longitud=convertir_float(row['longitud']),
            )
        except Exception as e:
            print(f"Error en fila {_}: {e}")
