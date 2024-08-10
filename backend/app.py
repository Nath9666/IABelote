from flask import Flask, request, jsonify
from flask_cors import CORS
from function import *
import json
import shutil
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Ajoutez cette ligne pour permettre les requêtes CORS

UPLOAD_FOLDER_FRONT = './front/public/data'
UPLOAD_FOLDER = './data' 
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return jsonify("Hello, Flask!")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file_path_react = os.path.join(UPLOAD_FOLDER_FRONT, file.filename)
    file.save(file_path)
    file.save(file_path_react)
    return jsonify({"message": "Image uploaded successfully", "file_path": file_path}), 200


@app.route('/reconize', methods=['POST'])
def reconize():
    data = request.json
    image_path = data.get('image_path', './data/1_.png')  # Utilisez le chemin de l'image fourni ou un chemin par défaut
    
    #Copy l'image dans le serveur front
    destination_path = './front/public/data/original.png'

    # Copier l'image
    shutil.copy(image_path, destination_path)

    print(f"Image copiée de {image_path} à {destination_path}")
    
    img, digits_rois = detect_digits(image_path)
    img = square(img, digits_rois)
    model_CNN = load_model('./models/DetectionReconize_CNN.h5')  # Utiliser load_model pour le modèle CNN
    digits, recognize, digits_probabilities = recognize_digits_cnn(img, digits_rois, model_CNN)

# Convertir les types int64 et float64 en types natifs Python
    digits = [int(digit) if isinstance(digit, np.int64) else digit for digit in digits]
    recognize = [list(rec) if isinstance(rec, np.int64) else rec for rec in recognize]
    digits_probabilities = [prob.tolist() if isinstance(prob, np.ndarray) else prob for prob in digits_probabilities]

    print(digits_probabilities)

    response_data = {
        "max_digits": digits,
        "zone_digits": recognize,
        "digits_probabilities": digits_probabilities
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)