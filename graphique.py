import numpy as np
import matplotlib.pyplot as plt

data_numpy = np.load('C:/Users/HP/OneDrive/Documents/PROJET IRD/Projet_en_python/signals.npy')

# choisissez entre le nombre de x à considérer dans cette partie
# Nombre de données à afficher 3 ici
# num_data = 3

#Pour afficher tous le graphique en tenant compte de toutes les données dans le fichier numpy
# Nombre de données à afficher (toutes les données dans cet exemple)
num_data = data_numpy.shape[0]


# Taille de la figure (en pouces) pour unr figure plus large
fig_width = 25
fig_height = 8

# Création de la figure avec la taille souhaitée
fig, ax = plt.subplots(figsize=(fig_width, fig_height))

# Tracé de chaque donnée
for i in range(num_data):
    data = data_numpy[i, :, 0]
    x = range(len(data))
    
    plt.plot(x, data, label='Donnée {}'.format(i+1))
    

plt.xlabel('Valeurs')
plt.ylabel('Amplitudes')
plt.title('Graphique avec 3 données ')
#plt.legend()
plt.grid(True)

# Enregistrer les figures au format JPG
filename = f'C:/Users/HP/OneDrive/Documents/PROJET IRD/Projet_en_python/graphique_avec_3_données.jpg'
plt.savefig(filename, format='jpg')

plt.show()



