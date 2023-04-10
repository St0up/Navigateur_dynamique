"""
Ce programme est le lien entre les différents objets définis
"""

from table import*
from graphe import*
from dijkstra import*

def duree_trajet(trajet, t, graphe):
    """
    ENTREE : trajet : le trajet le plus rapide sur ce graphe
             t : le temps à partir de quand la voiture part
             graphe : le graphe étudié
    SORTIE : le trajet le plus court entre les deux sommets sous la forme :
        trajet = (temps_total, [(t1,a,b),(t2,b,c)...])

    calcule le reel trajet parcouru en terme de temps par la voiture
    """  
    duree = t
    parcours = []
    for i in trajet:
        temps = (graphe.arete)[i].temps(duree)
        parcours.append((temps, i))
        duree += temps
    return duree, parcours
        

def maj_arete(table_etat, graphe):
    """
    ENTREE: table_etat : la table état
            graphe : le graphe étudié
    SORTIE: NONE
    
    Mise à jour des arêtes du graphe
    """
    for i in graphe.ens_aretes():              # on étudie l'ensemble des arêtes
        l = table_etat.transpo_j((table_etat.dic_ind).get(i))    # l, liste du nombre de voitures qu'il y a sur l'arête i
        (graphe.arete)[i].vitesse_t(l)         # Mise à jour de la liste des vitesses sur l'arête i
        
def maj(table_etat, graphe, t, flotte, trajet):
    """
    ENTREE: table_etat : la table état
            graphe : le graphe étudié
            initial : le sommet de départ
            arrivee : le sommet d'arrivé
            t : le temps à partir de quand la voiture part
            fltte : la flotte de voitures
    
    La fonction maj fait le lien entre la table état et le graphe dans son état actuel
    """
    trajet_reel = duree_trajet(trajet, t, graphe)
    table_etat.new_traj_car(trajet_reel, t)                 # Mise à jour de la table état avec le nouveau trajt
    maj_arete(table_etat, graphe)                      # Mise à jour de la liste de vitesse des arrêtes
    flotte.introduit(trajet_reel, t)                        # Mise a jour de la flotte                             

def boucle_principale(table_etat, graphe, initial, arrivee, nb, tau, flotte):
    """
    ENTREE: table_etat : la table état
            graphe : le graphe du réseau étudié
            initial : le sommet de départ
            arrivee : le sommet d'arrivé
            nb : le nombre de voitures qui sont voulues sur le réseau
            tau : le temps d'écart entre le départ de chaque voiture
            flotte : la flotte de voitures
    
    Fonction lançant les nb voitures sur le réseau routier
    """
    nb_cars = 0                                # le nombre de voitures déjà lancé
    while nb_cars < nb:
        t = int(tau*nb_cars)
        trajet = dijkstra( initial, arrivee, graphe, t)                       
        maj(table_etat, graphe, t, flotte, trajet)    #lance une voiture sur la route
        nb_cars += 1
    flotte.temps = table_etat.size