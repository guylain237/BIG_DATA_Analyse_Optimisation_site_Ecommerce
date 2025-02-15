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
        items_properties = self.datasets['item_properties_combined']
        
        events = events[events.itemid.isin(items_properties.itemid.unique())]
        
        event_attributes = events.groupby("event").size()
        print(f"size_event : \n \n{event_attributes}")

        event_attributes.to_csv("../data/event_attributes.csv",index=True)
        print("📁 Le fichier 'event_attributess.csv' a été créé avec succès !")
        
        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", events.describe())


    

    def analyze_item_properties_combined(self):
        print("Analyse du fichier item_properties_combined...")
        df = self.datasets['item_properties_combined']

        # Statistiques descriptives de base
        print("Statistiques descriptives :\n", df.describe())

        


    def run_all_analyses(self):
        self.analyze_category_tree()
        self.analyze_events()
        self.analyze_item_properties_combined()
      
