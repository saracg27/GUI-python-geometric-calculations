from tkinter import *
from math import sqrt


def Aire():
    base=float(entreeBase.get())
    hauteur=float(entreeHauteur.get())
    aire=(base*hauteur)/2
    txtPerim.configure(text="")
    txtAire.configure(text="{:.2f}".format(aire))
    txtCm.configure(text="Aire:")

def Perim():
    base=float(entreeBase.get())
    hauteur=float(entreeHauteur.get())
    perim=base+hauteur+sqrt(base**2+hauteur**2)
    txtAire.configure(text="")
    txtPerim.configure(text="{:.2f}".format(perim))
    txtCm.configure(text="Périmètre:")

fen1=Tk()
fen1.title("Triangle")

label_b=Label(fen1,text="base:")
label_b.grid(row=0,column=0,sticky=E)
label_h=Label(fen1,text="hauteur:")
label_h.grid(row=1,column=0,sticky=E)
txtCm=Label(fen1,text="--:")
txtCm.grid(row=2,column=0,sticky=E)

txtAire=Label(fen1,text="")
txtAire.grid(row=2,column=1)
txtPerim=Label(fen1,text="")
txtPerim.grid(row=2,column=1)

entreeBase=Entry(fen1)
entreeBase.grid(row=0,column=1)
entreeHauteur=Entry(fen1)
entreeHauteur.grid(row=1,column=1)

boutonAire=Button(fen1,text="Aire",command=Aire)
boutonAire.grid(row=3,column=0)
boutonPerim=Button(fen1,text="Périmètre",command=Perim)
boutonPerim.grid(row=3,column=1)

fen1.mainloop()
