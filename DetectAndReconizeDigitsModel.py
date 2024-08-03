import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
import numpy as np
import joblib
from sklearn.datasets import fetch_openml
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Charger les données MNIST
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
print(X.shape, y.shape)

# Convertir X en un tableau numpy
X_np = X.to_numpy()

# Remodeler la première image à sa taille originale 28x28 et la convertir en entiers 8 bits
image = X_np[0].reshape(28, 28).astype('uint8')

# Utiliser matplotlib pour afficher l'image
plt.imshow(image, cmap='gray')
plt.show()

hauteur, largeur = image.shape

# Afficher les dimensions
print(f"Hauteur: {hauteur}, Largeur: {largeur}")

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un pipeline qui inclut le MinMaxScaler et le modèle SVC avec les hyperparamètres optimisés
optimized_model = make_pipeline(MinMaxScaler(), SVC(C=10, gamma='scale', kernel='rbf', probability=True))

# Entraîner le modèle optimisé
optimized_model.fit(X_train, y_train)

# Évaluer le modèle optimisé sur l'ensemble de test
y_pred_optimized = optimized_model.predict(X_test)
print(classification_report(y_test, y_pred_optimized))

# Enregistrer le modèle optimisé
model_path = './models/DetectionReconize_optimized2.pkl'
if not os.path.exists(os.path.dirname(model_path)):
    os.makedirs(os.path.dirname(model_path))
joblib.dump(optimized_model, model_path)