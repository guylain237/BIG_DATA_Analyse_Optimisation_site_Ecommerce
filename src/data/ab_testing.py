
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

class ab_test():
    def __init__(self):
        self.processed_path = os.getenv('PROCESSED_PATH')

    def repartition(self):
        item_properties = pd.read_csv(f"{self.processed_path}/item_properties_combined_processed.csv")
        item_properties_shuffle = item_properties.sample(frac=1, random_state=42).reset_index(drop=True)
        split_index = len(item_properties_shuffle) // 2

        groupeA = item_properties_shuffle.iloc[:split_index]
        groupeB = item_properties_shuffle.iloc[split_index:]

        groupeA.to_csv('data/ab_test/groupeA.csv', index=False)
        groupeB.to_csv('data/ab_test/groupeB.csv', index=False)
        print('repartition made succsesfully can now be used for A/B testing')