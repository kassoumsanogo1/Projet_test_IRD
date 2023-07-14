import numpy as np
import xml.etree.ElementTree as ET

# Charger les données à partir du fichier .npy
#data = np.load('fichier.npy')
data = np.load('signals.npy')

# Créer l'élément racine du fichier XML
root = ET.Element('data')


# Parcourir les données et créer des éléments XML correspondants
for row in data:
    instance = ET.SubElement(root, 'matrix')
    for i, value in enumerate(row):
        ET.SubElement(instance, 'point' + str(i)).text = str(value)

# Créer l'arbre XML à partir de l'élément racine
tree = ET.ElementTree(root)

# Enregistrer l'arbre XML dans un nouveau fichier .xml
tree.write('data_file.xml')

#CONSIGNES : 
#Suivez les mèmes consignes que dans version finale pour lancer l'API
#Ce code m'a permi de convertir mon fichier .npy en fichier .xml
#Dans le but de tester mon fichier .xml sur ma version finale 
# Tout d'abord j'ai converti le fichier .npy en .xml 
# puis je l'ai fourni à mon API finale pour  avoir la prédiction.

#Jai ajouté une capture de la prediction que j'ai téléchargé à partir de Postman.
