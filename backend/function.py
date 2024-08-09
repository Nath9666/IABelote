import joblib
import cv2
import pandas as pd
from tensorflow.keras.models import load_model

def detect_digits(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    digits_rois = []
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if w >= 5 and h >= 25:
            roi = gray[y:y + h, x:x + w]
            digits_rois.append((x, y, w, h, roi))
    return img, digits_rois

def square(img, digits_roi):
    for (x, y, w, h, _) in digits_roi:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img

def recognize_digits_cnn(img, digits_rois, model):
    digits = []
    recognize = []
    digits_probabilities = []
    for (x, y, w, h, roi) in digits_rois:
        roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        roi = roi / 255.0  # Normalisation simple
        roi = roi.reshape(1, 28, 28, 1)  # Reshape pour correspondre à l'entrée du modèle CNN (batch_size, height, width, channels)

        digit = model.predict(roi)
        digit_class = digit.argmax()  # Obtenir la prédiction réelle à partir du résultat
        probabilities = digit[0]  # Obtenir les probabilités

        # Afficher les résultats sans encodage
        #?print(f"Digit: {digit_class}, Probabilities: {probabilities}")

        digits.append(digit_class)
        recognize.append([x,y,w,h])
        digits_probabilities.append(probabilities)
        cv2.putText(img, str(digit_class), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        cv2.imwrite('./front/public/data/recognized.png', img)
    # cv2.imshow("Digits Recognized", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return digits, recognize, digits_probabilities