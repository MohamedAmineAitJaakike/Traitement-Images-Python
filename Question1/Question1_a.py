import numpy as np

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

# Exemple d'utilisation
matrice1 = lire_matrice_bmp('i1.bmp')
matrice2 = lire_matrice_bmp('i2.bmp')

# Limite maximale de valeur (par exemple 15 pour des images 4 bits)
max_val = 15

# Effectuer l'addition des matrices et limiter les valeurs à max_val
resultat_addition = np.minimum(matrice1 + matrice2, max_val)

# Écrire le résultat dans un fichier BMP
ecrire_matrice_bmp('resultat_addition.bmp', resultat_addition)
