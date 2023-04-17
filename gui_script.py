from tkinter import * # Load library
from math import sqrt

# Define functions Aire and Perim
def Aire():
    base = float(entreeBase.get())
    hauteur = float(entreeHauteur.get())
    aire = (base * hauteur) / 2
def Perim():
    base = float(entreeBase.get())
    hauteur = float(entreeHauteur.get())
    perim = base + hauteur + sqrt(base**2 +hauteur**2)

# Define window
fen1 = Tk()

# Create labels
label_b = Label(fen1, text = "base:")
label_b.grid(row = 0, column = 0)
label_h = Label(fen1, text = "hauteur")
label_h.grid(row = 0, column = 1)

# Create entry text zones for base and height
entreeBase = Entry(fen1)
entreeBase.grid(row = 0, column = 1)
entreeHauteur = Entry(fen1)
entreeHauteur.grid(row = 1, column = 1)

# Create buttons to obtain calculations
boutonAire = Button(fen1, text = "Aire", command = Aire)
boutonAire.grid(row = 4, column = 0)
boutonPerim = Button(fen1, text = "Perimetre", command = Perim)
boutonPerim.grid(row = 4, column = 1)

fen1.mainloop()
