import subprocess  # Importa el módulo subprocess para ejecutar comandos del sistema

def PP_Ex6():
    try:
        # Ejecuta el comando para iniciar el servidor Django
        subprocess.run(
            ["python3", "Ex6/SERVER/server6/manage.py", "runserver", "8082"],  # Comando a ejecutar
            check=True  # Si el comando falla, lanzará una excepción
        )
    except subprocess.CalledProcessError as e:  # Captura errores específicos del comando
        print("Error al iniciar el servidor Django:", e)  # Imprime el mensaje de error
