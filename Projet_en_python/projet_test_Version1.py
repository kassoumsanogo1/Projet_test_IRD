from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
import tensorflow as tf
import numpy as np

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def make_prediction():
    # Récupérer les données JSON envoyées par le client
    data = np.load('signals.npy')
 
    # Exemple simple : renvoyer les données numpy en tant que prédiction
    prediction = model.predict(data)

    # Retourner la réponse au client
    response = {'prediction': prediction.tolist()}
    return jsonify(response)

if __name__ == '__main__':
    app.run()

    #REMARQUE POUR TESTER : 

    #Ceci est la première version de l'API
    #J'ai utilisé Flask pour la génération sous forme d'application.
    #Cette version me permet de tester directement sur Postman avec les données signals.py pour avoir la prédiction,
    # j'ajouterai une capture d'écran pour vous montrez la prédiction que j'ai eu. 

    

