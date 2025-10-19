<<<<<<< HEAD
# traitement-d-images

Ce dépôt contient des scripts Python pour effectuer diverses tâches de traitement d'images. Le projet couvre des opérations telles que la manipulation d'images binaires et en niveaux de gris, la création d'histogrammes, la conversion d'images, ainsi que l'application de filtres. Il vise à fournir une compréhension pratique des techniques fondamentales du traitement d'images en utilisant Python.
=======

<h1 align="center">Projet : Traitement d'Images avec Python</h1>

<p align="center">
  Une collection de scripts Python explorant les techniques fondamentales du traitement d'images. 
  <br />
  Ce projet couvre la manipulation, la conversion, l'analyse (histogrammes) et le filtrage d'images en utilisant <strong>OpenCV</strong> et <strong>Matplotlib</strong>.
</p>

<p align="center">
  <img src="demo/image-processing-demo.gif" alt="Démo animée du traitement d'images" width="85%"/>
</p>

---

## ✨ Fonctionnalités Principales

Ce projet fournit des scripts pour :
* **🎨 Conversion d'Images :** Convertir des images RGB en niveaux de gris (`grayscale`) et en binaire (`binary thresholding`).
* **📊 Analyse d'Histogrammes :** Générer et afficher les histogrammes d'images pour analyser la distribution des pixels.
* **🔧 Manipulation de Base :** Redimensionner (`resize`), rogner (`crop`), et faire pivoter (`rotate`) des images.
* **🔬 Application de Filtres :**
    * Filtres de lissage (Flou Gaussien, Flou Médian) pour réduire le bruit.
    * Filtres de détection de contours (Sobel, Canny).
* **🔢 Opérations Arithmétiques :** Additionner ou soustraire des images.

---

## 🛠️ Technologies et Bibliothèques

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/Matplotlib-3175A2?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib"/>
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
</p>

---

## 🚀 Installation et Lancement

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/MohamedAmineAitJaakike/Traitement-Images-Python.git
    cd traitement-d-images
    ```

2.  **Créer un environnement virtuel (Recommandé) :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3.  **Installer les dépendances :**
    Ce projet nécessite les bibliothèques listées ci-dessous. (Vous devriez créer un fichier `requirements.txt`).
    ```bash
    pip install opencv-python-headless
    pip install matplotlib
    pip install numpy
    ```

---

## 🏃 Exécution des Scripts

Les scripts sont conçus pour être exécutés individuellement depuis le terminal.

1.  Placez les images que vous souhaitez traiter dans un dossier (ex: `images/`).
2.  Exécutez le script de votre choix :

    ```bash
    # Exemple pour appliquer un filtre
    python scripts/appliquer_filtre.py images/mon_image.jpg

    # Exemple pour générer un histogramme
    python scripts/generer_histogramme.py images/mon_image.jpg
    ```

---

## 📂 Structure du Projet (Suggérée)

```
traitement-d-images/
├── scripts/                # Tous les scripts Python (.py)
│   ├── conversion.py
│   ├── filtres.py
│   ├── histogramme.py
│   └── manipulation.py
│
├── images/                 # Images d'entrée pour les tests
├── resultats/              # Images de sortie générées par les scripts
├── demo/                   # Contient le GIF animé pour le README
│
├── requirements.txt        # Liste des dépendances pip
└── README.md               # Ce fichier
```

---

## 🧑‍💻 Auteur

* **Mohamed Amine AIT JAAKIK**
* `mohamedamine.aitjaakike@etu.uae.ac.ma`
* ENSA Tétouan - Université Abdelmalek Essaâdi
>>>>>>> 3bd8026899217d5e3c0947a658e7a2ee0138c97e
