import pandas as pd
import kaggle
import subprocess
import zipfile
import os
from dotenv import load_dotenv

load_dotenv()

class Dataset:
    def __init__(self, datasets=None):
        """
        Initialise la classe Dataset avec les paramètres de téléchargement et de chemin.
        """
        self.datasets = datasets or {
            "category_tree": "category_tree.csv",
            "events": "events.csv",
            "item_properties_part1": "item_properties_part1.csv",
            "item_properties_part2": "item_properties_part2.csv",
        }

        self.dataset_name = os.getenv('DATASET_NAME')
        self.dataset_path = os.path.normpath(os.getenv('DATASET_PATH'))  # Normaliser le chemin

        # Créer le dossier s'il n'existe pas
        os.makedirs(self.dataset_path, exist_ok=True)

    def data_already_downloaded(self):
        """
        Vérifie si tous les fichiers du dataset sont déjà présents.
        """
        return all(os.path.exists(os.path.join(self.dataset_path, file)) for file in self.datasets.values())

    def data_downloads(self):
        """
        Télécharge et extrait un dataset Kaggle si ce n'est pas déjà fait.
        """
        if self.data_already_downloaded():
            print("✅ Les fichiers du dataset ecommerce existent déjà, téléchargement et extraction ignoré.")
            return

        zip_file = self.dataset_name.split("/")[-1] + ".zip"

        # Télécharger le dataset Kaggle
        subprocess.run(["kaggle", "datasets", "download", "-d", self.dataset_name, "-p", self.dataset_path], check=True)

        # Construire le chemin complet du fichier ZIP téléchargé
        zip_path = os.path.join(self.dataset_path, zip_file)

        # Extraire le fichier zip
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(self.dataset_path)

        # Supprimer le fichier ZIP après extraction
        os.remove(zip_path)

        print(f"✅ Dataset {self.dataset_name} téléchargé et extrait dans : {self.dataset_path}\n")

    def data_items(self):
        """
        Charge les fichiers CSV dans des Datasets .
        """
        try:
            # Charger les fichiers CSV dans des Datasets avec Pandas
            return {
                "category_tree": pd.read_csv(os.path.join(self.dataset_path, "category_tree.csv")),
                "events": pd.read_csv(os.path.join(self.dataset_path, "events.csv")),
                "item_properties_part1": pd.read_csv(os.path.join(self.dataset_path, "item_properties_part1.csv")),
                "item_properties_part2": pd.read_csv(os.path.join(self.dataset_path, "item_properties_part2.csv")),
            }
        except FileNotFoundError as e:
            print(f"Erreur : Fichier non trouvé - {e}")
        except pd.errors.EmptyDataError as e:
            print(f"Erreur : Fichier vide - {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")