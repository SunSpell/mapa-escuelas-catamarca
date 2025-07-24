import pandas as pd
from escuelas.models import Escuela

def convertir_float(valor):
    if isinstance(valor, str):
        return float(valor.replace(',', '.'))
    return valor

def run():
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
