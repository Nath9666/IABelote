from flask import Flask, request, jsonify
from flask_cors import CORS
from function import *
import json
import shutil
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Ajoutez cette ligne pour permettre les requêtes CORS

UPLOAD_FOLDER_FRONT = './front/public/data'
UPLOAD_FOLDER = './data'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_to_json(data, date_debut, filename_prefix='tournoi_data'):
    # Formater la date de début pour l'utiliser dans le nom du fichier
    date_str = datetime.strptime(date_debut, '%Y-%m-%dT%H:%M').strftime('%Y%m%d')
    filename = f"./data/tournois/{filename_prefix}_{date_str}.json"
    
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

@app.route('/')
def home():
    return jsonify("Hello, Flask!")

#TODO: faire une route pour avoir les infos du tournoi
#TODO: faire une route, avoir la partie actuelle

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

@app.route('/saveTournoi', methods=['POST'])
def save_tournoi():
    data = request.get_json()
    list_participant = data.get('Listparticipant', [])
    dateDebut = data.get('dateDebut', '')
    dateFin = data.get('dateFin', '')

    for participant in list_participant:
        participant['score'] = 0

    # Logique pour traiter les participants du tournoi
    print('Participants reçus:', list_participant)
    print('Date de début:', dateDebut)
    print('Date de fin:', dateFin)

    # Enregistrer les données dans un fichier JSON
    save_to_json(data, dateDebut)

    # Simuler une réponse
    response = {
        'message': 'Tournoi sauvegardé avec succès',
        'participants': list_participant,
        'dateDebut': dateDebut,
        'dateFin': dateFin
    }

    return jsonify(response), 200

@app.route('/templateValue', methods=['GET'])
def template_value():
    # Simuler une réponse
    general_path = './externe/contours/points/'
    output = [
        {
            "texte": 163,
            "position_image": (122, 178, 29, 85),
            "image": "_122_178_29_85.png",
            "general_probabilities" : 0.44,
            "chiffres": [
                {
                    "x": 122,
                    "y": 180,
                    "w": 9,
                    "h": 7,
                    "max_probabilities": (1, 0.8654794),
                    "probabilities": [0.7, 0.8654794, 0.5, 0.00225548, 0.00354571, 0.00219552, 0.02073413, 0.00446359, 0.03090764, 0.00912645]
                },
                {
                    "x": 131,
                    "y": 180,
                    "w": 9,
                    "h": 7,
                    "max_probabilities": (6, 0.7654794),
                    "probabilities": [0.6, 0.4, 0.00215548, 0.00344571, 0.00209552, 0.02063413, 0.7654794, 0.00436359, 0.03080764, 0.00902645]
                },
                {
                    "x": 140,
                    "y": 181,
                    "w": 9,
                    "h": 7,
                    "max_probabilities": (3, 0.6654794),
                    "probabilities": [0.5, 0.3, 0.00205548, 0.6654794, 0.00334571, 0.00199552, 0.02053413, 0.00426359, 0.03070764, 0.00892645]
                }
            ],
        }
    ]

    response = {
        'general_path': general_path,
        'data': output
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)