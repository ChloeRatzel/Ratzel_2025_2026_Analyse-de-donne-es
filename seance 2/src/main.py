# coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Étape 0 : chemin du CSV ---
chemin_csv = "./data/resultats-elections-presidentielles-2022-1er-tour.csv"

# --- Étape 1 : lecture du fichier CSV ---
contenu = pd.read_csv(chemin_csv)

# --- Étape 7 : types de chaque colonne ---
print("\n📊 Types de chaque colonne :")
print(contenu.dtypes)

# --- Étape 8 : noms de toutes les colonnes ---
print("\n📋 Toutes les colonnes :")
for col in contenu.columns:
    print(col)

# --- Étape 9 : afficher la colonne "Inscrits" ---
inscrits = contenu["Inscrits"]
print("\n📈 Nombre des inscrits :")
print(inscrits)

# --- Étape 10 : somme des colonnes numériques ---
somme_colonnes = []
print("\n📊 Somme des colonnes :")
for col in contenu.columns:
    if contenu[col].dtype in ["int64", "float64"]:
        somme = contenu[col].sum()
        somme_colonnes.append(somme)
        print(f"{col} : {somme}")
    else:
        somme_colonnes.append(None)
        print(f"{col} : Non numérique")

# --- Étape 11 : diagrammes en barres pour chaque département ---
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# --- Chemin du CSV ---
chemin_csv = "./data/resultats-elections-presidentielles-2022-1er-tour.csv"
contenu = pd.read_csv(chemin_csv)

# --- Création du dossier pour les images ---
dossier_images = "./images_departements"
os.makedirs(dossier_images, exist_ok=True)

# --- Fonction pour nettoyer les noms de fichiers ---
def nettoyer_nom_fichier(nom):
    # Remplace tout ce qui n'est pas lettre, chiffre ou underscore par _
    nom_sanitized = re.sub(r'[^A-Za-z0-9_]', '_', nom)
    return nom_sanitized

# --- Boucle pour créer les diagrammes ---
for index, row in contenu.iterrows():
    nom_dep = row["Libellé du département"]
    inscrits = row["Inscrits"]
    votants = row["Votants"]

    nom_dep_sanitized = nettoyer_nom_fichier(nom_dep)
    fichier_image = f"{dossier_images}/{nom_dep_sanitized}.png"

    plt.figure(figsize=(6,4))
    plt.bar(["Inscrits", "Votants"], [inscrits, votants], color=["blue", "green"])
    plt.title(f"Élections 2022 - {nom_dep}")
    plt.ylabel("Nombre de personnes")
    plt.tight_layout()
    
    plt.savefig(fichier_image)
    plt.close()

print(f"\n✅ Diagrammes enregistrés dans le dossier '{dossier_images}'")

# --- Étape 12 : diagrammes circulaires pour chaque département ---
# coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# --- Chemin du CSV ---
chemin_csv = "./data/resultats-elections-presidentielles-2022-1er-tour.csv"
contenu = pd.read_csv(chemin_csv)

# --- Création du dossier pour les images ---
dossier_images = "./images_circulaires"
os.makedirs(dossier_images, exist_ok=True)

# --- Fonction pour nettoyer les noms de fichiers ---
def nettoyer_nom_fichier(nom):
    # Remplace tout ce qui n'est pas lettre, chiffre ou underscore par _
    nom_sanitized = re.sub(r'[^A-Za-z0-9_]', '_', nom)
    return nom_sanitized

# --- Boucle pour créer les diagrammes circulaires ---
for index, row in contenu.iterrows():
    nom_dep = row["Libellé du département"]
    
    # Valeurs pour le camembert
    valeurs = [row["Abstentions"], row["Blancs"], row["Nuls"], row["Exprimés"]]
    labels = ["Abstention", "Blancs", "Nuls", "Exprimés"]
    
    # Nom de fichier sécurisé
    nom_dep_sanitized = nettoyer_nom_fichier(nom_dep)
    fichier_image = f"{dossier_images}/{nom_dep_sanitized}.png"
    
    # Création du diagramme circulaire
    plt.figure(figsize=(6,6))
    plt.pie(valeurs, labels=labels, autopct="%1.1f%%", startangle=90, colors=["gray","yellow","red","green"])
    plt.title(f"Élections 2022 - {nom_dep}")
    plt.tight_layout()
    
    # Sauvegarde
    plt.savefig(fichier_image)
    plt.close()

print(f"\n✅ Diagrammes circulaires enregistrés dans le dossier '{dossier_images}'")
# --- Étape 13 : Histogramme de la distribution des inscrits ---

# On récupère les valeurs de la colonne "Inscrits"
inscrits = contenu["Inscrits"]

# Créer un dossier pour stocker le graphique si besoin
os.makedirs("./images_histogrammes", exist_ok=True)

# Créer l'histogramme
plt.figure(figsize=(8, 5))
plt.hist(inscrits, bins=10, color="skyblue", edgecolor="black", density=True)

# Ajouter les titres et labels
plt.title("Histogramme de la distribution des inscrits (par département)")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Densité de fréquence")

# Sauvegarder l'image
plt.tight_layout()
plt.savefig("./images_histogrammes/histogramme_inscrits.png")
plt.close()

print("\n✅ Histogramme enregistré dans './images_histogrammes/histogramme_inscrits.png'")