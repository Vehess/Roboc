import os
import pickle

def recup_sauvegarde():
    """Cette fonction récupère les scores enregistrés si le fichier existe."""

    if os.path.exists(nom_fichier_sauvegarde):  # Le fichier existe
        # On le récupère
        fichier_sauvegarde = open(nom_fichier_sauvegarde, "rb")
        mon_depickler = pickle.Unpickler(fichier_sauvegarde)
        sauvegarde = mon_depickler.load()
        fichier_sauvegarde.close()
    else:  # Le fichier n'existe pas
        sauvegarde = {}
    return sauvegarde

def enregistrer_sauvegarde(sauvegarde):
    """Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores."""

    fichier_sauvegarde = open(nom_fichier_sauvegarde, "wb") # On écrase les anciennes sauvegarde
    mon_pickler = pickle.Pickler(fichier_sauvegarde)
    mon_pickler.dump(sauvegarde)
    fichier_sauvegarde.close()