# Archivo donde se almacenarán los contactos
ARCHIVO_CONTACTOS = 'contactos.txt'

# Función para añadir un contacto
def añadir_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    with open(ARCHIVO_CONTACTOS, 'a') as archivo:
        archivo.write(f'{nombre},{telefono}\n')
    print("Contacto añadido exitosamente.\n")

# Función para mostrar todos los contactos
def mostrar_contactos():
    print("Lista de Contactos:")
    try:
        with open(ARCHIVO_CONTACTOS, 'r') as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(',')
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
    except FileNotFoundError:
        print("No hay contactos aún.\n")

# Función para borrar un contacto
def borrar_contacto():
    nombre_borrar = input("Ingrese el nombre del contacto que desea borrar: ")
    contactos = []
    borrado = False
    try:
        with open(ARCHIVO_CONTACTOS, 'r') as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(',')
                if nombre != nombre_borrar:
                    contactos.append(linea)  # Agregar la línea completa
                else:
                    borrado = True
        if borrado:
            with open(ARCHIVO_CONTACTOS, 'w') as archivo:
                archivo.writelines(contactos)  # Escribir todas las líneas excepto la borrada
            print("Contacto borrado exitosamente.\n")
        else:
            print("Contacto no encontrado.\n")
    except FileNotFoundError:
        print("No hay contactos aún.\n")

# Función principal del menú
def PP_Ex2():
    while True:
        print("Agenda de Contactos")
        print("1. Mostrar contactos")
        print("2. Añadir contacto")
        print("3. Borrar contacto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_contactos()
        elif opcion == '2':
            añadir_contacto()
        elif opcion == '3':
            borrar_contacto()
        elif opcion == '4':
            print("Saliendo de la agenda de contactos.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.\n")

