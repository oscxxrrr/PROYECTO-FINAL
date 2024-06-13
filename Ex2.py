# Archivo donde se almacenarán los contactos
ARCHIVO_CONTACTOS = 'contactos.txt'

# Función para añadir un contacto
def añadir_contacto():
    nombre = input("Ingrese el nombre del contacto: ")  # Solicita el nombre del contacto
    telefono = input("Ingrese el número de teléfono: ")  # Solicita el número de teléfono del contacto
    with open(ARCHIVO_CONTACTOS, 'a') as archivo:  # Abre el archivo de contactos en modo append
        archivo.write(f'{nombre},{telefono}\n')  # Escribe el nombre y teléfono en el archivo, separados por una coma
    print("Contacto añadido exitosamente.\n")  # Informa al usuario que el contacto ha sido añadido

# Función para mostrar todos los contactos
def mostrar_contactos():
    print("Lista de Contactos:")  # Imprime el encabezado de la lista de contactos
    try:
        with open(ARCHIVO_CONTACTOS, 'r') as archivo:  # Abre el archivo de contactos en modo lectura
            for linea in archivo:  # Itera sobre cada línea del archivo
                nombre, telefono = linea.strip().split(',')  # Separa el nombre y el teléfono de cada línea
                print(f"Nombre: {nombre}, Teléfono: {telefono}")  # Imprime el nombre y el teléfono
    except FileNotFoundError:  # Maneja el error si el archivo no existe
        print("No hay contactos aún.\n")  # Informa al usuario que no hay contactos

# Función para borrar un contacto
def borrar_contacto():
    nombre_borrar = input("Ingrese el nombre del contacto que desea borrar: ")  # Solicita el nombre del contacto a borrar
    contactos = []  # Inicializa una lista para almacenar los contactos
    borrado = False  # Inicializa una bandera para verificar si se ha borrado un contacto
    try:
        with open(ARCHIVO_CONTACTOS, 'r') as archivo:  # Abre el archivo de contactos en modo lectura
            for linea in archivo:  # Itera sobre cada línea del archivo
                nombre, telefono = linea.strip().split(',')  # Separa el nombre y el teléfono de cada línea
                if nombre != nombre_borrar:  # Si el nombre no coincide con el nombre a borrar
                    contactos.append(linea)  # Agrega la línea completa a la lista de contactos
                else:
                    borrado = True  # Cambia la bandera a True si se encuentra el contacto a borrar
        if borrado:  # Si se ha encontrado y borrado el contacto
            with open(ARCHIVO_CONTACTOS, 'w') as archivo:  # Abre el archivo de contactos en modo escritura
                archivo.writelines(contactos)  # Escribe todas las líneas excepto la borrada
            print("Contacto borrado exitosamente.\n")  # Informa al usuario que el contacto ha sido borrado
        else:  # Si no se encuentra el contacto a borrar
            print("Contacto no encontrado.\n")  # Informa al usuario que no se ha encontrado el contacto
    except FileNotFoundError:  # Maneja el error si el archivo no existe
        print("No hay contactos aún.\n")  # Informa al usuario que no hay contactos

# Función principal del menú
def PP_Ex2():
    while True:  # Bucle infinito para mostrar el menú
        print("Agenda de Contactos")  # Imprime el título del menú
        print("1. Mostrar contactos")  # Opción para mostrar contactos
        print("2. Añadir contacto")  # Opción para añadir un contacto
        print("3. Borrar contacto")  # Opción para borrar un contacto
        print("4. Salir")  # Opción para salir del programa
        
        opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción
        
        if opcion == '1':  # Si la opción es 1
            mostrar_contactos()  # Llama a la función para mostrar contactos
        elif opcion == '2':  # Si la opción es 2
            añadir_contacto()  # Llama a la función para añadir un contacto
        elif opcion == '3':  # Si la opción es 3
            borrar_contacto()  # Llama a la función para borrar un contacto
        elif opcion == '4':  # Si la opción es 4
            print("Saliendo de la agenda de contactos.")  # Informa al usuario que se está saliendo del programa
            break  # Rompe el bucle para salir del programa
        else:  # Si la opción no es válida
            print("Opción no válida. Por favor, intente de nuevo.\n")  # Informa al usuario que la opción no es válida
