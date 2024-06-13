# Clase base futbolista
class futbolista:
    # Constructor de la clase base
    def __init__(self, atribut, edat):
        self.atribut = atribut  # Atributo que puede representar alguna característica del futbolista
        self.edat = edat  # Edad del futbolista

    def numero(self):
        pass  # Método que se sobrescribirá en las subclases para mostrar el número del futbolista

    def equipo(self):
        pass  # Método que se sobrescribirá en las subclases para mostrar el equipo del futbolista

    def quiensoy(self):
        print("Soy futbolista!!")  # Método que se puede sobrescribir en las subclases para mostrar quién es el futbolista

# Clase Modric que hereda de futbolista
class Modric(futbolista):
    def numero(self):
        print("Llevo el numero 10")  # Implementación específica para el número de Modric

    def equipo(self):
        print("Juego en el Real Madrid")  # Implementación específica para el equipo de Modric

    def quiensoy(self):
        print("Soy Luka Modric!!")  # Implementación específica para la identificación de Modric

# Clase Isco que hereda de futbolista
class Isco(futbolista):
    def numero(self):
        print("Llevo el numero 22")  # Implementación específica para el número de Isco

    def equipo(self):
        print("Juego en el Betis")  # Implementación específica para el equipo de Isco

    def quiensoy(self):
        print("Soy Isco!!")  # Implementación específica para la identificación de Isco

# Clase Cristiano que hereda de futbolista
class Cristiano(futbolista):
    def numero(self):
        print("Llevo el numero 7")  # Implementación específica para el número de Cristiano

    def equipo(self):
        print("Juego en el Al-Nassr")  # Implementación específica para el equipo de Cristiano

    def celebracion(self):
        print("SIUUUUU")  # Método adicional específico de Cristiano para mostrar su celebración

    def quiensoy(self):
        print("Soy El Bicho!!")  # Implementación específica para la identificación de Cristiano

# Clase Aspas que hereda de futbolista
class Aspas(futbolista):
    def numero(self):
        print("Llevo el numero 10")  # Implementación específica para el número de Aspas

    def equipo(self):
        print("Juego en el Celta de Vigo")  # Implementación específica para el equipo de Aspas

    def quiensoy(self):
        print("Soy Iago Aspas!!")  # Implementación específica para la identificación de Aspas

# Clase Halaand que hereda de futbolista
class Halaand(futbolista):
    def numero(self):
        print("Llevo el numero 9")  # Implementación específica para el número de Halaand

    def equipo(self):
        print("Juego en el Manchester City")  # Implementación específica para el equipo de Halaand

    def quiensoy(self):
        print("Soy Erling Haaland!!")  # Implementación específica para la identificación de Halaand

# Clase Kroos que hereda de futbolista
class Kroos(futbolista):
    def numero(self):
        print("Llevo el numero 8")  # Implementación específica para el número de Kroos

    def equipo(self):
        print("Juego en el Real Madrid")  # Implementación específica para el equipo de Kroos

    def quiensoy(self):
        print("Soy Toni Kroos!!")  # Implementación específica para la identificación de Kroos

# Clase Messi que hereda de futbolista
class Messi(futbolista):
    def numero(self):
        print("Llevo el numero 10")  # Implementación específica para el número de Messi

    def equipo(self):
        print("Juego en el Inter de Miami")  # Implementación específica para el equipo de Messi

    def quiensoy(self):
        print("Soy Lionel Messi!!")  # Implementación específica para la identificación de Messi

# Función principal para mostrar la información de los futbolistas
def PP_Ex4():
    # Lista de instancias de futbolistas
    a = [
        Modric("38", 1),
        Isco("32", 1),
        Cristiano("39", 1),
        Aspas("37", 1),
        Halaand("23", 1),
        Kroos("34", 1),
        Messi("36", 1)
    ]
    
    for e in a:  # Iterar sobre cada futbolista
        e.numero()  # Mostrar su número
        e.equipo()  # Mostrar su equipo
        e.quiensoy()  # Mostrar su identificación
        print()  # Imprimir una línea en blanco para separar cada futbolista
