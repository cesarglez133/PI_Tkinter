import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Casas de apuestas")
ventana.geometry("400x300")

# Crear etiqueta de título
lblTitulo = tk.Label(ventana, text="Elige tu casa de apuestas la cuál quieres emular", font=("Arial", 12))
lblTitulo.pack(pady=10)

# Crear botón de Caliente.mx
btnCaliente = tk.Button(ventana, text="Caliente.mx", font=("Arial", 10), width=20, height=2, bg="#ff0000", fg="#ffffff")
btnCaliente.pack(pady=10)

# Crear botón de Bet365
btnBet365 = tk.Button(ventana, text="Bet365", font=("Arial", 10), width=20, height=2, bg="#07A40E", fg="#ffffff")
btnBet365.pack(pady=10)

# Centrar ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

# Iniciar ciclo de eventos
ventana.mainloop()
