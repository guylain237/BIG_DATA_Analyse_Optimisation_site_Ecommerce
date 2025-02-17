
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os
import scipy.stats as stats
load_dotenv()

class ab_test():
    def __init__(self):
        self.processed_path = os.getenv('PROCESSED_PATH')

    def repartition(self):


        # Simulation des données pour les utilisateurs
        np.random.seed(42)  # Pour garantir la reproductibilité

        # Nombre d'utilisateurs dans chaque groupe
        n_addtocart = 10000  # Groupe qui ajoute des produits au panier
        n_viewonly = 10000   # Groupe qui consulte uniquement

        # Taux de conversion simulé pour chaque groupe
        conversion_rate_addtocart = 0.2796  # 27.96% de conversion
        conversion_rate_viewonly = 0.0009   # 0.09% de conversion

        # Génération des résultats de conversion pour chaque groupe
        addtocart_conversions = np.random.binomial(n_addtocart, conversion_rate_addtocart)
        viewonly_conversions = np.random.binomial(n_viewonly, conversion_rate_viewonly)

        # Calcul des taux de conversion pour chaque groupe
        conversion_rate_addtocart_simulated = addtocart_conversions / n_addtocart
        conversion_rate_viewonly_simulated = viewonly_conversions / n_viewonly

        # Affichage des résultats
        print(f'Taux de conversion pour "Ajout au panier" : {conversion_rate_addtocart_simulated:.4f}')
        print(f'Taux de conversion pour "Consultation uniquement" : {conversion_rate_viewonly_simulated:.4f}')

        # Test A/B : Test de différence de proportions (test Z)
        # H0 : les taux de conversion des deux groupes sont égaux
        # H1 : les taux de conversion des deux groupes sont différents
        # Calcul de la statistique z et de la p-value pour tester la différence de conversion
        p1 = conversion_rate_addtocart_simulated
        p2 = conversion_rate_viewonly_simulated
        n1 = n_addtocart
        n2 = n_viewonly

        # Calcul de la variance combinée
        pooled_p = (addtocart_conversions + viewonly_conversions) / (n1 + n2)
        std_error = np.sqrt(pooled_p * (1 - pooled_p) * (1/n1 + 1/n2))

        # Calcul de la statistique z
        z = (p1 - p2) / std_error

        # Calcul de la p-value pour le test bilatéral
        p_value = 2 * (1 - stats.norm.cdf(abs(z)))

        # Résultats du test
        print(f'Statistique Z : {z:.4f}')
        print(f'P-value : {p_value:.4f}')

        # Interprétation
        if p_value < 0.05:
            print("La différence entre les groupes est statistiquement significative. Il est probable que l'ajout au panier influence le taux de conversion.")
        else:
            print("La différence entre les groupes n'est pas statistiquement significative.")
