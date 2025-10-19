import numpy as np

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

# Exemple d'utilisation
matrice, max_val = lire_matrice_p2('i.bmp')  # Remplacer 'i.bmp' par le nom de votre fichier image

# Valeur maximale pour limiter le résultat (par exemple, 15 pour une image 4 bits)
max_val = 15

# Effectuer la multiplication de la matrice par 2 (et limiter la valeur maximale à 15)
resultat_multiplication = np.minimum(matrice * 2, max_val)  # Limiter à la valeur maximale (par exemple 15)

# Écrire le résultat dans un nouveau fichier PGM
ecrire_matrice_p2('resultat_multiplication.pgm', resultat_multiplication, max_val)
