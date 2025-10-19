import numpy as np
import os

# Fonction pour lire la matrice depuis un fichier BMP
def lire_matrice_bmp(fichier):
    with open(fichier, 'r') as f:
        # Ignorer la ligne 'P1' et toute ligne de commentaire
        while True:
            ligne = f.readline().strip()
            if ligne == 'P1':
                break
            if ligne.startswith('#'):  # Ignorer les commentaires
                continue

        # Lire la taille de la matrice
        dimensions = f.readline().strip().split()
        lignes = int(dimensions[0])
        colonnes = int(dimensions[1])

        # Lire les éléments de la matrice
        matrice = [list(map(int, ligne.strip().split())) for ligne in f.readlines()]
    
    return np.array(matrice)

# Fonction pour écrire la matrice dans un fichier BMP
def ecrire_matrice_bmp(fichier, matrice):
    with open(fichier, 'w') as f:
        f.write('P1\n')
        f.write(f"{matrice.shape[0]} {matrice.shape[1]}\n")
        for ligne in matrice:
            f.write(' '.join(map(str, ligne)) + '\n')

# Fonction pour chercher un fichier dans le répertoire du script
def chercher_fichier(nom_fichier):
    # Obtient le répertoire du script actuel
    script_dir = os.path.dirname(os.path.realpath(__file__))
    chemin_fichier = os.path.join(script_dir, nom_fichier)
    
    if os.path.exists(chemin_fichier):
        return chemin_fichier
    return None  # Si le fichier n'est pas trouvé dans le répertoire du script

# Chercher les fichiers BMP dans le répertoire du script
chemin_i1 = chercher_fichier('i1.bmp')
chemin_i2 = chercher_fichier('i2.bmp')

# Si les fichiers sont trouvés, lire les matrices et effectuer l'addition
if chemin_i1 and chemin_i2:
    matrice1 = lire_matrice_bmp(chemin_i1)
    matrice2 = lire_matrice_bmp(chemin_i2)

    # Limite maximale de valeur (par exemple 15 pour des images 4 bits)
    max_val = 1

    # Effectuer l'addition des matrices et limiter les valeurs à max_val
    resultat_addition = np.minimum(matrice1 + matrice2, max_val)

    # Sauvegarder l'image résultante dans le même répertoire
    chemin_resultat = os.path.join(os.path.dirname(chemin_i1), 'resultat_addiiton.bmp')
    ecrire_matrice_bmp(chemin_resultat, resultat_addition)

    print(f"Addition des matrices réussie et enregistrée dans '{chemin_resultat}'")
else:
    print("Un ou plusieurs fichiers sont introuvables dans le répertoire du script.")
