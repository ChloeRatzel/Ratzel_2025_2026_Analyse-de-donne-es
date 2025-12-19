# Dockerfile corrigé

FROM python:3.6

# 1) Installer les dépendances système pour GDAL / Fiona
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 2) Définir le dossier de travail
RUN mkdir /application
WORKDIR /application

# 3) Copier le fichier requirements
ADD requirements.txt /application/

# 4) Mettre à jour pip
RUN pip install --upgrade pip

# 5) Installer les dépendances Python
RUN pip install -r /application/requirements.txt

# 6) Copier le reste de l'application
ADD . /application

# 7) Commande de démarrage
CMD ["python", "main.py"]

