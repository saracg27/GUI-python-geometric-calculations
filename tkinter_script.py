#Creer une interface utilisateur permettant de calculer le périmètre et l'aire d'un triangle rectangle
# à partir  de la base et de la hauteur du triangle. 

# Importer la bibliothèque tkinter pour créer une interface graphique
from tkinter import *
# Importer la fonction racine carrée de la bibliothèque mathématique pour le calcul du périmètre
from math import sqrt

# Define functions Aire and Perim
def Aire():
    base = float(entreeBase.get())
    hauteur = float(entreeHauteur.get())
    aire = (base * hauteur) / 2
    txtPerim.configure(text="") # Effacer le texte précédent affiché pour le périmètre
    txtAire.configure(text="{:.2f}".format(aire)) # Afficher l'aire calculée avec deux décimales
    txtCm.configure(text="Aire:")
    
def Perim():
    base = float(entreeBase.get())
    hauteur = float(entreeHauteur.get())
    perim = base + hauteur + sqrt(base**2 +hauteur**2)
    txtAire.configure(text="")
    txtPerim.configure(text="{:.2f}".format(perim))
    txtCm.configure(text="Perimetre:")

# Define window
fen1 = Tk()
fen1.title("Triangle")

# Create labels
label_b = Label(fen1, text = "base:")
label_b.grid(row = 0, column = 0)
label_h = Label(fen1, text = "hauteur:")
label_h.grid(row = 1, column = 0)
txtCm = Label(fen1, text = "--:")
txtCm.grid(row = 2, column = 0)

txtAire = Label(fen1, text="")
txtAire.grid(row=2, column=1)
txtPerim = Label(fen1, text="")
txtPerim.grid(row=2, column=1)

# Create entry text zones for base and height
entreeBase = Entry(fen1)
entreeBase.grid(row = 0, column = 1)
entreeHauteur = Entry(fen1)
entreeHauteur.grid(row = 1, column = 1)

# Create buttons to obtain calculations
boutonAire = Button(fen1, text = "Aire", command = Aire)
boutonAire.grid(row = 3, column = 0)
boutonPerim = Button(fen1, text = "Perimetre", command = Perim)
boutonPerim.grid(row = 3, column = 1)

fen1.mainloop()
