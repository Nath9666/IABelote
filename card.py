import pygame
import color as c

class Carte:
    def __init__(self, valeur:str, couleur:str, screen_dimension:tuple):
        """! Constructeur de la classe Carte

        @param valeur: La valeur de la carte
        @param couleur: La couleur de la carte
        @param screen_dimension: Les dimensions de l'écran

        @return une instance de la classe Carte
        
        """
        self.x = 50
        self.y = 50
        self.rotationX = 0
        self.rotationY = 0
        self.valeur = valeur
        self.couleur = couleur
        self.owner = None
        self.atout = False
        self.font = pygame.font.Font(None, int(36*screen_dimension[0]/1080))
        self.height = 200*screen_dimension[1]/1080
        self.width = 100*screen_dimension[0]/1080
        self.point = self.get_point()

    def to_string(self):
        """! Méthode pour afficher la carte

        @return une chaine de caractère contenant la valeur et la couleur de la carte
            
        """
        return f"{self.valeur} de {self.couleur}"
    
    def dessiner_carte(self, ecran:pygame.Surface):
        """! Méthode pour dessiner une carte
        
        @param ecran: L'écran sur lequel dessiner la carte

        @return une carte dessinée sur l'écran
        """
        rect = pygame.Surface((self.width, self.height))
        rect.fill(c.RED if self.couleur in ["Carreau", "Coeur"] else c.WHITE)
        rect.blit(self.font.render(self.valeur, True, c.BLACK), (10, 10))
        rect.blit(self.font.render(self.couleur, True, c.BLACK), (10, 50))
        rect = pygame.transform.rotate(rect, self.rotationX)
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
        if self.atout:
            points = {
                "A": 11,
                "7": 0,
                "8": 0,
                "9": 14,
                "10": 10,
                "V": 20,
                "D": 3,
                "R": 4
            }
            return points.get(self.valeur, 0)
        
        points = {
            "A": 11,
            "7": 0,
            "8": 0,
            "9": 0,
            "10": 10,
            "V": 2,
            "D": 3,
            "R": 4
        }
        return points.get(self.valeur, 0)