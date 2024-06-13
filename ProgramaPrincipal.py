import Ex1
import Ex2
import Ex3
import Ex4
import Ex5
import Ex6

def menu_principal():
    opcio = 0 
    while opcio < 1 or opcio > 7:
        print("""
            Menu Principal:
            1. Llistes y numeros aleatoris.
            2. Fitxers
            3. Juego
            4. Objetos, clase, herencia...
            5. Scrapping
            6. Server web
            7. Salir
        """)
        opcio = int(input("Selecciona la opcio que vulguis: "))
        if opcio < 1 or opcio > 7:
            print("Opcio no valida")
        else:
            return opcio
        
# Programa Principal
op = 1
while op != 7:
    op = menu_principal()
    if op == 1:
        Ex1.PP_ex1()
    elif op == 2: 
        Ex2.PP_Ex2()
    elif op == 3:
        Ex3.PP_Ex3()
    elif op == 4: 
        Ex4.PP_Ex4()
    elif op == 5:
        Ex5.PP_Ex5()
    elif op == 6:
        Ex6.PP_Ex6() 
    elif op == 7:
        print("Gracias por usar mi proyecto final, hasta la proxima :)")
    else:
        print("Opcio no valida")
