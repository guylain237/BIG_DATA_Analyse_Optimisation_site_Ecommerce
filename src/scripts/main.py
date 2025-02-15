import sys
import os

# Ajouter le dossier 'src' au chemin Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importer la classe Dataset
from data import Dataset
from data import DataProcessing
from data import DataAnalystic

def main():
    print ("demarrage du programme...")
    print ("====================================")
    print ("=====================================")
    print ("=====================================")
    print("telechargement des données...")
    
    # Initialiser la classe Dataset
    dataset = Dataset()

    # Télécharger et extraire les données
    dataset.data_downloads()

    # Charger les données
    datasets = dataset.data_items()

    processor = DataProcessing(datasets)
    processor.clean_data()
    processed_data = processor.get_processed_data()

    print("\nDonnées après traitement :")
    print(f"category_tree :\n{processed_data['category_tree'].info()} \n")
    print(f"events :\n{processed_data['events'].head()}\n")
    print(f"item_properties_part1 :\n{processed_data['item_properties_part1'].head()}\n")
    print(f"item_properties_part2 :\n{processed_data['item_properties_part2'].head()}\n")


#   # Initialiser la classe DataAnalystic
    analystic = DataAnalystic()

    # Analyser les données
    analystic.analyze_events()



if __name__ == "__main__":
    main()
