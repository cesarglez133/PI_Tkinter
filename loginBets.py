import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x200")


# Crear etiqueta para correo
lblCorreo = tk.Label(ventana, text="Correo electrónico:")
lblCorreo.pack(pady=5)

# Crear campo de entrada para correo
txtCorreo = tk.Entry(ventana)
txtCorreo.pack(pady=5)

# Crear etiqueta para contraseña
lblContrasena = tk.Label(ventana, text="Contraseña:")
lblContrasena.pack(pady=5)

# Crear campo de entrada para contraseña
txtContrasena = tk.Entry(ventana, show="*")
txtContrasena.pack(pady=5)

# Crear botón de iniciar sesión
btnIniciarSesion = tk.Button(ventana, text="Iniciar sesión")
btnIniciarSesion.pack(pady=10)

# Crear botón de registrarme
btnRegistrarme = tk.Button(ventana, text="Registrarme")
btnRegistrarme.pack()

# Crear botón de olvidé mi contraseña
btnOlvideContrasena = tk.Button(ventana, text="Olvidé mi contraseña")
btnOlvideContrasena.pack(pady=5)

# Centrar ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

# Iniciar ciclo de eventos
ventana.mainloop()
