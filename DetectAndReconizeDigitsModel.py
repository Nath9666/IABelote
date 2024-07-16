import cv2
import numpy as np
import joblib
from sklearn.datasets import fetch_openml
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline
import os

# Charger les données MNIST
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X = MinMaxScaler().fit_transform(X)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un nouveau modèle avec les meilleurs hyperparamètres
optimized_model = make_pipeline(MinMaxScaler(), SVC(C=10, gamma='scale', kernel='rbf'))

# Entraîner le modèle optimisé
optimized_model.fit(X_train, y_train)

# Évaluer le modèle optimisé sur l'ensemble de test
y_pred_optimized = optimized_model.predict(X_test)
print(classification_report(y_test, y_pred_optimized))

# Enregistrer le modèle optimisé
if not os.path.exists('./models'):
    os.makedirs('./models')
joblib.dump(optimized_model, './models/DetectionReconize_optimized.pkl')