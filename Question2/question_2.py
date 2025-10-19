import cv2 as cv
from matplotlib import pyplot as plt
from os import path

# Demander à l'utilisateur de saisir le chemin d'accès complet à l'image
print("Saisissez le chemin d'accès complet à l'image (par exemple, /chemin/vers/image.jpg): ")
imagePath = input()

# Vérifier si le fichier existe
if not path.exists(imagePath):
    print("Image non trouvée !")
    exit()

# Charger l'image
img = cv.imread(imagePath)

# Si l'image n'a pas été chargée correctement, sortir du programme
if img is None:
    print("Échec du chargement de l'image.")
    exit()

# Séparer les canaux de l'image (Bleu, Vert, Rouge)
b, g, r = cv.split(img)

# Afficher l'image dans une fenêtre
cv.imshow("Image", img)

# Tracer l'histogramme des canaux Bleu, Vert et Rouge
plt.figure()
plt.title("Histogramme des canaux de couleurs")
plt.xlabel("Valeur des pixels")
plt.ylabel("Fréquence")

# Tracer les histogrammes des canaux avec des couleurs correspondantes
plt.hist(b.ravel(), 256, [0, 256], color='blue', label='Canal Bleu')
plt.hist(g.ravel(), 256, [0, 256], color='green', label='Canal Vert')
plt.hist(r.ravel(), 256, [0, 256], color='red', label='Canal Rouge')

# Ajouter une légende pour chaque canal
plt.legend()

# Afficher le graphique
plt.show()

# Attendre une touche pour fermer la fenêtre d'affichage de l'image
cv.waitKey(0)
cv.destroyAllWindows()
