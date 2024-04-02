import pygame
import packet as p
import player as pl

# Initialize the game
pygame.init()

# Set up the screen
pygame.display.set_caption("Jeu de belote")
screen = pygame.display.set_mode((800, 600))
dimension = [screen.get_width(), screen.get_height()]

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game = True
Player1 = pl.Player("Nathan")

# Create a deck
deck = p.Paquet()
deck.melanger()
print(deck.to_string())


# Créer un objet horloge
horloge = pygame.time.Clock()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # Effacer l'écran
    screen.fill((0, 0, 0))  # Remplit l'écran avec la couleur noire


    pygame.display.flip()

    # Limiter le taux de rafraîchissement à 24 images par seconde
    horloge.tick(24)