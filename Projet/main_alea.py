""" 
Programme où est définit le graphe étudié
"""
from tools.table import*
from tools.arete import*
from tools.graphe import*
from tools.trajet_naif import*
from tools.trajet_initial import*
from tools.trajet_dynamique import*
from tools.presentation import*
from tools.flotte import*
from tools.outils import*
from tools.creation import creation_graphe

nb_villes = 50
nb_win = 0
info_init = [0,0,0,0,0,0]
info_dyn = [0,0,0,0,0,0]
nb_points = 30
deg_voulu = 3
depart = 0           # sommet de départ
nb_voitures = 3000   # nombre de voitures introduites sur le graphe
attente = 0.1        # délai d'attente entre chaque voiture        

for i in range(nb_villes):
    s,a, p = creation_graphe(nb_points, deg_voulu)
    print(s,a,p)
    arrivee = p          # sommet d'arrivée         
    table_etat_initial = TableEtat(convert_arete(a))    # initialisation de la table état
    graphe_initial = Graphe(s,a)                        # initialisation du graphe
    flotte2 = Flotte()                                  # initialisation de la flotte
    boucle_initial(table_etat_initial, graphe_initial, depart, arrivee, nb_voitures, attente, flotte2)    # execution de la simulation
    temps_init = flotte2.temps                      
    table_etat_dynamique = TableEtat(convert_arete(a))    # initialisation de la table état
    graphe_dynamique = Graphe(s,a)                        # initialisation du graphe
    flotte3 = Flotte()                                    # initialisation de la flotte
    boucle_dynamique(table_etat_dynamique, graphe_dynamique, depart, arrivee, nb_voitures, attente, flotte3)    # execution de la simulation
    temps_dyn = flotte3.temps                      # transmission des données acquises
    print(i)
    info_init[0] += flotte2.temps
    info_init[1] += len(flotte2.trajets)
    donnee_init = flotte2.analyse()
    info_init[2] += donnee_init[0]
    info_init[3] += donnee_init[2]
    info_init[4] += donnee_init[3]
    info_init[5] += donnee_init[4]
    info_dyn[0] += flotte3.temps
    info_dyn[1] += len(flotte3.trajets)
    donnee_dyn = flotte3.analyse()
    info_dyn[2] += donnee_dyn[0]
    info_dyn[3] += donnee_dyn[2]
    info_dyn[4] += donnee_dyn[3]
    info_dyn[5] += donnee_dyn[4]
    print("nombre de villes : ", nb_villes)
    print("\n")
    print("nombre de sommets : ", nb_points)
    print("degree des sommets : ", deg_voulu)
    print("\n")
    print("nombre de voitures : ", nb_voitures)
    print("temps d'attente : ", attente)
    print("\n")
    print("L'algorithme : initial")
    print("\n")
    print("durée total moyen: ", info_init[0]/(i+1))
    print("Le nombre de trajets différents: ", info_init[1]/(i+1))
    print("Le trajet le plus long : ", info_init[2]/(i+1))
    print("La médiane est : ", info_init[3]/(i+1))
    print("La moyenne est : ", info_init[4]/(i+1))
    print("L'écart-type est : ", info_init[5]/(i+1))
    print("\n")
    print("L'algorithme : Dynamique")
    print("\n")
    print("durée total moyen: ", info_dyn[0]/(i+1))
    print("Le nombre de trajets différents: ", info_dyn[1]/(i+1))
    print("Le trajet le plus long : ", info_dyn[2]/(i+1))
    print("La médiane est : ", info_dyn[3]/(i+1))
    print("La moyenne est : ", info_dyn[4]/(i+1))
    print("L'écart-type est : ", info_dyn[5]/(i+1))
    print("\n")
    if temps_dyn <= temps_init :
        nb_win += 1
        print(nb_win)
    
print("nombre de villes : ", nb_villes)
print("\n")
print("nombre de sommets : ", nb_points)
print("degree des sommets : ", deg_voulu)
print("\n")
print("nombre de voitures : ", nb_voitures)
print("temps d'attente : ", attente)
print("\n")
print("L'algorithme : initial")
print("\n")
print("durée total moyen: ", info_init[0]/nb_villes)
print("Le nombre de trajets différents: ", info_init[1]/nb_villes)
print("Le trajet le plus long : ", info_init[2]/nb_villes)
print("La médiane est : ", info_init[3]/nb_villes)
print("La moyenne est : ", info_init[4]/nb_villes)
print("L'écart-type est : ", info_init[5]/nb_villes)
print("\n")
print("L'algorithme : Dynamique")
print("\n")
print("durée total moyen: ", info_dyn[0]/nb_villes)
print("Le nombre de trajets différents: ", info_dyn[1]/nb_villes)
print("Le trajet le plus long : ", info_dyn[2]/nb_villes)
print("La médiane est : ", info_dyn[3]/nb_villes)
print("La moyenne est : ", info_dyn[4]/nb_villes)
print("L'écart-type est : ", info_dyn[5]/nb_villes)
print("\n")