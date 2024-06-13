#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
# Encabezado que especifica el intérprete a utilizar para ejecutar el script.
# Aquí se utiliza Python 3.

import os
import sys
# Importa los módulos necesarios para manejar variables de entorno y argumentos de línea de comandos.

def main():
    """Run administrative tasks."""
    # Define la función principal que ejecuta las tareas administrativas de Django.
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    # Configura la variable de entorno 'DJANGO_SETTINGS_MODULE' para apuntar al archivo de configuración del proyecto Django.
    
    try:
        from django.core.management import execute_from_command_line
        # Intenta importar la función 'execute_from_command_line' de Django, que se usa para ejecutar comandos desde la línea de comandos.
    except ImportError as exc:
        # Si la importación falla, captura la excepción y muestra un mensaje de error detallado.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
            # Mensaje de error que sugiere posibles causas y soluciones.
        ) from exc
    
    execute_from_command_line(sys.argv)
    # Llama a 'execute_from_command_line' pasando los argumentos de la línea de comandos para ejecutar el comando especificado.

if __name__ == '__main__':
    main()
    # Verifica si el script se está ejecutando directamente y, si es así, llama a la función 'main'.
