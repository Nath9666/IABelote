import pygame

class Tapis:
    def __init__(self):
        """! Constructeur de la classe Tapis
        
        @return une instance de la classe Tapis
        """
        self.cards = []
        self.font = pygame.font.Font(None, 36)

    def add_card(self, card:object):
        """! Méthode pour ajouter une carte au tapis

        @param card: La carte à ajouter
        """
        self.cards.append(card)

    def draw_tapis(self, screen:pygame.Surface):
        """! Méthode pour dessiner le tapis
        
        @param screen: L'écran sur lequel dessiner le tapis
        
        @return un tapis dessiné sur l'écran
        """
        if len(self.cards) == 0:
            return
        if len(self.cards) ==4:
            self.cards.clear()
        for __, card in enumerate(self.cards):
            card.x = screen.get_width() / 2
            card.y = screen.get_height() / 2
            card.dessiner_carte(screen)

    def get_points(self):
        """! Méthode pour obtenir les points du tapis
        
        @return les points du tapis
        """
        points = 0
        for card in self.cards:
            points += card.point
        return points