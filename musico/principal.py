import random
import abc

   
class instrumentos(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def __afinar__(self):
        pass

    @abc.abstractmethod    
    def __tocar__(self):
        pass

    @abc.abstractmethod    
    def __tocar__(self, nota):
        pass


        


class Persona:

    def __setNombre__(self, nombre):
        self.nombre = nombre

    def __presentar__(self):
        print("Hola mi nombre es " + self.nombre)

    


class Musico(Persona):

    def __tocar__(self, i):
        i.__afinar__()
        i.__tocar__()
        i.__tocara__("Do")

    
        

    

class Violin(instrumentos):

    def __afinar__(self):
        print("Afinando Violin")
    
    def __tocar__(self):
        print("Tocando Violin")

    def __tocara__(self, nota):
        print("Tocando Violin en " + nota)    

class Bajo(instrumentos):

    def __afinar__(self):
        print("Afinando Bajo")
    
    def __tocar__(self):
        print("Tocando Bajo")
        
    def __tocara__(self, nota):
        print("Tocando Bajo en " + nota)    
    

class Guitarra(instrumentos):

    def __afinar__(self):
        print("Afinando guitarra")
    
    def __tocar__(self):
        print("Tocando Guitarra")

    def __tocara__(self, nota):
        print("Tocando Guitarra en " + nota)

class Banda:
    def __init__(self):
        self.musicos = []
    
    def __agregarMusico__(self, nombre):
        self.m = Musico()
        self.m.__setNombre__(nombre)
        self.musicos.append(self.m)

    def __generarInstrumento__(self):
        opc = random.randint(1,3)
        if (opc == 1) :
            return Guitarra()
        if (opc == 2):
            return Bajo()
        if (opc == 3):
            return Violin()
        return instrumentos
    
    def __presentarBanda__(self):
        for Musico in self.musicos:
            Musico.__presentar__()
            Musico.__tocar__(self.__generarInstrumento__())
         

b = Banda()
b.__agregarMusico__("Juan")
b.__agregarMusico__("Maria")
b.__agregarMusico__("Miguel")

b.__presentarBanda__()
    