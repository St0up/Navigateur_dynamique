""" 
Programme où est définit le graphe étudié
"""
from table import*
from arete import*
from graphe import*
from trajet import*
from presentation import*
from flotte import*
from outils import*

# Saisie des données d'entrée

s = [0,1,2,3]                                                            # liste des sommets  
a = [(0,1,1500,13.9),(0,2,2000,13.9),(1,3,2000,13.9),(2,3,1500,13.9)]    # liste des arêtes avec leur longueur et leur vitesse limite

depart = 0           # sommet de départ
arrivee = 3          # sommet d'arrivée
nb_voitures = 1000   # nombre de voitures introduites sur le graphe
attente = 0.1        # délai d'attente entre chaque voiture

# Création des objets graphe, table état et flotte

table_etat = TableEtat(convert_arete(a))    # initialisation de la table état
graphe = Graphe(s,a)                        # initialisation du graphe
flotte = Flotte()                           # initialisation de la flotte

# Execution du programme

boucle_principale(table_etat, graphe, depart, arrivee, nb_voitures, attente, flotte)    # execution de la simulation
table_etat.show()
affichage_resultat(table_etat, nb_voitures, attente, flotte)                            # transmission des données acquises