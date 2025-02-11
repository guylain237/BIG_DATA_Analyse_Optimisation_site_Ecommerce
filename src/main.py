from data import data_dowloads
from data import data_items

data_dowloads("retailrocket/ecommerce-dataset")

category_tree, events, item_properties_part1, item_properties_part2 = data_items()



    # Afficher les premières lignes de chaque DataFrame pour inspection
print("Category Tree:")
print(f" Category Tree:\n {category_tree.head()}")

print("")
print(f" \n Events: \n{events.head()}")

print(f"\n Item Properties Part 1: \n{item_properties_part1.head()}")

print(f"\n Item Properties Part 2: \n{item_properties_part2.head()}")


