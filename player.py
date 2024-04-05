import pygame
import math
class Player:
    def __init__(self, name):
        self.name = name
        self.donneur = False
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)
        self.hand[len(self.hand)-1].owner = self

    def to_string(self):
        print("Player: " + self.name)
        for card in self.hand:
            print(card.to_string())

    def play_card(self, index):
        if index >= len(self.hand):
            return None
        return self.hand.pop(index)
    
    def dessiner_player(self, screen, centre_x, centre_y, angle):
        # Carrer de 10*10
        pygame.draw.rect(screen, (255, 255, 255), (centre_x - 5, centre_y - 5, 10, 10))

        cercle1 = 200
        cercle2 = 50

        # Definit la donné du rayon du cercle
        if screen.get_width() > screen.get_height():
            rayon = screen.get_height() / 2 - cercle1
        else :
            rayon = screen.get_width() / 2 - cercle1

        # Dessine un cercle de 100 de rayon
        pygame.draw.circle(screen, (255, 255, 255), (int(centre_x), int(centre_y)), rayon, 1)
        pygame.draw.circle(screen, (255, 255, 255), (int(centre_x), int(centre_y)), rayon-cercle2,1)

        # Convertir l'angle en radians
        if angle == 90 or angle == 270:
            angle_rad = math.radians(angle + 180 + 90)
        else:
            angle_rad = math.radians(angle+90)

        # Calculer la position du joueur
        joueur_x = centre_x + math.cos(angle_rad) * (rayon)
        joueur_y = centre_y + math.sin(angle_rad) * (rayon)

        # Calcule la position du texte joeur
        text_x = centre_x + math.cos(angle_rad) * (rayon - cercle2)
        text_y = centre_y + math.sin(angle_rad) * (rayon - cercle2)

        # Dessine les cartes
        largeur_carte = 100
        longeur_carte = 200
        nb_cartes = len(self.hand)
        total_largeur = largeur_carte * nb_cartes

        for i, card in enumerate(self.hand):
            if angle == 90 or angle == 270:
                card.x = joueur_x + 200
                card.y = joueur_y - total_largeur/2 + i * largeur_carte
                if angle == 90:
                    card.x = card.x - longeur_carte
                if angle == 270:
                    card.x = card.x - 2*longeur_carte
            else:
                card.x = joueur_x - total_largeur/2 + i * largeur_carte
                card.y = joueur_y
                if angle == 180:
                    card.y = card.y - longeur_carte
            card.rotationX = angle
            card.dessiner_carte(screen)

        # Dessine le nom
            font = pygame.font.Font(None, 36)
        if self.donneur:
            # Dessine son nom
            text = font.render(self.name, 1, (255, 0, 0))
        else:
            text = font.render(self.name, 1, (255, 255, 255))
        text = pygame.transform.rotate(text, angle)
        text_rect = text.get_rect(center=(text_x, text_y))
        screen.blit(text, text_rect)