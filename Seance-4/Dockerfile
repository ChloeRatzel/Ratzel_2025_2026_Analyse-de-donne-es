#Dockerfile
#Par défaut, ce fichier installe la dernière version de Python. Pour changer de version, remplacer le numéro de version et sa mineure, comme 3.6, 3.7, 3.8, 3.9, 3.10, 3.11 ou 3.12, ou encore par latest pour avoir la dernière version. Toutefois, certains paquets ne fonctionnement pas sur une version supérieure à celle retenue.
FROM python:3.6

# Installer les dépendances système si nécessaire (exemple : GDAL)
# RUN apt-get update && apt-get install -y gdal-bin libgdal-dev

WORKDIR /application

COPY requirements.txt /application/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# main.py sera exécuté via docker-compose command



