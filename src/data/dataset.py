import pandas as pd
import kaggle 
import subprocess
import zipfile

class Dataset:
    def __init__(self, dataset_name="retailrocket/ecommerce-dataset", dataset_path="../../data"):
        """
        Initialise la classe Dataset avec les paramètres de téléchargement et de chemin.

        Args:
            dataset_name (str): Le nom du dataset Kaggle sous le format "retailrocket/ecommerce-dataset".
            dataset_path (str): Le chemin où extraire les fichiers.
        """
        self.dataset_name = dataset_name
        self.dataset_path = dataset_path

    def data_downloads(self):
        """
        Télécharge et extrait un dataset Kaggle.
        """
        # Télécharger le dataset Kaggle
        zip_file = self.dataset_name.split("/")[-1] + ".zip"
        subprocess.run(["kaggle", "datasets", "download", "-d", self.dataset_name], check=True)

        # Extraire le fichier zip
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(self.dataset_path)

        print(f"✅ Dataset {self.dataset_name} téléchargé et extrait dans : {self.dataset_path}")

    def data_items(self):
        """
        Charge les fichiers CSV dans des DataFrames Pandas.
        """
        # Charger les fichiers CSV dans des DataFrames Pandas
        category_tree = pd.read_csv(f'{self.dataset_path}/category_tree.csv')
        events = pd.read_csv(f'{self.dataset_path}/events.csv')
        item_properties_part1 = pd.read_csv(f'{self.dataset_path}/item_properties_part1.csv')
        item_properties_part2 = pd.read_csv(f'{self.dataset_path}/item_properties_part2.csv')

        return category_tree, events, item_properties_part1, item_properties_part2