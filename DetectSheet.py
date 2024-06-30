import cv2
import numpy as np
import os
import time  # Ajout de l'importation du module time

# Capture de l'image à partir de la première caméra connectée
cap = cv2.VideoCapture(0)

# Dossier pour enregistrer les images
save_folder = "images_sauvegardees"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

while True:
    # Lecture de l'image de la caméra
    ret, frame = cap.read()
    if not ret:
        print("Impossible de capturer l'image de la caméra. Vérifiez la connexion.")
        break

    # Conversion en niveaux de gris et floutage
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Détection de contours
    edged = cv2.Canny(blurred, 30, 150)

    # Trouver les contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrer et dessiner les contours
    for contour in contours:
        # Calculer le périmètre du contour
        peri = cv2.arcLength(contour, True)
        # Approximation du contour
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # Si le contour a 4 points, on suppose que c'est une feuille de papier
        if len(approx) == 4:
            cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
            break

    # Afficher l'image avec le contour en rouge
    cv2.imshow("Feuille Detectee", frame)

    # Vérifier si la touche 'espace' est appuyée pour enregistrer l'image
    if cv2.waitKey(1) & 0xFF == ord(' '):
        # Générer un nom de fichier basé sur le timestamp actuel
        filename = os.path.join(save_folder, f"feuille_{int(time.time())}.png")
        cv2.imwrite(filename, frame)
        print(f"Image enregistrée sous : {filename}")

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer toutes les fenêtres
cap.release()
cv2.destroyAllWindows()