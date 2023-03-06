from tkinter import *
from datetime import datetime, date, time, timedelta


#1. instanciamos el objeto ventana

ventana= Tk()   
ventana.geometry("600x400")
ventana.title("Historial")

seccion1= Frame(ventana)
seccion1.pack(expand=True,fill='both')
 
seccion2= Frame(ventana)
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana)
seccion3.pack(expand=True,fill='both')

#texto para los campos
txtinicio= Label(seccion1,text="Historial")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=270,y=30)

txtCorreo= Label(seccion2,text="fecha:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=20,y=1)

txtCorreo= Label(seccion2,text="xx/xx/xxx",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=70,y=1)

txtContra= Label(seccion2,text="equpo 1",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=85,y=50)

txtContra= Label(seccion2,text="equpo 2",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=375,y=50)

txtContra= Label(seccion2,text="empate",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=230,y=50)

txtCorreo= Label(seccion3,text="fecha:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=20,y=1)

txtCorreo= Label(seccion3,text="xx/xx/xxx",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=70,y=1)

txtContra= Label(seccion3,text="equpo 1",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=85,y=50)

txtContra= Label(seccion3,text="equpo 2",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=375,y=50)

txtContra= Label(seccion3,text="empate",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=230,y=50)
#los campos
Correo= Entry(seccion2, bg="#F3F3F3")
Correo.place(x=55,y=75)

Contraseña= Entry(seccion2, bg="#F3F3F3")
Contraseña.place(x=200, y=75)

Contraseña= Entry(seccion2, bg="#F3F3F3")
Contraseña.place(x=345, y=75)

orreo= Entry(seccion3, bg="#F3F3F3")
Correo.place(x=55,y=75)

Contraseña= Entry(seccion3, bg="#F3F3F3",show="*")
Contraseña.place(x=200, y=75)
3
Contraseña= Entry(seccion3, bg="#F3F3F3",show="*")
Contraseña.place(x=345, y=75)


#3. agregamos los botones

btonloG= Button(seccion2,text="GANADO",fg="green",bg="white")
btonloG.place(x=510,y=20)

btonloG= Button(seccion2,text="PERDIDO",fg="red",bg="white")
btonloG.place(x=510,y=60)

btonloG= Button(seccion3,text="GANADO",fg="green",bg="white")
btonloG.place(x=510,y=20)

btonloG= Button(seccion3,text="PERDIDO",fg="red",bg="white")
btonloG.place(x=510,y=60)


ventana.mainloop()