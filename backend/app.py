from flask import Flask, request
from function import *
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/reconize', methods=['GET', 'POST'])
def reconize():
    if request.method == 'POST':
        data = request.json
        return f"Received POST data: {data}", 200
    image_path = './data/1_.png'
    img, digits_rois = detect_digits(image_path)
    img = square(img, digits_rois)
    model_CNN = load_model('./models/DetectionReconize_CNN.h5')  # Utiliser load_model pour le modèle CNN
    digits_Cnn = recognize_digits_cnn(img, digits_rois, model_CNN)

    print(digits_Cnn)

    digits_Cnn_output = ''.join(map(str, digits_Cnn))
    return digits_Cnn_output, 200

if __name__ == '__main__':
    app.run(debug=True)
