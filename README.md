# Mapa de Escuelas - Catamarca

Este proyecto es una aplicación web desarrollada con Django que muestra un mapa interactivo de las escuelas de la provincia de Catamarca, Argentina. Permite a los usuarios visualizar la ubicación de las escuelas, obtener información detallada de cada una y filtrarlas por nivel educativo y localidad.

## Características

-   **Mapa Interactivo**: Muestra todas las escuelas en un mapa utilizando Leaflet.js.
-   **Información Detallada**: Al hacer clic en una escuela, se muestra su nombre, domicilio, director/a y más.
-   **Filtros Dinámicos**: Permite filtrar las escuelas por:
    -   Nombre de la escuela o director/a.
    -   Nivel educativo.
    -   Localidad.
-   **Carga de Datos**: Incluye un script para cargar los datos de las escuelas desde un archivo Excel.

## Requisitos

-   Python 3.8 o superior
-   Django
-   pandas
-   openpyxl

## Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/mapa-escuelas-catamarca.git
    cd mapa-escuelas-catamarca
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar las dependencias:**

    No se proporciona un archivo `requirements.txt`, pero puedes instalar las dependencias necesarias manualmente:

    ```bash
    pip install django pandas openpyxl
    ```

4.  **Aplicar las migraciones:**

    ```bash
    python manage.py migrate
    ```

5.  **Cargar los datos de las escuelas:**

    Para poblar la base de datos, ejecuta el siguiente comando. Asegúrate de que el archivo `Mapaeducativo.xlsx` se encuentre en el directorio raíz del proyecto.

    ```bash
    python manage.py shell
    ```

    Dentro del shell de Django, ejecuta el script:

    ```python
    import cargar_escuelas
    cargar_escuelas.run()
    exit()
    ```

## Uso

Una vez completada la instalación y la carga de datos, puedes iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver el mapa de escuelas.

## Estructura del Proyecto

-   `mapaescuelas/`: Directorio principal del proyecto Django.
-   `escuelas/`: Aplicación Django que contiene la lógica principal.
    -   `models.py`: Define el modelo `Escuela`.
    -   `views.py`: Contiene la vista para renderizar el mapa.
    -   `urls.py`: Define las URLs de la aplicación.
    -   `templates/`: Contiene las plantillas HTML.
    -   `admin.py`: Configura la interfaz de administración para el modelo `Escuela`.
    -   `apps.py`: Archivo de configuración de la aplicación.
-   `cargar_escuelas.py`: Script para cargar los datos desde el archivo Excel.
-   `manage.py`: Utilidad de línea de comandos de Django.
-   `Mapaeducativo.xlsx`: Archivo Excel con los datos de las escuelas.
-   `README.md`: Este archivo.
