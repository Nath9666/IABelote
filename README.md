# IA Belote

## Description

Ce projet à pour but de faire apprendre à une IA à jouer à la belote. Pour cela, nous avons utilisé un algorithme de renforcement, le Q-learning.
Il pemert également d'explorer la programtions orientée objet mais aussi le fait de develloper une IA basée sur le Q-learning.

A noter : Ce projet est un projet personnel et n'a pas pour but d'être utilisé en production.

Il existe plusieurs versions de la belote, nous avons choisi de nous baser sur la belote avec une variantes concernant la vache folle.

### Règles de la belote
Pour faire le programme de l'IA, il est nécessaire de comprendre les règles de la belote. Voici un résumé des règles de la belote :
[règles de la belote](https://www.ffbelote.org/regles-officielle-belote/)

#### Règles de la vache folle

Dans cette variantes, si personne n'as pris durant le deuxième tour de prises alors c'est le conneur qui prends.
Cela apporte une difficulté supplémentaire pour l'IA.

## Installation

Pour installer le projet, il suffit de cloner le dépôt git et d'installer les dépendances.

```bash
pip install nes-py
pip install gym-super-mario-bros
```

## Recréation du jeu

Dans un premier temps, nous avons recrée le jeu de la belote en python.
les fichiers `card.py` et `deck.py` permettent de créer les cartes et le paquet de cartes.

Quand on fichier `player.py` permet de créer un joueur.

## IA 

Noous nous sommes basée sur cette video [IA play mario](https://youtu.be/2eeYqJ0uBKE)

Avec en plus le code [IA marrio code](https://github.com/nicknochnack/MarioRL/blob/main/Mario%20Tutorial.ipynb)