import gym_super_mario_bros

# Créer l'environnement Mario
env = gym_super_mario_bros.make("SuperMarioBros-1-1-v0")

# Boucle d'entraînement
for episode in range(10):
    state = env.reset()  # Réinitialiser l'environnement
    done = False  # Indicateur de fin d'épisode

    while not done:
        action = env.action_space.sample()  # Sélectionner une action aléatoire
        next_state, reward, done, info = env.step(action)  # Effectuer l'action dans l'environnement

        # Mettre à jour l'IA avec l'état actuel, l'action, la récompense et l'état suivant

        state = next_state  # Mettre à jour l'état actuel

    # Mettre à jour les paramètres de l'IA après chaque épisode

# Tester l'IA entraînée
state = env.reset()
done = False

while not done:
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    env.render()

env.close()