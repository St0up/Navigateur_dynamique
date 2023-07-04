"""
Programme mettant en forme les calculs produit par le programme
"""

import matplotlib.pyplot as plt

def affichage_resultat(nb_cars, attente, flotte, qui):
    """
    ENTREE : nb_cars : le nombre de voitures
             attente : le temps d'attente entre chaque lancé de voitures
             flotte : informations sur les voitures
             qui : nom de l'algo étudié
    """
    print("\n")
    print("L'algorithme : ", qui)
    print("\n")
    print("nombre de voitures : ", nb_cars)
    print("temps d'attente : ", attente)
    print("durée total: ", flotte.temps)
    print(flotte.trajets)
    donnee = flotte.analyse()
    print("Le trajet le plus long : ", donnee[0])
    print("Le trajet le plus court : ", donnee[1])
    print("La médiane est : ", donnee[2])
    print("La moyenne est : ", donnee[3])
    print("L'écart-type est : ", donnee[4])
    print("\n")
    
def comparaison(flotte1, flotte2, flotte3):
    """
    ENTREE : flotte1 : la flotte lié au Dijkstra naif
             flotte2 : la flotte lié au Dijkstra initial
             flotte3 : la flotte lié au Dijkstra dynamique
    """
    distrib1 = flotte1.temps/flotte1.temps                                   
    distrib_initial = flotte2.temps/flotte1.temps
    distrib_dynamique = flotte3.temps/flotte1.temps
    print("Prix de distribution de naif : ", 1)    
    print("Prix de distribution de initial : ", distrib_initial)
    print("Prix de distribution de dynamique : ", distrib_dynamique)
    if distrib_dynamique < distrib_initial:
        print("L'algorithme dynamique est meilleur que l'initial")
    else:
        print("L'algorithme initial est meilleur que le dynamique")
    print("\n")
    
def graphique(flotte1,flotte2,flotte3):
    plt.plot(flotte1.temps_graphe[1],flotte1.temps_graphe[0], label='naif')
    plt.plot(flotte1.temps_graphe[1],flotte2.temps_graphe[0], label='initial')
    plt.plot(flotte1.temps_graphe[1],flotte3.temps_graphe[0], label='dynamique')
    plt.xlabel('nb voitures')
    plt.ylabel('temps graphe')
    plt.legend()
    plt.show()