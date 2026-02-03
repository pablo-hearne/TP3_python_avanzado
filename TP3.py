"""
                    Ejercicio: Reproductor de Música en POO con Python
    Objetivo:
Implementar un sistema de reproducción de música utilizando Programación Orientada a Objetos. 
Debes evitar el uso de estructuras de control condicional (if, elif, else o match-case) 
para cambiar entre fuentes de reproducción.

    Descripción:
Se debe modelar un reproductor de música que puede reproducir sonido desde diferentes fuentes:

MP3 (por defecto)
CD
Consola

Cada fuente debe tener su propia forma de indicar que está reproduciendo música:

MP3: "Sonando MP3"
CD: "Sonando CD"
Consola: "Sonando Consola"


El reproductor debe tener un método reproducir() que muestre
el mensaje correspondiente según la fuente activa.
Además, debe contar con un método cambiar_fuente(nueva_fuente)
que permita cambiar la fuente de reproducción sin utilizar estructuras condicionales 
(if, elif, else, match-case).

Requisitos Técnicos:

Utilizar el concepto de polimorfismo para evitar el uso de condicionales.
Crear una clase Reproductor con los métodos reproducir() y cambiar_fuente(nueva_fuente).
Crear una clase para cada fuente de sonido (MP3, CD, Consola) con su propia implementación de reproducir().
El programa debe iniciar con la fuente MP3 por defecto.


    Ejemplo de Uso Esperado:
reproductor = Reproductor()  
reproductor.reproducir()  # Salida: "Sonando MP3"

reproductor.cambiar_fuente(CD())  
reproductor.reproducir()  # Salida: "Sonando CD"

reproductor.cambiar_fuente(Consola())  
reproductor.reproducir()  # Salida: "Sonando Consola"
"""



class Types_of_reproductor():
    def __init__(self,origin_of_sound) -> None:
        self.origin_of_sound = origin_of_sound
        pass
    def name_getter(self):
        return self.origin_of_sound

class CD(Types_of_reproductor):
    def __init__(self,origin_of_sound = "CD") -> None:
        self.origin_of_sound = origin_of_sound
        pass
    pass

class MP3(Types_of_reproductor):
    def __init__(self, origin_of_sound = "MP3") -> None:
        self.origin_of_sound = origin_of_sound
        pass
    pass

class Consola(Types_of_reproductor):
    def __init__(self, origin_of_sound = "Consola") -> None:
        self.origin_of_sound = origin_of_sound

class Reproductor():
    def __init__(self,origin_of_sound_rep = MP3()) -> None:
        self.origin_of_sound_rep = origin_of_sound_rep
        pass
    def reproducir(self):
        print (f"Sonando {self.origin_of_sound_rep.name_getter()}")
        return
    def cambiar_fuente(self,new_origin_of_sound):
        self.origin_of_sound_rep  = new_origin_of_sound
        return
    pass

reproductor = Reproductor()

reproductor.reproducir()
reproductor.cambiar_fuente(CD())
reproductor.reproducir()
reproductor.cambiar_fuente(Consola())
reproductor.reproducir()
