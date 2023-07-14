from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import tensorflow as tf
import numpy as np
 
#j'utilise Flask pour lancer mon API
app = Flask(__name__)

# Charger le modèle de réseau de neurones à partir du fichier HDF5
model = tf.keras.models.load_model('model.h5')

# Utilisez xml_data pour extraire les informations nécessaires

def extract_matrices_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    matrices = []

    # Parcourir les éléments du fichier XML pour extraire les matrices de points
    for matrix_elem in root.findall('.//matrix'):
        points = []

        # Parcourir les éléments de chaque matrice pour extraire les points
        for point_elem in matrix_elem.findall('.//point'):
            x = float(point_elem.find('x').text)
            y = float(point_elem.find('y').text)
            points.append([x, y])

        matrices.append(points)

    return matrices

# Fonction pour effectuer les prédictions sur les matrices de points
def make_predictions(matrices):
    # Convertir les matrices de points en un tableau NumPy
    data = np.array(matrices)

    # Effectuer les prédictions en utilisant le modèle chargé
    predictions = model.predict(data)

    return predictions


# Fonction pour traiter le fichier XML et renvoyer les résultats de prédiction
# Définir le chemin d'API pour effectuer les prédictions
#methode POST pour recuperer les données
@app.route('/predict', methods=['POST'])

def process_xml_file():

    #Partie recupération des données
    xml_file = request.data

    #Partie extraction de matrices à partir du XML
    matrices = extract_matrices_from_xml(xml_file)

    #Partie prédiction
    predictions = make_predictions(matrices)

    # Renvoyer les résultats au format souhaité (par exemple, JSON)
    response = {'predictions': predictions.tolist()}

     # Renvoyer les résultats au format JSON
    return jsonify(response)


if __name__ == '__main__':
    app.run()


    #REMARQUE POUR TESTER : 
    
    #Ceci est la version finale de l'API
    #J'ai utilisé Flask pour la génération sous forme d'application.
    #Cette version me permet de tester directement sur Postman avec les données signals.py pour avoir la prédiction,
    # j'ajouterai une capture d'écran pour vous montrez la prédiction que j'ai eu.

    #CONSIGNES : 

    #Installer Flask sur votre ordinateur en suivant :
    #pip install flask

    #Enregistrez votre fichier et exécutez-le à partir du terminal avec la commande :
    #python projet_test_version_finale.py en ayant préalablement télécharger python.
    #Cela démarrera le serveur Flask local. 

   #si cela ne marche pas entrez : pip install flask d'abord avant de lancer l'API

    #vous pourrez accéder à l'application en lançant Postman
    # puis l'adresse URL http://localhost:5000/predict , sur votre terminal
    # N'oubliez pas d'ajouter les données test en XML au niveau du body

    #Jai ajouté une capture de la prediction que j'ai téléchargé à partir de Postman.

    
    
