import subprocess

def PP_Ex6():
    try:
        subprocess.run(["python3", "Ex6/SERVER/server6/manage.py", "runserver", "8082"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al iniciar el servidor Django:", e)