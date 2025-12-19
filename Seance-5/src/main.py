# coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

# Fonction locale pour ouvrir un fichier CSV
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Début du programme
print("Résultat sur le calcul d'un intervalle de fluctuation")

# Lecture des données depuis le fichier CSV
donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))

# Afficher un aperçu des données
print("\nAperçu des 100 échantillons :")
print(donnees.head())

# Calcul des moyennes pour chaque colonne
moyennes = donnees.mean()

# Arrondi des moyennes à l'entier le plus proche (aucune décimale)
moyennes_arrondies = moyennes.round(0).astype(int)

# Affichage des moyennes arrondies
print("\nMoyennes arrondies des 100 échantillons :")
for colonne, moyenne in moyennes_arrondies.items():
    print(f"{colonne} : {moyenne}")

# Partie théorie (conservée mais non utilisée ici)
print("\nRésultat sur le calcul d'un intervalle de confiance")
print("Théorie de la décision")


# Comparaison avec la population mère

# 1) Calcul des fréquences observées à partir des moyennes arrondies
S = moyennes_arrondies.sum()  # somme des individus moyens
f_pour = round(moyennes_arrondies["Pour"] / S, 2)
f_contre = round(moyennes_arrondies["Contre"] / S, 2)
f_sans = round(moyennes_arrondies["Sans opinion"] / S, 2)

print("\nFréquences observées des échantillons (arrondies à 2 décimales) :")
print(f"Pour : {f_pour}")
print(f"Contre : {f_contre}")
print(f"Sans opinion : {f_sans}")

# 2) Fréquences réelles de la population mère
pop_pour = 852
pop_contre = 911
pop_sans = 422
pop_total = 2185

F_pour = round(pop_pour / pop_total, 2)
F_contre = round(pop_contre / pop_total, 2)
F_sans = round(pop_sans / pop_total, 2)

print("\nFréquences réelles de la population mère (arrondies à 2 décimales) :")
print(f"Pour : {F_pour}")
print(f"Contre : {F_contre}")
print(f"Sans opinion : {F_sans}")

# 3) Calcul de l'intervalle de fluctuation à 95 %
def intervalle_fluctuation(p, n):
    z = 1.96  # valeur critique pour un seuil de 95 %
    se = math.sqrt(p * (1 - p) / n)
    borne_inf = p - z * se
    borne_sup = p + z * se
    return round(borne_inf, 3), round(borne_sup, 3)

# Utilisation de la taille moyenne d'un échantillon
n = S

IF_pour = intervalle_fluctuation(F_pour, n)
IF_contre = intervalle_fluctuation(F_contre, n)
IF_sans = intervalle_fluctuation(F_sans, n)

print("\nIntervalles de fluctuation à 95 % autour des fréquences réelles :")
print(f"Pour : {IF_pour}")
print(f"Contre : {IF_contre}")
print(f"Sans opinion : {IF_sans}")


# Théorie de l’estimation
# Intervalle de confiance pour le premier échantillon

# Extraire la première ligne de données
premier_echantillon = donnees.iloc[0].tolist()

# Calcul de la somme des individus dans cet échantillon
n1 = sum(premier_echantillon)

# Calcul des fréquences observées dans le premier échantillon
p_pour = premier_echantillon[0] / n1
p_contre = premier_echantillon[1] / n1
p_sans = premier_echantillon[2] / n1

print("\nPremier échantillon (effectifs) :", premier_echantillon)
print("Taille du premier échantillon :", n1)
print(f"Fréquences observées dans le premier échantillon : Pour {round(p_pour,2)}, Contre {round(p_contre,2)}, Sans opinion {round(p_sans,2)}")

# Fonction pour calculer l'intervalle de confiance à 95 % d'une proportion
def intervalle_confiance_prop(p, n):
    z = 1.96  # valeur critique pour un niveau de confiance de 95 %
    se = math.sqrt(p * (1 - p) / n)
    lower = p - z * se
    upper = p + z * se
    return round(lower, 3), round(upper, 3)

# Calcul des intervalles de confiance pour chaque fréquence
IC_pour = intervalle_confiance_prop(p_pour, n1)
IC_contre = intervalle_confiance_prop(p_contre, n1)
IC_sans = intervalle_confiance_prop(p_sans, n1)

print("\nIntervalle de confiance à 95 % pour le premier échantillon :")
print(f"Pour : {IC_pour}")
print(f"Contre : {IC_contre}")
print(f"Sans opinion : {IC_sans}")


# Test de normalité avec Shapiro-Wilk


from scipy.stats import shapiro

# Charger les deux fichiers
test1 = pd.read_csv("./data/Loi-normale-Test-1.csv").squeeze().values
test2 = pd.read_csv("./data/Loi-normale-Test-2.csv").squeeze().values

# Exécuter le test de Shapiro-Wilk
stat1, pvalue1 = shapiro(test1)
stat2, pvalue2 = shapiro(test2)

print("\nRésultats du test de normalité Shapiro-Wilk :")
print(f"Test 1 : statistique = {stat1:.4f}, p‑value = {pvalue1:.4f}")
print(f"Test 2 : statistique = {stat2:.4f}, p‑value = {pvalue2:.4f}")

# Interprétation simple des résultats
alpha = 0.05
if pvalue1 > alpha:
    print("→ Test 1 : p‑value > 0.05 → On ne rejette pas H0 (probablement normal)")
else:
    print("→ Test 1 : p‑value ≤ 0.05 → On rejette H0 (pas normal)")

if pvalue2 > alpha:
    print("→ Test 2 : p‑value > 0.05 → On ne rejette pas H0 (probablement normal)")
else:
    print("→ Test 2 : p‑value ≤ 0.05 → On rejette H0 (pas normal)")
