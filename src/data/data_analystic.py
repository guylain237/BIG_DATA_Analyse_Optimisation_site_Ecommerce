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
        df = self.datasets['category_tree']

        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", df.describe())

       

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
        conversion_usere.to_csv("data/processed/conversion_user.csv",index=True)
        print("📁 Le fichier 'conversion_user.csv' a été créé avec succès !")

    def analyze_item_properties_combined(self):
        print("Analyse du fichier item_properties_combined...")
        df = self.datasets['item_properties_combined']

        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", df.describe())

        


    def run_all_analyses(self):
        self.analyze_category_tree()
        self.analyze_events()
        self.analyze_item_properties_combined()
      
