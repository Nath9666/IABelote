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
ajust = 0.8

# Set up the screen
pygame.display.set_caption("Jeu de belote")
screen = pygame.display.set_mode((screen_height*ajust, screen_height*ajust))
dimension = (screen.get_width(), screen.get_height())

game = True

# Create a deck
deck = p.Paquet(dimension)
deck.melanger()
deck.define_atout("Carreau")

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
tapis.add_card(deck.tirer_carte())

take_action = [
    "Carreau",
    "Coeur",
    "Pique",
    "Trefle"
    "Pass"
    "O"
    "N"
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
    pygame.K_o:"O",
    pygame.K_n:"N",
    pygame.K_c:"Carreau",
    pygame.K_h:"Coeur",
    pygame.K_p:"Pique",
    pygame.K_t:"Trefle"}

# Créer un objet horloge
horloge = pygame.time.Clock()

# Layer du jeu
## 0: Menu
## 1: Premier Tour
## 2: Deuxieme Tour
## 3: Le jeu
layer = 1

# Boucle de jeu
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            # Vérifie si la touche pressée est dans le dictionnaire
            if event.key in button_toAction and layer == 3:
                # Récupère le numéro de la carte
                card_number = button_toAction[event.key]
                # Vérifie si le numéro de la carte est inférieur au nombre de cartes que le joueur a
                if card_number < len(curent_player.hand):
                    # Joue la carte correspondante à la touche pressée
                    tapis.add_card(curent_player.play_card(card_number))
                    print(str(tapis.get_points()))
                    index_player += 1
                    curent_player = List_players[index_player % 4]
            if event.key in button_toAction and layer == 1:
                # Récupère l'action
                action = button_toAction[event.key]
                # Vérifie si l'action est un atout
                if action in take_action[:4]:
                    # Définir l'atout
                    deck.define_atout(action)
                    layer = 3
                # Vérifie si l'action est un passe
                elif action == "Pass":
                    # Passe au joueur suivant
                    index_player += 1
                    curent_player = List_players[index_player % 4]
                    # Vérifie si le donneur est le dernier joueur
                    if index_player == 0:
                        # Passe au deuxième tour
                        layer = 2
                # Vérifie si l'action est un O
                elif action == "O":
                    # Passe au joueur suivant
                    index_player += 1
                    curent_player = List_players[index_player % 4]
                    deck.define_atout(tapis.cards[0].couleur)
                    # Passe au deuxième tour
                    layer = 2
                # Vérifie si l'action est un N
                elif action == "N":
                    # Passe au joueur précédent
                    index_player -= 1
                    curent_player = List_players[index_player % 4]
                    # Passe au deuxième tour
                    layer = 2

    # Effacer l'écran
    screen.fill(c.BLACK)  # Remplit l'écran avec la couleur noire

    # Dessiner les joueurs
    for i, player in enumerate(List_players):
        player.dessiner_player(screen, dimension[0]/2, dimension[1]/2, i*90)

    if layer == 0:
        # Dessiner le menu
        pass
    elif layer == 1:
        # Dessiner le premier tour
        tapis.draw_tapis(screen)
        curent_player.prendre_atout(screen, tapis.cards[0].couleur)        
    elif layer == 2:
        # Dessiner le deuxieme tour
        pass
    elif layer == 3:
        # Dessiner le tapis
        tapis.draw_tapis(screen)
        tapis.draw_team_point(screen)

    pygame.display.flip()

    # Limiter le taux de rafraîchissement à 24 images par seconde
    horloge.tick(24)