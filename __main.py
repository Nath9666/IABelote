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

take_action = [
    "Carreau",
    "Coeur",
    "Pique",
    "Trefle"
    "Pass"
    "0",
    "1"
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
]

# Dictionnaire pour mapper les touches aux actions
button_toAction = {
    pygame.K_0: 0,
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_KP0: 0,
    pygame.K_KP1: 1,
    pygame.K_KP2: 2,
    pygame.K_KP3: 3,
    pygame.K_KP4: 4,
    pygame.K_KP5: 5,
    pygame.K_KP6: 6,
    pygame.K_KP7: 7,
}

# Créer un objet horloge
horloge = pygame.time.Clock()

# Boucle de jeu
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            # Vérifie si la touche pressée est dans le dictionnaire
            if event.key in button_toAction:
                # Récupère le numéro de la carte
                card_number = button_toAction[event.key]

                # Vérifie si le numéro de la carte est inférieur au nombre de cartes que le joueur a
                if card_number < len(curent_player.hand):
                    # Joue la carte correspondante à la touche pressée
                    tapis.add_card(curent_player.play_card(card_number))
                    print(str(tapis.get_points()))
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