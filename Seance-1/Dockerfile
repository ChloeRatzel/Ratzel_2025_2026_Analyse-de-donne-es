#Dockerfile
#Par défaut, ce fichier installe la dernière version de Python. Pour changer de version, remplacer le numéro de version et sa mineure, comme 3.6, 3.7, 3.8, 3.9, 3.10, 3.11 ou 3.12, ou encore par latest pour avoir la dernière version. Toutefois, certains paquets ne fonctionnement pas sur une version supérieure à celle retenue.
FROM python:3.6
RUN mkdir /application
WORKDIR "/application"
# Upgrade pip

# Installer GDAL et les outils nécessaires pour Fiona
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /application/

# Installer les paquets Python

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gfortran \
    libatlas-base-dev \
    libfreetype6-dev \
    libpng-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install -r /application/requirements.txt



# Update


# RUN pip install numpy scipy pandas
CMD [ "python", "main.py" ]
