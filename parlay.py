from tkinter import *

#ventana
ventana= Tk()   
ventana.geometry("800x600")
ventana.title("momio")

#frames

seccion1= Frame(ventana)
seccion1.pack(expand=True,fill='both')

#texto

txtinicio= Label(seccion1,text="cantidad de momios:")
txtinicio.configure(font=("calibri", 13))
txtinicio.place(x=270,y=30)

txtCorreo= Label(seccion1,text="momio1:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=20,y=85)

txtCorreo= Label(seccion1,text="momio2:",fg="black")
txtCorreo.configure(font=("calibri",13))
txtCorreo.place(x=20,y=165)

txtContra= Label(seccion1,text="equpo 1",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=115,y=80)

txtContra= Label(seccion1,text="equpo 2",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=405,y=80)

txtContra= Label(seccion1,text="empate",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=260,y=80)

txtContra= Label(seccion1,text="equpo 1",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=115,y=160)

txtContra= Label(seccion1,text="equpo 2",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=405,y=160)

txtContra= Label(seccion1,text="empate",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=260,y=160)

txtContra= Label(seccion1,text="selescciones su prediccion:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=550,y=70)

txtContra= Label(seccion1,text="selescciones su prediccion:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=550,y=150)

txtContra= Label(seccion1,text="cantidad a apostar:",fg="black")
txtContra.configure(font=("calibri",13))
txtContra.place(x=130,y=220)

txtContra= Label(seccion1,text="total a ganar:",fg="black")
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

btonloG= Button(seccion1,text="momio",bg="white")
btonloG.place(x=25,y=30)

btonloG= Button(seccion1,text="individual",bg="white")
btonloG.place(x=140,y=30)

btonloG= Button(seccion1,text="equipo1",bg="white")
btonloG.place(x=550,y=105)

btonloG= Button(seccion1,text="empate",bg="white")
btonloG.place(x=610,y=105)

btonloG= Button(seccion1,text="equipo2",bg="white")
btonloG.place(x=670,y=105)

btonloG= Button(seccion1,text="equipo1",bg="white")
btonloG.place(x=550,y=185)

btonloG= Button(seccion1,text="empate",bg="white")
btonloG.place(x=610,y=185)

btonloG= Button(seccion1,text="equipo2",bg="white")
btonloG.place(x=670,y=185)


btonloG= Button(seccion1,text="guardar",bg="white")
btonloG.place(x=470,y=230)

ventana.mainloop()
