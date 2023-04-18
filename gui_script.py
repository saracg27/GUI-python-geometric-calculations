#Devoir semaine 4 - Python. Creer une interface utilisateur permettant de calculer le périmètre et l'aire d'un triangle rectangle
# à partir  de la base et de la hauteur du triangle. 

# Importer las bibliothèques tkinter pour créer une interface graphique, et math pour sqrt
from tkinter import *
from math import sqrt

# Définir les fonctions Aire et Perim
def Aire():
    # Récupérer les valeurs entrées pour la base et la hauteur
    base = float(entreeBase.get())
    hauteur = float(entreeHauteur.get())
    # Calculer l'aire du triangle
    aire = (base * hauteur) / 2
    # Effacer le texte précédent affiché pour le périmètre
    txtPerim.configure(text="")
    # Afficher l'aire calculée avec deux décimales
    txtAire.configure(text="{:.2f}".format(aire))
    # Changer le texte du label pour "Aire"
    txtCm.configure(text="Aire:")

def Perim():
    # Récupérer les valeurs entrées pour la base et la hauteur
    base = float(entreeBase.get())
    hauteur = float(entreeHauteur.get())
    # Calculer le périmètre du triangle
    perim = base + hauteur + sqrt(base**2 +hauteur**2)
    # Effacer le texte précédent affiché pour l'aire
    txtAire.configure(text="")
    # Afficher le périmètre calculé avec deux décimales
    txtPerim.configure(text="{:.2f}".format(perim))
    # Changer le texte du label pour "Périmètre"
    txtCm.configure(text="Périmètre:")

# Créer une fenêtre principale
fen1 = Tk()
# Donner un titre à la fenêtre
fen1.title("Triangle")

# Créer les étiquettes pour l'entrée de la base et de la hauteur
label_b = Label(fen1, text = "base:")
label_b.grid(row = 0, column = 0, sticky=E)
label_h = Label(fen1, text = "hauteur:")
label_h.grid(row = 1, column = 0, sticky=E)
# Créer un label pour afficher le résultat (air ou périmètre)
txtCm = Label(fen1, text = "--:")
txtCm.grid(row = 2, column = 0, sticky=E)

# Créer un label pour afficher le résultat de l'aire
txtAire = Label(fen1, text="")
txtAire.grid(row=2, column=1)
# Créer un label pour afficher le résultat du périmètre
txtPerim = Label(fen1, text="")
txtPerim.grid(row=2, column=1)

# Créer des zones d'entrée pour la base et la hauteur
entreeBase = Entry(fen1)
entreeBase.grid(row = 0, column = 1)
entreeHauteur = Entry(fen1)
entreeHauteur.grid(row = 1, column = 1)

# Créer des boutons pour lancer les calculs
boutonAire = Button(fen1, text = "Aire", command = Aire)
boutonAire.grid(row = 3, column = 0)
boutonPerim = Button(fen1, text = "Périmètre", command = Perim)
boutonPerim.grid(row = 3, column = 1)

# Démarrer la boucle et la fenêtre
fen1.mainloop()
