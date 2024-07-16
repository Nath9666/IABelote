import matplotlib.pyplot as plt

def plot(historique, first_layer_name = "accuracy" , second_layer_name = "val_accuracy"):
    # Tracer la précision d'entraînement et de validation
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(historique.history[first_layer_name], label='Précision Entraînement')
    plt.plot(historique.history[second_layer_name], label='Précision Validation')
    plt.title('Précision du modèle en fonction du temps')
    plt.xlabel('Époques')
    plt.ylabel('Précision')
    plt.legend()

    # Tracer la perte d'entraînement et de validation
    plt.subplot(1, 2, 2)
    plt.plot(historique.history['loss'], label='Perte Entraînement')
    plt.plot(historique.history['val_loss'], label='Perte Validation')
    plt.title('Perte du modèle en fonction du temps')
    plt.xlabel('Époques')
    plt.ylabel('Perte')
    plt.legend()

    plt.tight_layout()
    plt.show()