# Utiliser une version plus récente de Python
FROM python:3.9-slim

# Définir le dossier de travail
WORKDIR /app

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances Python essentielles
RUN pip install --no-cache-dir pandas numpy matplotlib

# Copier tout le dossier src dans le container
COPY src/ /app/

# Vérifier que le fichier est bien copié (temporaire)
RUN ls -R /app

# Exécuter le script principal
CMD ["python", "main.py"]

