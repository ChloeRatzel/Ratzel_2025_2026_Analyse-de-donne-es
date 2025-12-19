#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Étape 4 : ouverture du fichier CSV avec "with" ---
chemin_csv = "./data/resultats-elections-presidentielles-2022-1er-tour.csv"

with open(chemin_csv, "r", encoding="utf-8") as f:
    contenu = pd.read_csv(f)

print("✅ Fichier chargé avec 'with' et read_csv()")
print(contenu.head())

# 👇 AJOUTÉ ICI : afficher toutes les colonnes du fichier pour vérifier leur nom exact
print("\n📌 Liste des colonnes du fichier :")
print(contenu.columns.tolist())

# --- Étape 5 : sélectionner les colonnes quantitatives ---
colonnes_quanti = contenu.select_dtypes(include=["number"])
print("\n📊 Colonnes quantitatives :")
print(colonnes_quanti.head())

# --- Étape 6 : calcul des statistiques demandées ---
moyennes = colonnes_quanti.mean().round(2).tolist()
medianes = colonnes_quanti.median().round(2).tolist()
modes = colonnes_quanti.mode().iloc[0].round(2).tolist()
ecarts_types = colonnes_quanti.std().round(2).tolist()
ecarts_absolus = (np.abs(colonnes_quanti - colonnes_quanti.mean())).mean().round(2).tolist()
etendues = (colonnes_quanti.max() - colonnes_quanti.min()).round(2).tolist()

print("\n📈 --- STATISTIQUES DES COLONNES QUANTITATIVES ---")
print("\n⭐ Moyennes :", moyennes)
print("\n⭐ Médianes :", medianes)
print("\n⭐ Modes :", modes)
print("\n⭐ Écarts-types :", ecarts_types)
print("\n⭐ Écarts absolus moyens :", ecarts_absolus)
print("\n⭐ Étendues :", etendues)

# --- Étape 8 : distance interquartile et interdécile ---
diq = (colonnes_quanti.quantile(0.75) - colonnes_quanti.quantile(0.25)).round(2)
did = (colonnes_quanti.quantile(0.9) - colonnes_quanti.quantile(0.1)).round(2)

print("\n⭐ Distance interquartile (Q3 - Q1) :", diq.tolist())
print("\n⭐ Distance interdécile (D9 - D1) :", did.tolist())

# --- Étape 9 : boîtes à moustache ---
if not os.path.exists("img"):
    os.makedirs("img")

for col in colonnes_quanti.columns:
    plt.figure(figsize=(6,4))
    plt.boxplot(colonnes_quanti[col])
    plt.title(f"Boîte à moustache de {col}")
    plt.ylabel(col)
    plt.savefig(f"img/boxplot_{col}.png")
    plt.close()

print("✅ Boîtes à moustache créées et sauvegardées dans le dossier 'img'.")

# --- Étape 10 : catégorisation des îles selon leur surface ---
import os
import pandas as pd
import matplotlib.pyplot as plt

# 🔹 Définir le chemin vers le CSV des îles
chemin_csv_iles = "./data/island-index.csv"

# 🔹 Charger le CSV
contenu = pd.read_csv(chemin_csv_iles, encoding="utf-8")

# 🔹 Vérifier les colonnes disponibles
print("📌 Colonnes disponibles :", contenu.columns.tolist())

# Assurer que la colonne Surface est numérique
contenu["Surface (km²)"] = pd.to_numeric(contenu["Surface (km²)"], errors="coerce")

# Définir les intervalles et labels
bins = [0, 10, 25, 50, 100, 2500, 5000, 10000, float("inf")]
labels = [
    "]0,10]",
    "]10,25]",
    "]25,50]",
    "]50,100]",
    "]100,2500]",
    "]2500,5000]",
    "]5000,10000]",
    "≥10000"
]
# Catégoriser les surfaces
contenu["Categorie_surface"] = pd.cut(
    contenu["Surface (km²)"],
    bins=bins,
    labels=labels,
    right=True
)
# Compter le nombre d'îles par catégorie
compte = contenu["Categorie_surface"].value_counts().sort_index()
print(compte)
