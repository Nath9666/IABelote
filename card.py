import pygame

class Carte:
    def __init__(self, valeur:str, couleur:str):
        """! Constructeur de la classe Carte

        @param valeur: La valeur de la carte
        @param couleur: La couleur de la carte

        @return une instance de la classe Carte
        
        """
        self.x = 50
        self.y = 50
        self.rotationX = 0
        self.rotationY = 0
        self.valeur = valeur
        self.couleur = couleur
        self.owner = None
        self.font = pygame.font.Font(None, 36)
        self.point = self.get_point()

    def to_string(self):
        """! Méthode pour afficher la carte

        @return une chaine de caractère contenant la valeur et la couleur de la carte
            
        """
        return self.valeur + " de " + self.couleur
    
    # [ ]: faire les image de carte
    def dessiner_carte(self, ecran:pygame.Surface):
        """! Méthode pour dessiner une carte
        
        @param ecran: L'écran sur lequel dessiner la carte

        @return une carte dessinée sur l'écran
        """
        # Créer un rectangle
        rect = pygame.Surface((100, 200))
    
        # Changer la couleur en fonction de la couleur de la carte
        if self.couleur in ["Carreau", "Coeur"]:
            rect.fill((255, 0, 0))  # Rouge
        else:
            rect.fill((255, 255, 255))  # Blanc
    
        # Créer une surface avec la valeur
        valeur_surface = self.font.render(self.valeur, True, (0, 0, 0))
        rect.blit(valeur_surface, (10, 10))
    
        # Créer une surface avec la couleur
        couleur_surface = self.font.render(self.couleur, True, (0, 0, 0))
        rect.blit(couleur_surface, (10, 50))
    
        # Appliquer la rotation
        rect = pygame.transform.rotate(rect, self.rotationX)
    
        # Dessiner le rectangle sur l'écran
        ecran.blit(rect, (self.x, self.y))

    def bouger(self, x:float, y:float):
        """! Méthode pour bouger une carte
        
        @param x: La valeur de déplacement en x
        @param y: La valeur de déplacement en y
        
        @return une carte déplacée
        """
        self.x += x
        self.y += y

    def tourner(self, x:float, y:float):
        """! Méthode pour tourner une carte
        
        @param x: La valeur de rotation en x
        @param y: La valeur de rotation en y
        
        @return une carte tournée
        """
        self.rotationX += x
        self.rotationY += y

    def get_point(self):
        """! Méthode pour obtenir le point d'une carte

        @return le point de la carte
        """
        if self.valeur == "A":
            self.point = 11
        elif self.valeur == "7":
            self.point = 0
        elif self.valeur == "8":
            self.point = 0
        elif self.valeur == "9":
            self.point = 0
        elif self.valeur == "10":
            self.point = 10
        elif self.valeur == "V":
            self.point = 2
        elif self.valeur == "D":
            self.point = 3
        elif self.valeur == "R":
            self.point = 4
        return self.point