import sys
import os

# Ajouter le dossier 'src' au chemin Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importer la classe Dataset
from data import Dataset

def main():
    dataset = Dataset()
    
    # Télécharger et extraire les données
    dataset.data_downloads()
    
    # Charger les données
    category_tree, events, item_properties_part1, item_properties_part2 = dataset.data_items()

    # Afficher un aperçu des données
      # Afficher les premières lignes de chaque DataFrame pour inspection
 
    print(f" Category Tree:\n {category_tree.head()}")

  
    print(f" \n Events: \n{events.head()}")

    print(f"\n Item Properties Part 1: \n{item_properties_part1.head()}")

    print(f"\n Item Properties Part 2: \n{item_properties_part2.head()}")

if __name__ == "__main__":
    main()
