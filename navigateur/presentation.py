"""
Programme mettant en forme les calculs produit par le programme
"""

def affichage_resultat(table_etat, nb_cars, attente, flotte):
    """
    ENTREE : table_etat: la table état
             nb_cars : le nombre de voitures
             attente : le temps d'attente entre chaque lancé de voitures
             flotte : informations sur les voitures
    """
    print("\n")
    print("nombre de voitures : ", nb_cars)
    print("temps d'attente : ", attente)
    print("durée total: ", table_etat.size)
    print(flotte.trajets)
    donnee = flotte.analyse()
    print("Le trajet le plus long : ", donnee[0])
    print("Le trajet le plus court : ", donnee[1])
    print("La médiane est : ", donnee[2])
    print("La moyenne est : ", donnee[3])
    print("L'écart-type est : ", donnee[4])
    print("\n")