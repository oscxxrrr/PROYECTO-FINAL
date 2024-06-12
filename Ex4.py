class futbolista:
    def __init__(self, atribut, edat):
        self.atribut = atribut
        self.edat = edat

    def numero(self):
        pass

    def equipo(self):
        pass

    def quiensoy(self):
        print("Soy futbolista!!")

class Modric(futbolista):
    def numero(self):
        print("Llevo el numero 10")

    def equipo(self):
        print("Juego en el Real Madrid")

    def quiensoy(self):
        print("Soy Luka Modric!!")

class Isco(futbolista):
    def numero(self):
        print("Llevo el numero 22")

    def equipo(self):
        print("Juego en el Betis")

    def quiensoy(self):
        print("Soy Isco!!")

class Cristiano(futbolista):
    def numero(self):
        print("Llevo el numero 7")

    def equipo(self):
        print("Juego en el Al-Nassr")

    def celebracion(self):
        print("SIUUUUU")

    def quiensoy(self):
        print("Soy El Bicho!!")

class Aspas(futbolista):
    def numero(self):
        print("Llevo el numero 10")

    def equipo(self):
        print("Juego en el Celta de Vigo")

    def quiensoy(self):
        print("Soy Iago Aspas!!")

class Halaand(futbolista):
    def numero(self):
        print("Llevo el numero 9")

    def equipo(self):
        print("Juego en el Manchester City")

    def quiensoy(self):
        print("Soy Erling Haaland!!")

class Kroos(futbolista):
    def numero(self):
        print("Llevo el numero 8")

    def equipo(self):
        print("Juego en el Real Madrid")

    def quiensoy(self):
        print("Soy Toni Kroos!!")

class Messi(futbolista):
    def numero(self):
        print("Llevo el numero 10")

    def equipo(self):
        print("Juego en el Inter de Miami")

    def quiensoy(self):
        print("Soy Lionel Messi!!")

def PP_Ex4():
    a = [
        Modric("38", 1),
        Isco("32", 1),
        Cristiano("39", 1),
        Aspas("37", 1),
        Halaand("23", 1),
        Kroos("34", 1),
        Messi("36", 1)
    ]
    
    for e in a:
        e.numero()
        e.equipo()
        e.quiensoy()
        print()
    

