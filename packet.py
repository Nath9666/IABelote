import random
import card as c

class Paquet:
    def __init__(self):
        self.cartes = []
        self.valeurs = ["A","7", "8", "9", "10", "V", "D", "R"]
        self.couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
        self.creer_paquet()

    def creer_paquet(self):
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.cartes.append(c.Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.cartes)

    def tirer_carte(self):
        return self.cartes.pop()
    
    def to_string(self):
        for carte in self.cartes:
            print(carte.to_string())