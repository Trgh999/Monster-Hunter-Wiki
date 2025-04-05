# Utilise une image de base officielle Python 3.10
FROM python:3.10-slim

# Met à jour pip avant d'installer les dépendances
RUN pip install --upgrade pip

# Met à jour les sources APT et installe les dépendances nécessaires
RUN apt-get update -y && apt-get install -y \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans ce répertoire de travail
COPY requirements.txt .

# Installe les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le reste de l'application dans le conteneur
COPY . .

# Exécute ton bot Python (le fichier `bot.py` doit être présent)
CMD ["python3", "main.py"]
