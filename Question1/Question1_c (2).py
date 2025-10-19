import numpy as np
import os

# Fonction pour lire la matrice depuis un fichier P2 (format PGM ASCII)
def lire_matrice_p2(fichier):
    with open(fichier, 'r') as f:
        # Lire l'en-tête P2 et ignorer les commentaires
        while True:
            ligne = f.readline().strip()
            if ligne == 'P2':
                break
            if ligne.startswith('#'):  # Ignorer les commentaires
                continue

        # Lire la taille de l'image (dimensions)
        dimensions = f.readline().strip().split()
        lignes = int(dimensions[0])
        colonnes = int(dimensions[1])

        # Lire la valeur maximale (souvent 255 pour des images en niveaux de gris)
        max_val = int(f.readline().strip())

        # Lire les éléments de la matrice (pixels)
        matrice = [list(map(int, ligne.strip().split())) for ligne in f.readlines()]
    
    return np.array(matrice), max_val

# Fonction pour écrire la matrice dans un fichier P2 (format PGM ASCII)
def ecrire_matrice_p2(fichier, matrice, max_val):
    with open(fichier, 'w') as f:
        f.write('P2\n')
        f.write(f"{matrice.shape[1]} {matrice.shape[0]}\n")  # dimensions : colonnes x lignes
        f.write(f"{max_val}\n")  # valeur maximale (par exemple 255)
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

# Chercher le fichier BMP dans le répertoire du script
chemin_image = chercher_fichier('i.bmp')

# Si le fichier est trouvé, lire la matrice et effectuer l'opération
if chemin_image:
    matrice, max_val = lire_matrice_p2(chemin_image)

    # Limiter la valeur maximale pour l'opération (par exemple, 15 pour une image 4 bits)
    max_val = 15

    # Effectuer la multiplication de la matrice par 2 et limiter la valeur maximale à max_val
    resultat_multiplication = np.minimum(matrice * 2, max_val)

    # Sauvegarder l'image résultante dans le même répertoire
    chemin_resultat = os.path.join(os.path.dirname(chemin_image), 'resultat_multiplication.pgm')
    ecrire_matrice_p2(chemin_resultat, resultat_multiplication, max_val)

    print(f"Multiplication des matrices réussie et enregistrée dans '{chemin_resultat}'")
else:
    print("Le fichier 'i.bmp' est introuvable dans le répertoire du script.")
