# Projet pour la detection de feuille de marquage de belote

## Objectif

L'objectif est de faciliter la detection de feuille de marquage de belote en utilisant des algorithmes de traitement d'image.

[Aide](https://www.kaggle.com/code/basu369victor/kuzushiji-recognition-just-like-digit-recognition)

## La feuille

Dans un premier temps, nous decidons de quel type de feuille de marquage nous voulons.

Voir les fichiers :

- [Feuille de marquage PNG ](./externe/FeuilleMarquage.png)
- [Feuille de marquage PDF ](./externe/FeuilleMarquage.pdf)
- [Feuille de marquage XLSX](./externe/FeuilleMarquage.xlsx)
- [Feuille de marquage CSV ](./externe/FeuilleMarquage.csv)

## La detection

Pour la detection, nous utilisons des algorithmes de traitement d'image.

### Detection de la feuille

Pour la detection de la feuille, nous utilisons un algorithme de detection de contour, pour la detecter automatiquement.

Coupler a un algorithme de CNN, nous pouvons verifier si la feuille est bien detectee et dans le bon sens.

### Detection des points

Pour la detection des points, nous utilisons un algorithme de CNN afin de verfier si les points sont correcte.

## L'application

L'application est une application web(ou python) qui permet de detecter les feuilles de marquage de belote, Afin de calculer les points par joueurs et d'afficher un classement.

Elle est founir avec un [support externe](./externe/support.md) pour les utilisateurs et un [appareils photo](./externe/plan.png) pour la detection.
