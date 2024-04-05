import pygame

class Carte:
    def __init__(self, valeur, couleur):
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
        return self.valeur + " de " + self.couleur
    
    def dessiner_carte(self, ecran):
        # Créer un rectangle
        rect = pygame.Surface((100, 200))
        rect.fill((255, 255, 255))

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

    def bouger(self, x, y):
        self.x += x
        self.y += y

    def tourner(self, x, y):
        self.rotationX += x
        self.rotationY += y

    def get_point(self):
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