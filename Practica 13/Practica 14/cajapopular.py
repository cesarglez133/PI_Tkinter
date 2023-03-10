import random

class CajaPopular:
    def __init__(self):
        self.cuenta_actual = None

    def crear_cuenta(self, nombre, edad):
        nueva_cuenta = Cuenta(nombre, edad)
        numero_cuenta = random.randint(1000, 9999)
        nueva_cuenta.asignar_numero_cuenta(numero_cuenta)
        self.cuenta_actual = nueva_cuenta
        return nueva_cuenta

    def consultar_saldo(self):
        return self.cuenta_actual.consultar_saldo()

    def ingresar_efectivo(self, cantidad):
        self.cuenta_actual.ingresar_efectivo(cantidad)

    def retirar_efectivo(self, cantidad):
        return self.cuenta_actual.retirar_efectivo(cantidad)

    def transferir_efectivo(self, cantidad, numero_cuenta_destino):
        return self.cuenta_actual.transferir_efectivo(cantidad, numero_cuenta_destino)

class Cuenta:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.numero_cuenta = None
        self.saldo_actual = 0.0

    def asignar_numero_cuenta(self, numero):
        self.numero_cuenta = numero

    def consultar_saldo(self):
        return self.saldo_actual

    def ingresar_efectivo(self, cantidad):
        self.saldo_actual += cantidad

    def retirar_efectivo(self, cantidad):
        if cantidad > self.saldo_actual:
            return False
        else:
            self.saldo_actual -= cantidad
            return True

    def transferir_efectivo(self, cantidad, cuenta_destino):
        if cantidad > self.saldo_actual:
            return False
        else:
            self.saldo_actual -= cantidad
            return True