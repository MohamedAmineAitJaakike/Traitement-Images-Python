from PIL import Image
import numpy as np
from os import path

# Demander à l'utilisateur de saisir le chemin complet de l'image
print("Entrez le chemin d'accès complet de l'image (par exemple, /chemin/vers/image.jpg): ")
nom_image = input()

# Vérifier si le fichier existe
if not path.exists(nom_image):
    print("Image introuvable !")
    exit()

# Ouvrir l'image
image = Image.open(nom_image)

# Vérifier si l'image est en mode RGB (couleur)
if image.mode != 'RGB':
    image = image.convert('RGB')

# Récupérer les dimensions de l'image
largeur, hauteur = image.size

# Convertir l'image en une matrice NumPy
pixels = np.array(image)

# Déterminer la valeur maximale des pixels en fonction du type d'encodage
if pixels.dtype == np.uint8:
    valeur_max = 255  # Codage sur 8 bits
elif pixels.dtype == np.uint16:
    valeur_max = 65535  # Codage sur 16 bits
else:
    # Autre codage (rare), on prend la valeur maximale trouvée
    valeur_max = pixels.max()

# Définir le chemin du fichier texte dans le même répertoire que l'image
repertoire_image = path.dirname(nom_image)
fichier_sortie = path.join(repertoire_image, "matrice_image.txt")

# Générer un fichier texte contenant le format PNM
with open(fichier_sortie, "w") as fichier:
    # Écrire l'en-tête P3
    fichier.write("P3\n")
    # Écrire les dimensions et la valeur maximale
    fichier.write(f"{largeur} {hauteur}\n{valeur_max}\n")
    # Écrire la matrice sous forme de triplets [R, G, B]
    for i in range(hauteur):
        ligne = "".join([f"[{pixels[i][j][0]}, {pixels[i][j][1]}, {pixels[i][j][2]}]" for j in range(largeur)])
        fichier.write(ligne + "\n")

# Confirmer à l'utilisateur que le fichier a été généré
print(f"Fichier généré avec succès ({fichier_sortie})")
print(f"Dimensions : {largeur}x{hauteur}")
print(f"Valeur maximale des pixels : {valeur_max}")
