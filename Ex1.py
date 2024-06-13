from random import randint as ri  # Importa la función randint de la biblioteca random y la renombra como ri

def gllista():  # Define una función llamada gllista
    l = []  # Crea una lista vacía
    for i in range(3):  # Repite el siguiente bloque 3 veces
        l.append(ri(0, 10))  # Agrega un número aleatorio entre 0 y 10 a la lista
    return l  # Devuelve la lista generada

def grespota():  # Define una función llamada grespota
    l = []  # Crea una lista vacía
    for i in range(3):  # Repite el siguiente bloque 3 veces
        num = int(input("Introduce 3 números para intentar adivinarlos: "))  # Solicita al usuario que introduzca un número
        l.append(num)  # Agrega el número introducido a la lista
    return l  # Devuelve la lista generada

def comparar(l, m):  # Define una función llamada comparar que recibe dos listas como parámetros
    a = [0, 0, 0]  # Crea una lista con tres ceros
    for i in range(3):  # Repite el siguiente bloque 3 veces
        if l[i] == m[i]:  # Si el elemento en la posición i de ambas listas es igual
            a[i] = 10  # Establece el valor en la posición i de la lista a a 10
    if a[0] == 10 and a[1] == 10 and a[2] == 10:  # Si todos los valores en la lista a son 10
        print("Has adivinado los numeros, enhorabuena.")  # Imprime un mensaje de éxito
        return 0  # Devuelve 0 para indicar que el juego ha terminado
    for i in range(3):  # Repite el siguiente bloque 3 veces
        if a[i] == 0:  # Si el valor en la posición i de la lista a es 0
            if m[i] in l:  # Si el número en la posición i de la lista m está en la lista l
                a[i] = 5  # Establece el valor en la posición i de la lista a a 5
    for i in range(3):  # Repite el siguiente bloque 3 veces
        if a[i] == 10:  # Si el valor en la posición i de la lista a es 10
            print("El numero {} es correcto".format(m[i]))  # Imprime que el número es correcto
        elif a[i] == 5:  # Si el valor en la posición i de la lista a es 5
            print("El numero {} existe pero no en la posicion que toca".format(m[i]))  # Imprime que el número existe pero está en la posición incorrecta
        else:  # Si el valor en la posición i de la lista a es 0
            print("El numero {} no existe".format(m[i]))  # Imprime que el número no existe

def PP_ex1():  # Define una función llamada PP_ex1
    op = 1  # Inicializa una variable op con el valor 1
    l = gllista()  # Genera una lista aleatoria llamando a la función gllista
    while op != 0:  # Mientras op no sea igual a 0
        m = grespota()  # Solicita al usuario que introduzca una lista de números llamando a la función grespota
        op = comparar(l, m)  # Compara la lista generada y la lista introducida por el usuario
