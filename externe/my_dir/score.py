import os
import json

name_file = "trial.json"
path = "my_dir\mnist_tuning\\"
# Liste tous les éléments dans le répertoire
all_items = os.listdir(path)

# Filtre pour ne garder que les dossiers
dirs = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
scores = {}

for dir in dirs :
    # Concatène le chemin et le nom du fichier
    full_path = os.path.join(path,dir, name_file)


    # Ouvre le fichier et le lit
    with open(full_path, 'r') as file:
        data = json.load(file)

    # Affiche le contenu du fichier JSON
    if data['status'] == "COMPLETED":
        print(data['trial_id'], data['score'])
        scores[data['trial_id']] = data['score']

# Trier les scores en fonction des valeurs
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))

print(sorted_scores)