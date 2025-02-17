import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv


# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class DataAnalystic:
    def __init__(self):
        self.processed_path = os.getenv('PROCESSED_PATH')
        self.experiments_path = os.getenv('EXPERIMENTS_PATH')
        self.datasets = self.load_processed_data()

    def load_processed_data(self):
        """
        Charge les données traitées depuis le dossier 'processed'.
        """
        datasets = {}
        for file in os.listdir(self.processed_path):
            if file.endswith('_processed.csv'):
                file_path = os.path.join(self.processed_path, file)
                dataset_name = file.replace('_processed.csv', '')
                datasets[dataset_name] = pd.read_csv(file_path)
                print(f"{dataset_name} chargé avec succès.")
        return datasets


    def analyze_category_tree(self):
        print("Analyse du fichier category_tree...")
        category_tree = self.datasets['category_tree']

        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", category_tree.describe())

        print(f"Valeurs manquantes pour la table catégorie : \n{category_tree.isnull().sum()}\n\n")

        # Catégories principales (sans parent)
        root_categories = category_tree[category_tree['parentid'].isnull()]
        print(f"Nombre de catégories principales : {root_categories['categoryid'].count()}")

        # Initialisation du premier niveau avec une liste pour stocker tous les niveaux
        category_levels = [(root_categories, 1)]
        print("Tous les niveaux de catégorie")

        # Génération dynamique des niveaux suivants
        for level in range(2, 9):  # De 2 à 8 inclus
            category_level = category_tree[category_tree['parentid'].isin(category_levels[-1][0]['categoryid'])]
            print(f"Category Level {level}: {category_level['categoryid'].count()}")
            category_levels.append((category_level, level))

        # Ajout de la colonne level_tree et concaténation des résultats
        category_tree_level = pd.concat([df.assign(level_tree=level) for df, level in category_levels], ignore_index=True)

        # Vérification du résultat
        print(category_tree_level.sort_values("categoryid"))

        # Exportation des transformations
        category_tree_level.to_csv(f"{self.experiments_path}/category_tree_experiment.csv", index=False)
        print("📁 Le fichier 'category_tree_experiment.csv' a été créé avec succès !")

    def analyze_events(self):
        print("Analyse du fichier events...")
        events = self.datasets['events']
        item_properties = self.datasets['item_properties_combined']
        
        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", events.describe())
        # filtrer les items id qui sont presents dans events et item_properties
        events = events[events['itemid'].isin(item_properties['itemid'])]
        #  selectionne des valeurs unique d'event
        event_attributes = events.groupby("event").size()
        print(f"size_event : \n \n{event_attributes}")
        
        #  creation d'un fichier csv pour la visualization des données
        event_attributes.to_csv("data/experiments/event_attributes.csv",index=True)
        print("📁 Le fichier 'event_attributess.csv' a été créé avec succès !")
       
       #  selectionne des valeurs unique d'event 
        event_view = events[events["event"]=="view"]
        event_addtocart = events[events["event"]=="addtocart"]
        event_transaction = events[events["event"]=="transaction"]
        print(f"selection_event view: \n\n{event_view}")
        print(f"selection_event addtocart: \n\n{event_addtocart}")
        print(f"selection_event transaction: \n\n{event_transaction}")
        
        #  Analyse des événements pour comprendre le comportement utilisateur et calculer le taux de conversion

        #  Identifier les utilisateurs ayant ajouté un produit au panier
        user_addtocart = event_addtocart["visitorid"].unique()
        print(f"utilisateurs qui ont ajoute un produit au panier: \n\n{user_addtocart}")

        #  Identifier les utilisateurs ayant vue des produits sans ajouté  au panier
        
        user_view_only = event_view[~event_view['visitorid'].isin(user_addtocart)]['visitorid'].unique()
        print(f"Utilisateurs ayant vu des produits sans ajouter au panier : \n\n{user_view_only}")


        #  Calculer le taux de conversion pour les deux groupes
        conv_addtocart = event_transaction[event_transaction["visitorid"].isin(user_addtocart)]["visitorid"].nunique()/len(user_addtocart)

        conv_view_only = event_transaction[event_transaction["visitorid"].isin(user_view_only)]["visitorid"].nunique()/len(user_view_only)
       
        # Affichage des résultats
        print(f"Taux de conversion des utilisateurs ayant ajouté un produit au panier : {conv_addtocart:.2%}")
        print(f"Taux de conversion des utilisateurs ayant seulement vu des produits : {conv_view_only:.2%}")
        
        #  creation d'un fichier csv pour la visualization des données
        data = { conv_addtocart * 100, conv_view_only * 100}
        conversion_usere = pd.DataFrame(data, index=["panier", "vue"])
        conversion_usere.to_csv(f"{self.experiments_path}/conversion_user.csv",index=True)
        print("📁 Le fichier 'conversion_user.csv' a été créé avec succès !")

        #  creation d'un fichier csv pour la visualization des données de events
        events.to_csv(f"{self.experiments_path}/event_experiments.csv",index=True)
        print("📁 Le fichier 'event_experiments.csv' a été créé avec succès !")


    def analyze_item_properties_combined(self):
        print("Analyse du fichier item_properties_combined...")
        
        # Chargement des données
        item_properties = self.datasets['item_properties_combined']

        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", item_properties.describe())

        # Vérification des valeurs manquantes
        print(f"Valeurs manquantes :\n{item_properties.isnull().sum()}")

        # Extraction des données "available"
        items_available = item_properties[item_properties['property'] == 'available'] \
            .drop(columns=["property", "timestamp"]) \
            .rename(columns={"value": "available"})
        print(items_available)

        # Vérification de la répartition des valeurs disponibles
        print(items_available.groupby("available").count())

        # Extraction des catégories
        items_category = item_properties[item_properties['property'] == 'categoryid'].copy()
        items_category["value"] = items_category["value"].astype("int32")  # Conversion en entier
        items_category = items_category.drop(columns=["property", "timestamp"]).rename(columns={"value": "category"})
        print(items_category.sort_values("category"))

        # Extraction et nettoyage des prix
        items_price = item_properties[item_properties["property"] == "790"].copy()
        items_price["value"] = items_price["value"].replace(["n", ".000"], "", regex=True)
        items_price["property"] = "price"  # Remplacement direct
        items_price = items_price.drop(columns=["property", "timestamp"]).rename(columns={"value": "price"})
        print(items_price)

        # Fusion des tables
        items_available_category = pd.merge(items_available, items_category, on="itemid", how="inner")
        items_clean = pd.merge(items_available_category, items_price, on="itemid", how="inner")

        # Suppression des doublons
        items_clean = items_clean.drop_duplicates()
        print(items_clean)

        # Exportation des résultats
        items_clean.to_csv(f"{self.experiments_path}/e_items_properties_clean.csv", index=False)
        item_properties.to_csv(f"{self.experiments_path}/e_item_properties.csv", index=False)
        print("📁 Les fichiers 'e_items_properties_clean.csv' et 'e_item_properties.csv' ont été créés avec succès !")


    def run_all_analyses(self):
        self.analyze_category_tree()
        self.analyze_events()
        self.analyze_item_properties_combined()
      
