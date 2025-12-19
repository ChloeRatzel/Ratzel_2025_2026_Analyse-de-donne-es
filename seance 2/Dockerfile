#Dockerfile
#Par défaut, ce fichier installe la dernière version de Python. Pour changer de version, remplacer le numéro de version et sa mineure, comme 3.6, 3.7, 3.8, 3.9, 3.10, 3.11 ou 3.12, ou encore par latest pour avoir la dernière version. Toutefois, certains paquets ne fonctionnement pas sur une version supérieure à celle retenue.
FROM python:3.6

# Créer le dossier de travail
RUN mkdir /application
WORKDIR "/application"

# Installer les dépendances système nécessaires pour les packages Python
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gfortran \
    libatlas-base-dev \
    libfreetype6-dev \
    libpng-dev \
    gdal-bin \
    libgdal-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip
RUN pip install --upgrade pip

# Copier le fichier requirements.txt
ADD requirements.txt /application/

# Installer tous les packages Python
RUN pip install -r /application/requirements.txt

# Commande par défaut
CMD ["python", "main.py"]
