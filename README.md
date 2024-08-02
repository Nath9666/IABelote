# Projet pour la détection de feuille de marquage de belote

## Objectif

L'objectif est de faciliter la détection de feuille de marquage de belote en utilisant des algorithmes de traitement d'image.

## Liens utiles

- [Aide](https://www.kaggle.com/code/basu369victor/kuzushiji-recognition-just-like-digit-recognition)
- [Introduction to CNN Keras](https://www.kaggle.com/code/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)
- [MNIST - Deep Neural Network with Keras](https://www.kaggle.com/code/prashant111/mnist-deep-neural-network-with-keras)
- [Offline Handwritten Text](https://www.kaggle.com/code/aman10kr/offline-handwritten-text-ocr)
- [Deep Neural Network Keras way](https://www.kaggle.com/code/poonaml/deep-neural-network-keras-way/notebook)

## La feuille

Dans un premier temps, nous décidons de quel type de feuille de marquage nous voulons.

Voir les fichiers :

- [Feuille de marquage PNG](./externe/FeuilleMarquage.png)
- [Feuille de marquage PDF](./externe/FeuilleMarquage.pdf)
- [Feuille de marquage XLSX](./externe/FeuilleMarquage.xlsx)
- [Feuille de marquage CSV](./externe/FeuilleMarquage.csv)

## La détection

Pour la détection, nous utilisons des algorithmes de traitement d'image.

### Détection de la feuille

Pour la détection de la feuille, nous utilisons un algorithme de détection de contour, pour la détecter automatiquement.

Couplé à un algorithme de CNN, nous pouvons vérifier si la feuille est bien détectée et dans le bon sens.

#### 1. `DETECTSHEET.PY`

Ce fichier contient le code pour détecter les contours d'une feuille de marquage dans une image ou une vidéo.

##### Fonctionnalités :
- Conversion de l'image en niveaux de gris.
- Application d'un flou gaussien.
- Détection des contours.
- Dessin des contours détectés.
- Sauvegarde des images avec contours détectés.

### Détection des points

Pour la détection des points, nous utilisons un algorithme de CNN afin de vérifier si les points sont corrects.

### 1. `DETECTANDRECONIZEDIGITSMODEL.PY`

Ce fichier contient le code pour entraîner un modèle de reconnaissance de chiffres en utilisant les données MNIST et un SVM optimisé.

#### Fonctionnalités :
- Chargement des données MNIST.
- Prétraitement des images.
- Entraînement d'un modèle SVM avec un pipeline de prétraitement.
- Évaluation du modèle.
- Sauvegarde du modèle entraîné.

### 2. `DETECTANDRECONIZEDIGITS.PY`

Ce fichier utilise le modèle entraîné pour détecter et reconnaître les chiffres dans une image donnée.

#### Fonctionnalités :
- Détection des chiffres dans une image.
- Encadrement des chiffres détectés.
- Reconnaissance des chiffres en utilisant le modèle SVM.
- Affichage des résultats.

## L'application

L'application est une application web et C# (pour le front) et python pour le back qui permet de détecter les feuilles de marquage de belote, afin de calculer les points par joueurs et d'afficher un classement.

Elle est fournie avec un [support externe](./externe/support.md) pour les utilisateurs et un [appareil photo](./externe/plan.png) pour la détection.
Vous les retrouver également sur le site [web](https://www.google.com).