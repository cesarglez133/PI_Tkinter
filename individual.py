import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Apuestas")
ventana.geometry("800x500")
ventana.configure(bg="white")

# Primera fila con botones
lblTipoApuesta = tk.Label(ventana, text="Tipo de apuesta:", font=("Arial", 10))
lblTipoApuesta.grid(row=0, column=0, padx=10, pady=10, sticky="w")

lblCantidadApostar = tk.Label(ventana, text="Cantidad de dinero a apostar:", font=("Arial", 10))
lblCantidadApostar.grid(row=1, column=0, padx=10, pady=10, sticky="w")

btnIndividual = tk.Button(ventana, text="Individual", font=("Arial", 10), width=10)
btnIndividual.grid(row=0, column=1, padx=10, pady=10)

btnMomio = tk.Button(ventana, text="Parlay", font=("Arial", 10), width=10)
btnMomio.grid(row=0, column=2, padx=10, pady=10)

entryCantidadApostar = tk.Entry(ventana, font=("Arial", 10), width=15)
entryCantidadApostar.grid(row=1, column=1, padx=10, pady=10)

# Segunda fila con etiquetas de equipo

lblEquipo1 = tk.Label(ventana, text="Equipo 1", font=("Arial", 10))
lblEquipo1.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblEquipo2 = tk.Label(ventana, text="Equipo 2", font=("Arial", 10))
lblEquipo2.grid(row=3, column=2, padx=10, pady=10, sticky="w")

lblEquipo3 = tk.Label(ventana, text="Equipo 3", font=("Arial", 10))
lblEquipo3.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Tercera fila con cuadros de texto y botón de guardar
lblNombres = tk.Label(ventana, text="Momios:", font=("Arial", 10))
lblNombres.grid(row=4, column=0, padx=10, pady=10, sticky="w")

entryEquipo1 = tk.Entry(ventana, font=("Arial", 10), width=15)
entryEquipo1.grid(row=4, column=1, padx=10, pady=10)

entryEquipo2 = tk.Entry(ventana, font=("Arial", 10), width=15)
entryEquipo2.grid(row=4, column=2, padx=10, pady=10)

entryEquipo3 = tk.Entry(ventana, font=("Arial", 10), width=15)
entryEquipo3.grid(row=4, column=3, padx=10, pady=10)

btnGuardar = tk.Button(ventana, text="Guardar", font=("Arial", 10), width=10)
btnGuardar.grid(row=4, column=4, padx=10, pady=10)

#Cuarta fila con etiquetas de momio
lblMomio1 = tk.Button(ventana, text="Seleccionar opción", font=("Arial", 10))
lblMomio1.grid(row=6, column=1, padx=10, pady=10, sticky="w")

lblMomio2 = tk.Button(ventana, text="Seleccionar opción", font=("Arial", 10))
lblMomio2.grid(row=6, column=2, padx=10, pady=10, sticky="w")

lblMomio3 = tk.Button(ventana, text="Seleccionar opción", font=("Arial", 10))
lblMomio3.grid(row=6, column=3, padx=10, pady=10, sticky="w")

#Quinta fila con etiqueta de total a ganar
lblTotalGanar = tk.Label(ventana, text="Total a ganar: ", font=("Arial", 10))
lblTotalGanar.grid(row=7, column=0, padx=10, pady=10, sticky="w")

#Centrar ventana en la pantalla
ventana.eval('tk::PlaceWindow . center')

#Iniciar ciclo de eventos
ventana.mainloop()

S