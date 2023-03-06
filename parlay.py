from tkinter import *

#ventana
ventana= Tk()   
ventana.geometry("800x600")
ventana.title("Parlay")

#frames

seccion1= Frame(ventana)
seccion1.pack(expand=True,fill='both')

#texto

txtinicio= Label(seccion1,text="Cantidad de momios:")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=270,y=30)

txtCorreo= Label(seccion1,text="Momio1:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=20,y=85)

txtCorreo= Label(seccion1,text="Momio2:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=20,y=165)

txtContra= Label(seccion1,text="Equipo 1",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=115,y=80)

txtContra= Label(seccion1,text="Equipo 2",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=405,y=80)

txtContra= Label(seccion1,text="Empate",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=260,y=80)

txtContra= Label(seccion1,text="Equipo 1",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=115,y=160)

txtContra= Label(seccion1,text="Equipo 2",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=405,y=160)

txtContra= Label(seccion1,text="Empate",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=260,y=160)

txtContra= Label(seccion1,text="Seleccione su predicción:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=550,y=70)

txtContra= Label(seccion1,text="Seleccione su predicción:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=550,y=150)

txtContra= Label(seccion1,text="Cantidad a apostar:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=130,y=220)

txtContra= Label(seccion1,text="Total a ganar:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=130,y=250)
#entry
Correo= Entry(seccion1, bg="#F3F3F3")
Correo.place(x=90,y=105)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=370, y=105)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=230, y=105)

Correo= Entry(seccion1, bg="#F3F3F3")
Correo.place(x=90,y=185)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=370, y=185)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=230, y=185)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=420, y=34)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=272, y=224)

Contraseña= Entry(seccion1, bg="#F3F3F3")
Contraseña.place(x=232, y=256)
#los botones

btonloG= Button(seccion1,text="Individual",bg="white")
btonloG.place(x=25,y=30)

btonloG= Button(seccion1,text="Parlay",bg="white")
btonloG.place(x=140,y=30)

btonloG= Button(seccion1,text="Equipo1",bg="white")
btonloG.place(x=550,y=105)

btonloG= Button(seccion1,text="Empate",bg="white")
btonloG.place(x=610,y=105)

btonloG= Button(seccion1,text="Equipo2",bg="white")
btonloG.place(x=670,y=105)

btonloG= Button(seccion1,text="Equipo1",bg="white")
btonloG.place(x=550,y=185)

btonloG= Button(seccion1,text="Empate",bg="white")
btonloG.place(x=610,y=185)

btonloG= Button(seccion1,text="Equipo2",bg="white")
btonloG.place(x=670,y=185)


btonloG= Button(seccion1,text="Guardar",bg="white")
btonloG.place(x=470,y=230)

ventana.mainloop()