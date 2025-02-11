import pandas as pd
import numpy as np
import kaggle 
import subprocess
import zipfile

def data_dowloads(dataset_name, dataset_path="../../data"):
    """
    Télécharge et extrait un dataset Kaggle.

    Args:
        dataset_name (str): Le nom du dataset Kaggle sous le format "owner/dataset-name".
        dataset_path (str): Le chemin où extraire les fichiers.
    """

    # Télécharger le dataset Kaggle
    zip_file = dataset_name.split("/")[-1] + ".zip"
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name], check=True)

    # Extraire le fichier zip
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(dataset_path)

    print(f"✅ Dataset {dataset_name} téléchargé et extrait dans {dataset_path}")


def data_items():
    
    # Charger les fichiers CSV dans des DataFrames Pandas
    category_tree = pd.read_csv('../../data/category_tree.csv')
    events = pd.read_csv('../../data/events.csv')
    item_properties_part1 = pd.read_csv('../../data/item_properties_part1.csv')
    item_properties_part2 = pd.read_csv('../../data/item_properties_part2.csv')

    # Afficher les premières lignes de chaque DataFrame pour inspection
    print("Category Tree:")
    print(category_tree.head())

    print("\n Events:")
    print(events.head())

    print("\n Item Properties Part 1:")
    print(item_properties_part1.head())

    print("\n Item Properties Part 2:")
    print(item_properties_part2.head())


1