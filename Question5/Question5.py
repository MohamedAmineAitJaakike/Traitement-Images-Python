import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import generic_filter
from os import path

def nagao_filter_optimized(image):
    # Fonction qui calcule la variance dans une fenêtre de taille 3x3
    def local_variance(window):
        return np.var(window)

    # Fonction qui calcule la moyenne dans la sous-fenêtre ayant la variance minimale
    def nagao_operation(window):
        window = window.reshape(5, 5)
        sub_windows = [window[i:i+3, j:j+3].flatten() for i in range(3) for j in range(3)]
        variances = np.array([local_variance(sw) for sw in sub_windows])
        min_variance_idx = np.argmin(variances)
        return np.mean(sub_windows[min_variance_idx])

    # Utiliser generic_filter pour appliquer le filtre de Nagao
    filtered_image = generic_filter(image, nagao_operation, size=5)
    return filtered_image.astype(np.uint8)

# Demander à l'utilisateur d'entrer le chemin de l'image
image_path = input("Entrez le chemin de l'image (ex: suburb_g.png, suburb_g.jpg) : ")

if not path.exists(image_path):
    print("Image non trouvée !")
    exit()

# Lire l'image en niveaux de gris
image = Image.open(image_path).convert('L')
image = np.array(image)

# Appliquer le filtre de Nagao 
filtered_image = nagao_filter_optimized(image)

# Afficher l'image originale et l'image filtrée
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Image originale")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Image filtrée (Filtre de Nagao)")
plt.imshow(filtered_image, cmap='gray')
plt.axis('off')

plt.show()

# Sauvegarder l'image filtrée
output_path = input("Entrez le chemin de sortie pour l'image filtrée (ex: suburb_gn.png, suburb_gn.jpg) : ")
filtered_image_pil = Image.fromarray(filtered_image)
filtered_image_pil.save(output_path)

print(f"L'image filtrée a été sauvegardée sous {output_path}.")
