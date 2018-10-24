# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import re

from carte import *
from fonctions import *

#Gestion des parties sauvegardées

#sauvegarde = recup_sauvegarde()


# On charge les cartes existantes
cartes = []
for filename in os.listdir("cartes"): #scandir(peut-etre plus interessant...)
    if filename.endswith(".txt"):
        chemin = os.path.join("cartes", filename)
        mapName = filename[:-3].lower() # nom_carte = filename[:-3].lower()
        with open(chemin, "r") as mapFile:
            mapContent = mapFile.read()
            cartes.append(Carte(mapName, mapContent))


            # Création d'une carte, à compléter

            print(contenu) #Semble enfin afficher le contenu des fichiers texte
            print(nom_carte) #clairement pas au bon endroit
            print(chemin)    #clairement pas au bon endroit
            print(cartes)    #clairement pas au bon endroit

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))




# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
