import tkinter as tk
from tkinter import messagebox
from clases import GeneradorContrasena
import string

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

        self.label_especiales = tk.Label(self.root, text="Cantidad de caracteres especiales:")
        self.label_especiales.grid(column=0, row=2, padx=10, pady=10)

        self.entry_especiales = tk.Entry(self.root)
        self.entry_especiales.grid(column=1, row=2)

        self.boton_generar = tk.Button(self.root, text="Generar contraseña", command=self.generar_contrasena)
        self.boton_generar.grid(column=1, row=3, pady=10)

        self.root.mainloop()

    def generar_contrasena(self):
        longitud = int(self.entry_longitud.get())

        if self.var_mayusculas.get():
            mayusculas = True
        else:
            mayusculas = False

        try:
            especiales = int(self.entry_especiales.get())
        except ValueError:
            especiales = 0

        generador = GeneradorContrasena(longitud)
        if mayusculas:
            generador.agregar_mayusculas()
        if especiales > 0:
            generador.agregar_caracteres_especiales(especiales)

        contrasena_generada = generador.generar_contrasena()
        if contrasena_generada.startswith("La longitud de la contraseña debe ser al menos de 8 caracteres."):
            messagebox.showerror("Error", contrasena_generada)
        else:
            messagebox.showinfo("Contraseña generada", f"La contraseña generada es: {contrasena_generada}")
            self.verificar_fortaleza(contrasena_generada)

    def verificar_fortaleza(self, contrasena):
        longitud = len(contrasena)
        numeros = sum(c.isdigit() for c in contrasena)
        letras_mayusculas = sum(c.isupper() for c in contrasena)
        caracteres_especiales = sum(c in string.punctuation for c in contrasena)

        if numeros == longitud:
            if longitud >= 8 and longitud <= 20:
                messagebox.showinfo("Fortaleza de la contraseña", "La contraseña es débil")
            elif longitud > 20:
                messagebox.showinfo("Fortaleza de la contraseña", "Lacontraseña es fácil")
                
        elif numeros + letras_mayusculas == longitud:
            if longitud >= 8 and longitud <= 20:
                messagebox.showinfo("Fortaleza de la contraseña", "La contraseña es fácil")
            elif longitud > 20:
                messagebox.showinfo("Fortaleza de la contraseña", "La contraseña es media")
                
        elif numeros + letras_mayusculas + caracteres_especiales:
            if longitud >= 8 and longitud <= 20:
                    messagebox.showinfo("Fortaleza de la contraseña", "La contraseña es media")
            elif longitud > 20:
                    messagebox.showinfo("Fortaleza de la contraseña", "La contraseña es fuerte")


