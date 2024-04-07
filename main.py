import pygame
import packet as p
import player as pl
import tapis as tp
import color as c

# Initialize the game
pygame.init()

# Get screen info
infoObject = pygame.display.Info()

# Get screen size
screen_width, screen_height = infoObject.current_w, infoObject.current_h

print(f"Screen size: {screen_width}x{screen_height}")

# Set up the screen
pygame.display.set_caption("Jeu de belote")
screen = pygame.display.set_mode((screen_height-40, screen_height-40))
dimension = (screen.get_width(), screen.get_height())

game = True

# Create a deck
deck = p.Paquet(dimension)
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

# [ ]: mettre en place le systeme de tour de pris
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                tapis.add_card(curent_player.play_card(0))
                print("Player 1" + str(tapis.get_points()))
                index_player += 1
                curent_player = List_players[index_player % 4]

    # Effacer l'écran
    screen.fill(c.BLACK)  # Remplit l'écran avec la couleur noire

    # Dessiner les joueurs
    for i, player in enumerate(List_players):
        player.dessiner_player(screen, dimension[0]/2, dimension[1]/2, i*90)

    # Dessiner le tapis
    tapis.draw_tapis(screen)

    pygame.display.flip()

    # Limiter le taux de rafraîchissement à 24 images par seconde
    horloge.tick(24)