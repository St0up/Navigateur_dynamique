""" 
Programme central, c'est celui qui permet de tout paramétrer
"""
from tools.table import*
from tools.graphe import*
from tools.trajet_naif import*
from tools.trajet_initial import*
from tools.trajet_dynamique import*
from tools.presentation import*
from tools.flotte import*
from tools.outils import*
from tools.creation import*

# Saisie des données d'entrée

#Exemple 1
"""
s = [0,1,2,3]                                                           # liste des sommets  
a = [(0,1,1000,13.9),(0,2,2000,13.9),(1,3,1000,13.9),(2,3,500,13.9)]    # liste des arêtes avec leur longueur et leur vitesse limite
p = 3
"""
# Exemple 2

s = [0,1,2,3,4,5]
a = [(0,1,5000,13.9),(0,2,10000,13.9),(1,2,2000,13.9),(1,3,10000,13.9),(1,4,8000,13.9),(2,3,5000,13.9),(2,4,12000,13.9),(3,4,3000,13.9),(3,5,8000,13.9),(4,5,2000,13.9)]
p = 5

# Exemple aléatoire
"""
nb_points = 9
deg_voulu = 3

s,a,p = creation_graphe(nb_points, deg_voulu)                        # fonction renvoyant un graphe aléatoire et un puits 
print("La liste des sommets : ",s,"\n\nLa liste des arêtes : ",a)    
"""
# paramétrage du navigateur

depart = 0           # sommet source
arrivee = p          # sommet puits
nb_voitures = 1000   # nombre de voitures introduites sur le graphe
attente = 0.1        # délai d'attente entre chaque voiture


""" Dijkstra Naif """

# Création des objets graphe, table état et flotte pour Dijkstra naif

table_etat_naif = TableEtat(convert_arete(a))    # initialisation de la table état
graphe_naif = Graphe(s,a)                        # initialisation du graphe
flotte1 = Flotte()                               # initialisation de la flotte

# Execution du programme

boucle_principale(table_etat_naif, graphe_naif, depart, arrivee, nb_voitures, attente, flotte1)    # execution de la simulation
affichage_resultat(nb_voitures, attente, flotte1, "naif")                                          # transmission des données acquises


""" Dijkstra Initial """

# Création des objets graphe, table état et flotte pour Dijkstra naif

table_etat_initial = TableEtat(convert_arete(a))    # initialisation de la table état
graphe_initial = Graphe(s,a)                        # initialisation du graphe
flotte2 = Flotte()                                  # initialisation de la flotte

# Execution du programme

boucle_initial(table_etat_initial, graphe_initial, depart, arrivee, nb_voitures, attente, flotte2)    # execution de la simulation
affichage_resultat(nb_voitures, attente, flotte2, "initial")                                          # transmission des données acquises


""" Dijkstra Dynamique """

# Création des objets graphe, table état et flotte pour Dijkstra Dynamique

table_etat_dynamique = TableEtat(convert_arete(a))    # initialisation de la table état
graphe_dynamique = Graphe(s,a)                        # initialisation du graphe
flotte3 = Flotte()                                    # initialisation de la flotte

# Execution du programme

boucle_dynamique(table_etat_dynamique, graphe_dynamique, depart, arrivee, nb_voitures, attente, flotte3)    # execution de la simulation
affichage_resultat(nb_voitures, attente, flotte3, "dynamique")                                              # transmission des données acquises

""" Comparaison """

comparaison(flotte1, flotte2, flotte3)    #Comparaison des différentes données