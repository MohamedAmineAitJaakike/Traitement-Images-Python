from PIL import Image
import numpy as np
from os import path

def convert_image(image_path, output_path, mode, bits=None):
    # Vérifier si l'image existe
    if not path.isfile(image_path):
        print("Le chemin de l'image est invalide ou le fichier n'existe pas.")
        return

    # Ouvrir l'image
    img = Image.open(image_path)

    if mode == 'binaire':
        # Convertir en image binaire
        img = img.convert('1')  # Mode '1' pour binaire
    elif mode == 'niveau_de_gris':
        # Convertir en niveaux de gris
        img = img.convert('L')  # Mode 'L' pour niveaux de gris

        if bits is not None:
            # Appliquer le nombre de bits
            max_val = 2**bits - 1
            img = img.point(lambda x: (x // (256 // (max_val + 1))) * (256 // (max_val + 1)))

    # Sauvegarder l'image convertie
    img.save(output_path)
    print(f"L'image a été enregistrée sous : {output_path}")

def main():
    image_path = input("Entrez le chemin complet de l'image à convertir (par exemple, /chemin/vers/image.jpg) : ")
    output_path = input("Entrez le chemin complet de sortie de l'image convertie (par exemple, /chemin/vers/image_convertie.jpg) : ")
    mode = input("Choisissez le mode (binaire/niveau_de_gris) : ").strip().lower()

    if mode == 'niveau_de_gris':
        bits = int(input("Entrez le nombre de bits (1-8) pour l'image en niveaux de gris : "))
        if bits < 1 or bits > 8:
            print("Le nombre de bits doit être entre 1 et 8.")
            return
    else:
        bits = None

    convert_image(image_path, output_path, mode, bits)

if __name__ == "__main__":
    main()
