import pygame

class Tapis:
    def __init__(self):
        self.cards = []
        self.font = pygame.font.Font(None, 36)

    def add_card(self, card):
        self.cards.append(card)

    def draw_tapis(self, screen):
        for __, card in enumerate(self.cards):
            card.x = screen.get_width() / 2
            card.y = screen.get_height() / 2
            #card.rotationX = 0
            card.dessiner_carte(screen)

    def get_points(self):
        points = 0
        for card in self.cards:
            points += card.point
        return points