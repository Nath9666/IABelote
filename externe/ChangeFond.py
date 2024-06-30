import bpy
import os

# Fonction pour convertir une couleur RGB en hexadécimal
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

# Liste des couleurs à appliquer (en RGB)
colors = []
n = 3  # Pour obtenir un cube de 3x3x3 = 27, mais nous ne prendrons que les 25 premières couleurs

for r in range(n):
    for g in range(n):
        for b in range(n):
            if len(colors) < 25:  # Limite à 25 couleurs
                colors.append((r / (n - 1), g / (n - 1), b / (n - 1)))

print(colors)

# Spécifiez le chemin du dossier où vous souhaitez enregistrer les images
output_folder = bpy.path.abspath("//renders/")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Assurez-vous que le matériau et le nœud existent
material_name = "fond"  # Remplacez par le nom de votre matériau
if material_name in bpy.data.materials:
    mat = bpy.data.materials[material_name]
    if "Principled BSDF" in mat.node_tree.nodes:  # Assurez-vous que le nœud Principled BSDF existe
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        for color in colors:
            # Change la couleur de base
            bsdf.inputs['Base Color'].default_value = color + (1,)  # Ajoutez l'alpha
            # Rendre l'image
            bpy.ops.render.render(write_still=True)
            # Construire le nom de fichier
            hex_color = rgb_to_hex(color)
            file_name = os.path.join(output_folder, f"{hex_color}.png")
            # Sauvegarder l'image
            bpy.data.images['Render Result'].save_render(filepath=file_name)
            print(f"Image sauvegardée: {file_name}")
else:
    print(f"Le matériau '{material_name}' n'existe pas.")