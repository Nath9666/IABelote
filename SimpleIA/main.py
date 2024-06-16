import gym
import tensorflow as tf
from tensorflow import keras
import pygame
import numpy as np

# Créer l'environnement Gym
env = gym.make('Pendulum-v1')

# Initialiser Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

# Définir le modèle d'IA avec TensorFlow
model = keras.Sequential([
    keras.layers.Dense(24, input_shape=(3,), activation='relu'),
    keras.layers.Dense(24, activation='relu'),
    keras.layers.Dense(1, activation='tanh')
])
optimizer = tf.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='mse')

def choose_action(state):
    """Choisir une action basée sur l'état actuel."""
    # S'assurer que 'state' est un tableau numpy à une dimension de taille 3
    state = np.array(state).flatten()  # Aplatir 'state' au cas où
    if state.shape[0] != 3:
        raise ValueError(f"L'état doit être de forme (3,), forme reçue: {state.shape}")
    scaled_action = model.predict(np.array([state]))[0]
    action = scaled_action * 2 - 1  # Scale de l'action entre -1 et 1
    return [action]

# Boucle principale
while True:
    # Obtenir l'état actuel de l'environnement
    observation = env.reset()
    
    for _ in range(1000):
        # Afficher l'état actuel avec Pygame
        screen.fill((0, 0, 0))
        # Convertir l'observation en une représentation visuelle
        # (Ceci est un exemple simplifié. Vous devrez adapter ceci pour visualiser l'état correctement.)
        pygame.draw.circle(screen, (255, 0, 0), (250, 250), 20)
        pygame.display.flip()
        
        # Choisir une action avec le modèle d'IA
        action = choose_action(observation)
        
        # Appliquer l'action à l'environnement
        observation, reward, done, info = env.step(action)
        
        # Mettre à jour l'interface graphique avec Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if done:
            break