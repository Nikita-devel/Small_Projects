import matplotlib.pyplot as plt

# Données expérimentales
m = [0, 2.4, 6.5, 10.7, 15, 20.3, 23.3, 27.8] # en g
Q = [0, 10500, 21000, 31500, 42000, 56000, 63000, 73500] # en J

# Tracer la courbe
plt.plot(m, Q)

# Ajouter des étiquettes d'axe et un titre
plt.xlabel('Masse (g)')
plt.ylabel('Energie (J)')
plt.title("Courbe d'évolution de l'énergie en fonction de la masse d'eau vaporisée")

# Afficher la courbe
plt.show()
