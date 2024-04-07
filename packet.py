import random
import card as c

class Paquet:
    def __init__(self, screen_dimension:tuple):
        """! Constructeur de la classe Paquet
        @param screen_dimension: Les dimensions de l'écran
        
        @return une instance de la classe Paquet
        """
        self.cartes = []
        self.valeurs = ["A","7", "8", "9", "10", "V", "D", "R"]
        self.couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
        self.atout = None
        self.creer_paquet(screen_dimension)

    def creer_paquet(self, screen_dimension:tuple):
        """! Méthode pour créer un paquet de cartes
        @param screen_dimension: Les dimensions de l'écran
        
        @return un paquet de cartes
        """
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.cartes.append(c.Carte(valeur, couleur, screen_dimension))

    def melanger(self):
        """! Méthode pour mélanger les cartes

        @return un paquet de cartes mélangées
        """
        random.shuffle(self.cartes)

    def tirer_carte(self):
        """! Méthode pour tirer une carte
        
        @return une carte tirée"""
        return self.cartes.pop()
    
    def to_string(self):
        """! Méthode pour afficher les cartes
        
        @return une chaine de caractère contenant les cartes
        """
        for carte in self.cartes:
            print(carte.to_string())

    def define_atout(self, atout:str):
        """! Méthode pour définir l'atout
        @param atout: L'atout
        
        @return l'atout
        """
        self.atout = atout
        for carte in self.cartes:
            if carte.couleur == atout:
                carte.atout = True
        return self.atout