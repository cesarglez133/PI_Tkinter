import tkinter as tk
from tkinter import messagebox

from cajapopular import CajaPopular

class InterfazCajaUPQ:
    def __init__(self, ventana):
        self.ventana = ventana
        self.cajapopular = CajaPopular()

        self.pantalla_inicio()

    def pantalla_inicio(self):
        self.limpiar_pantalla()
        self.ventana.title("CajaUPQ")
        tk.Label(self.ventana, text="Bienvenido a CajaUPQ", font=("Arial", 20)).pack(pady=20)
        tk.Button(self.ventana, text="Crear cuenta", font=("Arial", 14), command=self.pantalla_crear_cuenta).pack(pady=10)
        tk.Button(self.ventana, text="Acceder a mi cuenta", font=("Arial", 14), command=self.pantalla_datos_cuenta).pack(pady=10)

    def pantalla_crear_cuenta(self):
        self.limpiar_pantalla()
        self.ventana.title("Crear cuenta")
        tk.Label(self.ventana, text="Por favor, ingrese sus datos", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.ventana, text="Nombre: ").pack()
        nombre_entry = tk.Entry(self.ventana, font=("Arial", 14))
        nombre_entry.pack()
        tk.Label(self.ventana, text="Edad: ").pack()
        edad_entry = tk.Entry(self.ventana, font=("Arial", 14))
        edad_entry.pack()
        tk.Button(self.ventana, text="Crear", font    =("Arial", 14), command=lambda: self.crear_cuenta(nombre_entry.get(), edad_entry.get())).pack(pady=20)

    def pantalla_datos_cuenta(self):
        self.limpiar_pantalla()
        self.ventana.title("Mi cuenta")
        tk.Label(self.ventana, text="Datos de mi cuenta", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.ventana, text="Nombre: " + self.cajapopular.cuenta_actual.nombre, font=("Arial", 14)).pack()
        tk.Label(self.ventana, text="Número de cuenta: " + str(self.cajapopular.cuenta_actual.numero_cuenta), font=("Arial", 14)).pack()
        tk.Label(self.ventana, text="Edad: " + str(self.cajapopular.cuenta_actual.edad), font=("Arial", 14)).pack()
        tk.Label(self.ventana, text="Saldo actual: $" + str(self.cajapopular.cuenta_actual.saldo_actual), font=("Arial", 14)).pack(pady=20)
        tk.Button(self.ventana, text="Consultar saldo", font=("Arial", 14), command=self.pantalla_consultar_saldo).pack(pady=10)
        tk.Button(self.ventana, text="Ingresar efectivo", font=("Arial", 14), command=self.pantalla_ingresar_efectivo).pack(pady=10)
        tk.Button(self.ventana, text="Retirar efectivo", font=("Arial", 14), command=self.pantalla_retirar_efectivo).pack(pady=10)
        tk.Button(self.ventana, text="Transferir a otra cuenta", font=("Arial", 14), command=self.pantalla_transferir_efectivo).pack(pady=10)

    def pantalla_consultar_saldo(self):
        self.limpiar_pantalla()
        self.ventana.title("Consultar saldo")
        tk.Label(self.ventana, text="Saldo actual: $" + str(self.cajapopular.consultar_saldo()), font=("Arial", 20)).pack(pady=20)
        tk.Button(self.ventana, text="Volver", font=("Arial", 14), command=self.pantalla_datos_cuenta).pack(pady=20)

    def pantalla_ingresar_efectivo(self):
        self.limpiar_pantalla()
        self.ventana.title("Ingresar efectivo")
        tk.Label(self.ventana, text="Ingrese la cantidad de efectivo a ingresar", font=("Arial", 20)).pack(pady=20)
        cantidad_entry = tk.Entry(self.ventana, font=("Arial", 14))
        cantidad_entry.pack()
        tk.Button(self.ventana, text="Ingresar", font=("Arial", 14), command=lambda: self.ingresar_efectivo(cantidad_entry.get())).pack(pady=20)

    def pantalla_retirar_efectivo(self):
        self.limpiar_pantalla()
        self.ventana.title("Retirar efectivo")
        tk.Label(self.ventana, text="Ingrese la cantidad de efectivo a retirar", font=("Arial", 20)).pack(pady=20)
        cantidad_entry = tk.Entry(self.ventana, font=("Arial", 14))
        cantidad_entry.pack()
        tk.Button(self.ventana, text="Retirar", font=("Arial", 14), command=lambda: self.retirar_efectivo(cantidad_entry.get())).pack(pady=20)

    def pantalla_transferir_efectivo(self):
        self.limpiar_pantalla()
        self.ventana.title("Transferir a otra cuenta")
        tk.Label(self.ventana, text="Ingrese la cantidad de efectivo a transferir", font=("Arial", 20)).pack(pady=20)
        cantidad_entry = tk.Entry(self.ventana, font=("Arial", 14))
        cantidad_entry.pack()
        tk.Label(self.ventana, text="Ingrese el número de cuenta destino", font=("Arial", 20)).pack(pady=20)
        numero_entry = tk.Entry(self.ventana, font=("Arial", 14))
        numero_entry.pack()
        tk.Button(self.ventana, text="Transferir", font=("Arial", 14), command=lambda: self.transferir_efectivo(cantidad_entry.get(), numero_entry.get())).pack(pady=20)
    
    def crear_cuenta(self, nombre, edad):
        nueva_cuenta = self.cajapopular.crear_cuenta(nombre, edad)
        self.mostrar_mensaje("¡Cuenta creada con éxito!\nSu número de cuenta es " + str(nueva_cuenta.numero_cuenta))
        self.pantalla_datos_cuenta()

    def ingresar_efectivo(self, cantidad):
        self.cajapopular.ingresar_efectivo(float(cantidad))
        self.mostrar_mensaje("Efectivo ingresado con éxito")
        self.pantalla_datos_cuenta()

    def retirar_efectivo(self, cantidad):
        if self.cajapopular.retirar_efectivo(float(cantidad)):
            self.mostrar_mensaje("Efectivo retirado con éxito")
        else:
            self.mostrar_mensaje("No hay suficiente saldo en la cuenta")
        self.pantalla_datos_cuenta()

    def transferir_efectivo(self, cantidad, numero_cuenta_destino):
        if self.cajapopular.transferir_efectivo(float(cantidad), numero_cuenta_destino):
            self.mostrar_mensaje("Efectivo transferido con éxito")
        else:
            self.mostrar_mensaje("No hay suficiente saldo en la cuenta")
        self.pantalla_datos_cuenta()

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("CajaUPQ", mensaje)

    def limpiar_pantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    InterfazCajaUPQ(ventana_principal)
    ventana_principal.mainloop()