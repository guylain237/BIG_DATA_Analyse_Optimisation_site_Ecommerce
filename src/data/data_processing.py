import pandas as pd
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class DataProcessing:
    def __init__(self, datasets):
        self.datasets = datasets
        self.processed_path = os.getenv("PROCESSED_PATH")

        # Créer le dossier s'il n'existe pas
        os.makedirs(self.processed_path, exist_ok=True)

    def is_data_already_processed(self):
        """
        Vérifie si les fichiers nettoyés existent déjà.
        """
        return all(os.path.exists(os.path.join(self.processed_path, f"{name}_processed.csv")) for name in self.datasets)

    def clean_data(self):
        """
        Nettoie les datasets en supprimant les doublons et en convertissant les timestamps.
        """
        if self.is_data_already_processed():
            print("✅ Les fichiers nettoyés existent déjà, traitement ignoré.")
            return

        print("🛠 Initialisation du nettoyage des données...\n")

        for name, df in self.datasets.items():
            df.drop_duplicates(inplace=True)  # Suppression des doublons
            print(f"✅ Tous les doublons du fichier {name} ont été supprimés.\n")

            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Conversion des dates
                print(f"✅ Les dates ont été converties au bon format dans le fichier {name}.\n")

            # Enregistrer le fichier nettoyé
            processed_file_path = os.path.join(self.processed_path, f"{name}_processed.csv")
            df.to_csv(processed_file_path, index=False)
            print(f"📂 Le fichier {name} est enregistré dans : {processed_file_path}.\n")

        # Fusionner item_properties_part1 et item_properties_part2 si disponibles
        if 'item_properties_part1' in self.datasets and 'item_properties_part2' in self.datasets:
            combined_file_path = os.path.join(self.processed_path, "item_properties_combined_processed.csv")

            if os.path.exists(combined_file_path):
                print("✅ Le fichier fusionné item_properties_combined existe déjà, fusion ignorée.\n")
            else:
                item_properties_combined = pd.concat([self.datasets['item_properties_part1'], self.datasets['item_properties_part2']], ignore_index=True)
                item_properties_combined.drop_duplicates(inplace=True)
                print("✅ Les fichiers item_properties_part1 et item_properties_part2 ont été fusionnés et les doublons supprimés.\n")

                # Enregistrer le fichier fusionné
                item_properties_combined.to_csv(combined_file_path, index=False)
                print(f"📂 Le fichier fusionné item_properties_combined est enregistré dans : {combined_file_path}.\n")

        print("🎉 Données nettoyées avec succès !")

    def get_processed_data(self):
        """
        Charge et retourne les datasets nettoyés depuis le dossier 'processed'.
        """
        processed_data = {}
        for name in self.datasets:
            processed_file_path = os.path.join(self.processed_path, f"{name}_processed.csv")
        
            if os.path.exists(processed_file_path):
                processed_data[name] = pd.read_csv(processed_file_path)  # Charger la version nettoyée
            else:
                print(f"⚠️ Attention : Le fichier nettoyé {processed_file_path} n'existe pas. Retour des données brutes.")
                processed_data[name] = self.datasets[name]  # Retourner les données brutes si le fichier n'existe pas
        
        return processed_data