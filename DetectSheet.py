import cv2
import numpy as np
import os
import time

def detect_contours(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        if len(approx) == 4:
            cv2.drawContours(frame, [approx], -1, (0, 255, 0), 4)
            break
    return frame

# Utiliser la caméra ou lire depuis un fichier
cam = False  # Changez à False pour lire depuis un fichier

save_folder = "images_sauvegardees"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

if cam:
    cap = cv2.VideoCapture(0)
else:
    save_folder = "images_sauvegardees/renders/"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    path = './externe/renders/'
    frames = os.listdir(path)

if cam:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Impossible de capturer l'image de la caméra. Vérifiez la connexion.")
            break
        frame = detect_contours(frame)
        cv2.imshow("Feuille Detectee", frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            filename = os.path.join(save_folder, f"feuille_{int(time.time())}.png")
            cv2.imwrite(filename, frame)
            print(f"Image enregistrée sous : {filename}")
        if cv2.waitKey(1) & 0xFF == ord('q') or not cam:
            break
else:
    for frame_name in frames:
        frame_path = os.path.join(path, frame_name)  # Construit le chemin complet de l'image
        frame = cv2.imread(frame_path)  # Charge l'image
        if frame is None:
            print(f"Impossible de charger l'image {frame_name}.")
            continue
        frame_with_contours = detect_contours(frame)  # Applique la détection de contours
        filename = os.path.join(save_folder, f"feuille_{frame_name}")
        cv2.imwrite(filename, frame_with_contours)  # Sauvegarde l'image avec contours
        print(f"Image enregistrée sous : {filename}")

if cam:
    cap.release()
cv2.destroyAllWindows()