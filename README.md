# BIG_DATA_Analyse_Optimisation_site_Ecommerce

AB_test_Ecommerce-optimisation_data_analyst-visualisation
🛒 Vue d'ensemble du projet
Ce projet a pour objectif d'analyser le comportement des utilisateurs sur une plateforme e-commerce en utilisant un jeu de données provenant de RetailRocket. L'analyse vise à identifier des tendances, évaluer les performances des produits et optimiser l'engagement des utilisateurs via des scénarios de test A/B.

# 📊 Objectifs
Comprendre le comportement des utilisateurs (navigation, clics, achats).
Identifier les produits et catégories les plus performants.
Analyser les tendances temporelles (heures et jours d’activité maximale).
Simuler et analyser des tests A/B pour des prises de décision éclairées.
📁 Structure du projet
AB_test_Ecommerce-optimisation_data_analyst-visualisation/ ├── data/ # Fichiers des données brutes (ex. retailrocket-dataset.csv) ├── notebooks/ # Notebooks Jupyter pour l'exploration et l'analyse ├── scripts/ # Scripts Python pour le prétraitement et la visualisation des données ├── reports/ # Rapports et résumés des résultats ├── README.md # Description et guide d'utilisation du projet └── .gitignore # Fichiers et dossiers exclus de Git

yaml Copy code

# ⚙ Outils et technologies
Python : Traitement et analyse des données.
Bibliothèques : pandas, numpy, matplotlib, seaborn, scikit-learn.
Jupyter Notebook : Environnement interactif pour l'analyse.
Git : Gestion de version.
VS Code : Éditeur de code et gestion du projet.
🚀 Instructions d'installation
Clonez le repository :
git clone https://github.com/username/AB_test_Ecommerce-optimisation_data_analyst-visualisation.git
cd AB_test_Ecommerce-optimisation_data_analyst-visualisation
Configurez un environnement virtuel Python : bash Copy code python -m venv env source env/bin/activate # Sur Windows : env\Scripts\activate Installez les dépendances : bash Copy code pip install -r requirements.txt Lancez Jupyter Notebook : bash Copy code jupyter notebook Ouvrez et exécutez les notebooks dans le dossier notebooks/. 📈 Source des données Le jeu de données est issu de RetailRocket. Il contient :

# Événements : Interactions des utilisateurs (clics, vues, achats). Produits : Informations sur les articles de la plateforme. Horodatages : Dates et heures des événements.

# Configuration de l'Environnement et Tests

## 1. Création de l'Environnement Virtuel
```sh
python -m venv env
```

## 2. Activation de l'Environnement
```sh
env\Scripts\activate  # Sous Windows
source env/bin/activate  # Sous macOS/Linux
```

## 3. Installation des Dépendances
```sh
python -m pip install -r requirements.txt
```

## 4. Exécution des Tests

### Test des Pipelines
```sh
python -m src.scripts.main
```

### Test A/B
```sh
python -m src.scripts.test_ab
```


