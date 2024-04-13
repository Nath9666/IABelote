import pygame
import math
import color as c
class Player:
    def __init__(self, name:str):
        """! Constructeur de la classe Player
        
        @param name: Le nom du joueur
        
        @return une instance de la classe Player
        """
        self.name = name
        self.donneur = False
        self.point_InHand = 0
        self.hand = []

    def receive_card(self, card:object):
        """! Méthode pour recevoir une carte
        
        @param card: La carte à recevoir
        
        @return la carte reçue
        """
        self.hand.append(card)
        self.point_InHand += card.point
        self.hand[len(self.hand)-1].owner = self

    def to_string(self):
        """! Méthode pour afficher les cartes du joueur
        
        @return une chaine de caractère contenant les cartes du joueur
        """
        print("Player: " + self.name)
        for card in self.hand:
            print(card.to_string())

    def play_card(self, index:int):
        if index >= len(self.hand):
            return None
        return self.hand.pop(index)
    
    def dessiner_player(self, screen:pygame.Surface, centre_x:float, centre_y:float, angle:float):
        """! Méthode pour dessiner un joueur
        
        @param screen: L'écran sur lequel dessiner le joueur
        @param centre_x: La position x du centre du joueur
        @param centre_y: La position y du centre du joueur
        @param angle: L'angle de rotation du joueur
        
        @return un joueur dessiné sur l'écran
        """
        # Carrer de 10*10
        pygame.draw.rect(screen, c.WHITE, (centre_x - 5, centre_y - 5, 10, 10))

        cercle1 = 200 * screen.get_width() / 1080
        cercle2 = 50 * screen.get_width() / 1080

        # Definit la donné du rayon du cercle
        if screen.get_width() > screen.get_height():
            rayon = screen.get_height() / 2 - cercle1
        else :
            rayon = screen.get_width() / 2 - cercle1

        # Dessine un cercle de 100 de rayon
        pygame.draw.circle(screen, c.WHITE, (int(centre_x), int(centre_y)), rayon, 1)
        pygame.draw.circle(screen, c.WHITE, (int(centre_x), int(centre_y)), rayon-cercle2,1)

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
        if self.hand:  # Ajoutez cette ligne pour vérifier si la main du joueur n'est pas vide
            largeur_carte = self.hand[0].width
            longeur_carte = self.hand[0].height
            nb_cartes = len(self.hand)
            total_largeur = largeur_carte * nb_cartes

        # Dessine le nom
        font = pygame.font.Font(None, 36)

        for i, card in enumerate(self.hand):
            if angle == 90 or angle == 270:
                card.x = joueur_x + card.height
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

        
        if self.donneur:
            # Dessine son nom
            text = font.render(self.name, 1, c.RED)
        else:
            text = font.render(self.name, 1, c.WHITE)
        text = pygame.transform.rotate(text, angle)
        text_rect = text.get_rect(center=(text_x, text_y))
        screen.blit(text, text_rect)

    def prendre_atout(self, screen:pygame.Surface, atout:str):
        """! Méthode pour prendre l'atout
        
        @param screen: L'écran sur lequel afficher l'atout
        @param atout: L'atout à prendre
        """
        font = pygame.font.Font(None, 36)
        name = font.render(self.name, 1, c.WHITE)
        text = font.render(f"Prendre l'atout {atout} ?", 1, c.WHITE)
        text2 = font.render("Oui: O | Non: N", 1, c.WHITE)
        text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
        text2_rect = text2.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 50))
        name_rect = name.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 - 50))
        screen.blit(text, text_rect)
        screen.blit(text2, text2_rect)
        screen.blit(name, name_rect)