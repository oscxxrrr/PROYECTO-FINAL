from random import randint as ri

def gllista():
    l = []
    for i in range(3):
        l.append(ri(0,10))
    return l

def grespota():
    l = []
    for i in range(3):
        num = int(input("Introduce 3 números para intentar adivinarlos: "))
        l.append(num)    
    return l         

def comparar(l,m):                        
    a = [0,0,0]
    for i in range(3):
        if l[i] == m[i]:
            a[i] = 10
    if a[0] == 10 and a[1] == 10 and a[2] == 10:
        print("Has adivinado los numeros, enhorabuena.")
        return 0
    for i in range(3):
        if a[i] == 0:
            if m[i] in l:
                a[i] = 5
    for i in range(3):
        if a[i] == 10:
            print("El numero {} es correcto".format(m[i]))
        elif a[i] == 5:
            print("El numero {} existe pero no en la posicion que toca".format(m[i]))
        else:
            print("El numero {} no existe".format(m[i]))
        
def PP_ex1():
    op = 1
    l = gllista()
    while op!=0:
        m = grespota()
        op = comparar(l, m)
    