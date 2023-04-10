""" 
Programme où est définit le graphe étudié
"""
from table import*
from arete import*
from graphe import*
from trajet1 import*
from trajet_initial import*
from trajet_dynamique import*
from presentation import*
from flotte import*
from outils import*
import time

# Saisie des données d'entrée

#s = [0,1,2,3]                                                        # liste des sommets  
#a = [(0,1,1500,13.9),(0,2,2000,13.9),(1,3,2000,13.9),(2,3,1500,13.9)]    # liste des arêtes avec leur longueur et leur vitesse limite

s = [0,1,2,3,4,5]
a = [(0,1,5000,13.9),(0,2,10000,13.9),(1,2,2000,13.9),(1,3,10000,13.9),(1,4,8000,13.9),(2,3,5000,13.9),(2,4,12000,13.9),(3,4,3000,13.9),(3,5,8000,13.9),(4,5,2000,13.9)]

depart = 0           # sommet de départ
arrivee = 5          # sommet d'arrivée
nb_voitures = 1000   # nombre de voitures introduites sur le graphe
attente = 0.1        # délai d'attente entre chaque voiture


""" Dijkstra Naif """

# Création des objets graphe, table état et flotte pour Dijkstra naif

table_etat_naif = TableEtat(convert_arete(a))    # initialisation de la table état
graphe_naif = Graphe(s,a)                        # initialisation du graphe
flotte1 = Flotte()                               # initialisation de la flotte

# Execution du programme

boucle_principale(table_etat_naif, graphe_naif, depart, arrivee, nb_voitures, attente, flotte1)    # execution de la simulation
#table_etat_naif.show()
affichage_resultat(nb_voitures, attente, flotte1, "naif")                         # transmission des données acquises


""" Dijkstra Initial """

# Création des objets graphe, table état et flotte pour Dijkstra naif

table_etat_initial = TableEtat(convert_arete(a))    # initialisation de la table état
graphe_initial = Graphe(s,a)                        # initialisation du graphe
flotte2 = Flotte()                                  # initialisation de la flotte

# Execution du programme

boucle_initial(table_etat_initial, graphe_initial, depart, arrivee, nb_voitures, attente, flotte2)    # execution de la simulation
affichage_resultat(nb_voitures, attente, flotte2, "initial")                      # transmission des données acquises


""" Dijkstra Dynamique """

# Création des objets graphe, table état et flotte pour Dijkstra Dynamique

table_etat_dynamique = TableEtat(convert_arete(a))    # initialisation de la table état
graphe_dynamique = Graphe(s,a)                        # initialisation du graphe
flotte3 = Flotte()                                    # initialisation de la flotte

# Execution du programme

boucle_dynamique(table_etat_dynamique, graphe_dynamique, depart, arrivee, nb_voitures, attente, flotte3)    # execution de la simulation
#table_etat_dynamique.show()
affichage_resultat(nb_voitures, attente, flotte3, "dynamique")                        # transmission des données acquises

""" Comparaison """

comparaison(flotte1, flotte2, flotte3)