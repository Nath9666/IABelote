from flask import Flask, request, jsonify
from flask_cors import CORS
from function import *
import json

app = Flask(__name__)
CORS(app)  # Ajoutez cette ligne pour permettre les requêtes CORS

@app.route('/')
def home():
    return jsonify("Hello, Flask!")

@app.route('/reconize', methods=['POST'])
def reconize():
    data = request.json
    image_path = data.get('image_path', './data/1_.png')  # Utilisez le chemin de l'image fourni ou un chemin par défaut
    img, digits_rois = detect_digits(image_path)
    img = square(img, digits_rois)
    model_CNN = load_model('./models/DetectionReconize_CNN.h5')  # Utiliser load_model pour le modèle CNN
    digits_Cnn = recognize_digits_cnn(img, digits_rois, model_CNN)

    print(digits_Cnn)

    digits_Cnn_output = ''.join(map(str, digits_Cnn))
    return jsonify({"digits": digits_Cnn_output}), 200

if __name__ == '__main__':
    app.run(debug=True)