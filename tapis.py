import pygame
import math
import color as c

class Tapis:
    def __init__(self):
        """! Constructeur de la classe Tapis
        
        @return une instance de la classe Tapis
        """
        self.cards = []
        self.previous_card = None
        self.team1 = 0
        self.team2 = 0
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
        center_x = screen.get_width() / 2
        center_y = screen.get_height() / 2
        rayon = screen.get_height() / 8
        pygame.draw.circle(screen, c.WHITE, (int(center_x), int(center_y)), rayon, 1)
        if len(self.cards) == 0:
            return
        if len(self.cards) == 4:
            self.point_toTeam()
            self.previous_card = self.cards.copy()
            self.cards.clear()
        for __, card in enumerate(self.cards):
            if card.rotationX == 0:
                card.x = center_x
                card.y = center_y + rayon
            if card.rotationX == 90:
                card.x = center_x + rayon
                card.y = center_y
            if card.rotationX == 180:
                card.x = center_x
                card.y = center_y - rayon - card.height
            if card.rotationX == 270:
                card.x = center_x - rayon
                card.y = center_y
            card.dessiner_carte(screen)

    def draw_team_point(self, screen:pygame.Surface):
        """! Méthode pour dessiner les points des 2 équipes
            
        @return les points de l'équipe dessinés sur l'écran
        """
        team1_text = self.font.render(f"Équipe 1: {self.team1}", True, c.WHITE)
        team2_text = self.font.render(f"Équipe 2: {self.team2}", True, c.WHITE)

        screen.blit(team1_text, (screen.get_width() - team1_text.get_width() - 10, 10))
        screen.blit(team2_text, (screen.get_width() - team2_text.get_width() - 10, team1_text.get_height() + 20))

    def get_points(self):
        """! Méthode pour obtenir les points du tapis
        
        @return les points du tapis
        """
        points = 0
        for card in self.cards:
            points += card.point
        return points
    
    def point_toTeam(self):
        """! Méthode pour ajouter les points du tapis à l'équipe gagnante
        
        @return les points du tapis ajoutés à l'équipe gagnante
        """
        temp_card = self.cards[0]
        for card in self.cards:
            if temp_card.get_point() < card.get_point():
                temp_card = card
        
        print(f"La carte gagnante est: {temp_card.to_string()}")
        print(f"Jouer par {temp_card.owner.name}")

        if temp_card.owner.name in ["Player 1", "Player 3"]:
            self.team1 += self.get_points()
        else:
            self.team2 += self.get_points()
        