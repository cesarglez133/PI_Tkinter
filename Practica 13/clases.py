import string
import random

class GeneradorContrasena:
    def __init__(self, longitud):
        self.longitud = longitud
        self.caracteres = string.ascii_uppercase
        self.contrasena = ""

    def agregar_mayusculas(self):
        self.caracteres += string.ascii_uppercase

    def agregar_caracteres_especiales(self, cantidad):
        caracteres_especiales = string.punctuation
        for i in range(cantidad):
            self.caracteres += random.choice(caracteres_especiales)

    def generar_contrasena(self):
        if self.longitud < 8:
            return "La longitud de la contraseña debe ser al menos de 8 caracteres."

        for i in range(self.longitud):
            self.contrasena += random.choice(self.caracteres)

        return self.contrasena
