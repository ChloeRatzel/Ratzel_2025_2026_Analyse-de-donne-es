# coding:utf8
import os
import math
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Fonction pour ouvrir les fichiers
# ==============================
def ouvrirUnFichier(nom):
    """Ouvre un CSV et retourne un DataFrame pandas"""
    return pd.read_csv(nom)

# ==============================
# Fonction pour convertir en log
# ==============================
def conversionLog(liste):
    """Convertit les éléments >0 en log10, None sinon"""
    return [math.log10(x) if x > 0 else None for x in liste]

# ==============================
# Fonction pour trier en décroissant
# ==============================
def ordreDecroissant(liste):
    return sorted(liste, reverse=True)

# ==============================
# Chemin vers le fichier CSV (Docker-safe)
# ==============================
base_path = os.path.dirname(__file__)  # dossier où est main.py
file_path = os.path.join(base_path, "data", "island-index.csv")

# ==============================
# Étape 1.0 — Chargement du fichier
# ==============================
print("\n" + "-"*60)
print("Étape 1.0 — Importation du fichier island-index.csv")
print("-"*60)

iles = pd.DataFrame(ouvrirUnFichier(file_path))
print("\nFichier chargé avec succès :")
print(iles.head())

# ==============================
# 2) Isoler la colonne "Surface (km2)" (mise en float)
# ==============================
surface_isles = iles["Surface (km2)"].astype(float).tolist()

# ==============================
# 3) Ajouter les surfaces des continents
# ==============================
surface_isles.extend([
    85545323.0,  # Asie / Afrique / Europe
    37856841.0,  # Amérique
    7768030.0,   # Antarctique
    7605049.0    # Australie
])

# ==============================
# 4) Trier par ordre décroissant
# ==============================
surfaces_triees = ordreDecroissant(surface_isles)

# ==============================
# 5) Visualisation loi rang-taille (axes linéaires)
# ==============================
rangs = list(range(1, len(surfaces_triees) + 1))

plt.figure(figsize=(10, 6))
plt.scatter(rangs, surfaces_triees)
plt.title("Loi rang-taille des surfaces (axes linéaires)")
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.show()

# ==============================
# 6) Visualisation en log-log
# ==============================
log_rangs = conversionLog(rangs)
log_surfaces = conversionLog(surfaces_triees)

plt.figure(figsize=(10, 6))
plt.scatter(log_rangs, log_surfaces)
plt.title("Loi rang-taille des surfaces (axes logarithmiques)")
plt.xlabel("log10(Rang)")
plt.ylabel("log10(Surface (km²))")
plt.show()
