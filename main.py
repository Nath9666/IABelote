import pygame
import packet as p
import player as pl
import tapis as tp

# Initialize the game
pygame.init()

# Set up the screen
pygame.display.set_caption("Jeu de belote")
screen = pygame.display.set_mode((1080, 1080))
dimension = [screen.get_width(), screen.get_height()]

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game = True

# Create a deck
deck = p.Paquet()
deck.melanger()

# Create players
List_players = []
for i in range(4):
    List_players.append(pl.Player("Player " + str(i+1)))
    for j in range(5):
        List_players[i].receive_card(deck.tirer_carte())

List_players[0].donneur = True
index_player = 0
curent_player = List_players[index_player]

# Create tapis
tapis = tp.Tapis()

# Créer un objet horloge
horloge = pygame.time.Clock()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for card in tapis:
                print(card.to_string())
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tapis.add_card(curent_player.play_card(0))
                print("Player 1" + str(tapis.get_points()))
                index_player += 1
                curent_player = List_players[index_player % 4]

    # Effacer l'écran
    screen.fill((0, 0, 0))  # Remplit l'écran avec la couleur noire

    # Dessiner les joueurs
    for i, player in enumerate(List_players):
        player.dessiner_player(screen, dimension[0]/2, dimension[1]/2, i*90)

    # Dessiner le tapis
    tapis.draw_tapis(screen)

    pygame.display.flip()

    # Limiter le taux de rafraîchissement à 24 images par seconde
    horloge.tick(24)