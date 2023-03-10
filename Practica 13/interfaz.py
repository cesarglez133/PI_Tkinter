import tkinter as tk
from tkinter import messagebox
from clases import GeneradorContrasena
import string
import random

class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Generador de contraseñas")

        self.label_longitud = tk.Label(self.root, text="Longitud de la contraseña:")
        self.label_longitud.grid(column=0, row=0, padx=10, pady=10)

        self.entry_longitud = tk.Entry(self.root)
        self.entry_longitud.grid(column=1, row=0)

        self.label_mayusculas = tk.Label(self.root, text="¿Agregar letras mayúsculas?")
        self.label_mayusculas.grid(column=0, row=1, padx=10, pady=10)

        self.var_mayusculas = tk.BooleanVar(value=False)
        self.check_mayusculas = tk.Checkbutton(self.root, variable=self.var_mayusculas)
        self.check_mayusculas.grid(column=1, row=1)

        self.label_especiales = tk.Label(self.root, text="¿Agregar caracteres especiales?")
        self.label_especiales.grid(column=0, row=2, padx=10, pady=10)

        self.var_especiales = tk.BooleanVar(value=False)
        self.check_especiales = tk.Checkbutton(self.root, variable=self.var_especiales)
        self.check_especiales.grid(column=1, row=2)

        self.boton_generar = tk.Button(self.root, text="Generar contraseña", command=self.mostrar_contrasena)
        self.boton_generar.grid(column=1, row=3, pady=10)

        self.label_contrasena = tk.Label(self.root, text="Contraseña generada:")
        self.label_contrasena.grid(column=0, row=4, padx=10, pady=10)

        self.entry_contrasena = tk.Entry(self.root, width=30)
        self.entry_contrasena.grid(column=1, row=4)

        self.boton_copiar = tk.Button(self.root, text="Copiar", command=self.copiar_contrasena)
        self.boton_copiar.grid(column=2, row=4)

        self.root.mainloop()

    def mostrar_contrasena(self):
        longitud = int(self.entry_longitud.get())

        generador = GeneradorContrasena(longitud)
        if self.var_mayusculas.get():
            generador.agregar_mayusculas()
        generador.agregar_caracteres_especiales(self.var_especiales.get())
        contrasena_generada = generador.generar_contrasena()

        if contrasena_generada.startswith("La longitud de la contraseña debe ser al menos de 8 caracteres."):
            messagebox.showerror("Error", contrasena_generada)
            return
        else:
            self.entry_contrasena.delete(0, tk.END)
            self.entry_contrasena.insert(0, contrasena_generada)
            fortaleza = self.verificar_fortaleza(contrasena_generada)
            messagebox.showinfo("Contraseña generada", f"La contraseña generada es: {contrasena_generada}\n\nFortaleza: {fortaleza}")


    def verificar_fortaleza(self, contrasena):
        longitud = len(contrasena)
        numeros = sum(c.isdigit() for c in contrasena)
        letras_mayusculas = sum(c.isupper() for c in contrasena)
        letras_minusculas = sum(c.islower() for c in contrasena)
        caracteres_especiales = sum(c in string.punctuation for c in contrasena)

        if letras_minusculas == longitud and longitud >= 8 and longitud <= 20:
            return "Débil"

        elif letras_minusculas == longitud and longitud > 20:
            return "Media"

        elif letras_mayusculas > 0 and letras_minusculas > 0 and caracteres_especiales > 0 and longitud >= 8 and longitud <= 20:
            return "Media"

        elif letras_mayusculas > 0 and letras_minusculas > 0 and caracteres_especiales > 0 and longitud > 20:
            return "Fuerte"

        elif letras_mayusculas > 0 and letras_minusculas > 0 and longitud >= 8 and longitud <= 20:
            return "Fácil"

        elif letras_mayusculas > 0 and letras_minusculas > 0 and longitud > 20:
            return "Media"

        elif letras_minusculas > 0 and caracteres_especiales > 0 and longitud >= 8 and longitud <= 20:
            return "Media"

        elif letras_minusculas > 0 and caracteres_especiales > 0 and longitud > 20:
            return "Media"


       


    def copiar_contrasena(self):
        contrasena = self.entry_contrasena.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(contrasena)