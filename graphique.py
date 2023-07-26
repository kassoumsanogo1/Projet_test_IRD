import numpy as np
import matplotlib.pyplot as plt

# Exemple de données numpy
#data_numpy = np.random.rand(100, 3)  # Génération aléatoire de 100 lignes x 3 colonnes
data_numpy = np.load('C:/Users/HP/OneDrive/Documents/PROJET IRD/Projet_en_python/signals.npy')
# Convertir les données numpy en liste Python
data_list = data_numpy.tolist()

# Nombre de sous-graphiques que vous souhaitez afficher
num_subplots = 3

# Calcul du nombre de lignes et de colonnes pour la disposition des sous-graphiques
rows = num_subplots
cols = 1

# Création des sous-graphiques
fig, axes = plt.subplots(rows, cols, figsize=(8, 6))

# Tracé de chaque sous-ensemble de données
for i in range(num_subplots):
    x = range(len(data_list))
    y = [row[i] for row in data_list]
    
    # Utilisation de chaque axe pour créer un sous-graphique
    if num_subplots > 1:
        ax = axes[i]
    else:
        ax = axes
    
    ax.plot(x, y, label='Colonne {}'.format(i+1))
    ax.set_xlabel('Index')
    ax.set_ylabel('Valeurs')
    ax.set_title('Graphique {}'.format(i+1))
    ax.legend()
    ax.grid(True)

# Ajustement des espacements entre les sous-graphiques
plt.tight_layout()

# Enregistrer les figures au format JPG
for i, ax in enumerate(axes):
    filename = f'C:/Users/HP/OneDrive/Documents/PROJET IRD/Projet_en_python/graphique_{i+1}.jpg'
    ax.get_figure().savefig(filename, format='jpg')

# Affichage de la figure avec les sous-graphiques
plt.show()
