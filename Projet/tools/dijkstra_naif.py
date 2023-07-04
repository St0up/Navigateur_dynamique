"""
Programme donnant la fonction du calcul du plus court chemin
"""

from tools.graphe import*

def minimal(temps_traj, do):
    """
    ENTREE: pere : (int*int)list     liste donnant le temps pour allé du sommet de départ à ce sommet et son père
            do : (int)list    liste vérifiant si le sommet a déjà été étudié ou non
    SORTIE: ind : int
    
    Le sommet ind est le sommet qui est le plus proche du sommmet de départ non étudié
    """
    ind = -1                                       # valeur de retour, renvoie -1 si aucun sommet a été trouvé
    mini = 9999999                                 # durée la plus courte avec le sommet de départ
    for i in range (len(temps_traj)):              # regarde pour tous les sommets
        if temps_traj[i] < mini and do[i] == 0:    # le sommet doit vérifier si sa durée est plus courte que celle de ind et s'il n'a pas été étudié
            mini = temps_traj[i]
            ind = i
    return ind

def adjacent(graphe, ind, do):
    """
    ENTREE: graphe : le graphe étudié
            ind : le sommet étudié
            do : la liste vérifiant si les sommets ont été étudié ou non
    SORTIE: rep : liste des arêtes adjacentes à ind et qui n'ont pas encore été parcourus
    """
    rep = []
    for i in (graphe.arete).keys():          # vérifie toutes les arêtes   
        if i[0] == ind and do[i[1]] == 0:    # le premier sommet doit être ind et le deuxième ne doit pas avoir été étudié
            rep.append(i)                    
    return rep

def constru_rep(ind, pere):
    """
    ENTREE: ind : le sommet que l'on étudie
            pere : la liste des pères, donne le trajet par récursivité
    SORTIE: l : list qui donne le temps de trajets de initial à arrivee de la forme [(t1,a,b),(t2,b,c)...]
    """
    if ind == pere[ind][0]:                        # condition limite : le prochain sommet est lui même, nous sommes arrivées !        
        return []
    l = constru_rep(pere[ind][0], pere)            # liste construit par réccursivité sur le pere de ind
    l.append((pere[ind][0],ind))
    return l
       
def dijkstra(initial, arrivee, graphe, t):
    """
    ENTREE: initial : int, le sommet de départ
            arrivee : int, le sommet d'arrivé
            graphe : le graphe sur lequel on travaille
            t : int, le temps a partir duquel la voiture part
    SORTIE: le trajet le plus court entre les deux sommets sous la forme :
            trajet = (temps_total, [(t1,a,b),(t2,b,c)...])
    """
    n = len(graphe.sommet)                                     # regarde le nombre de sommets dans le graphe
    pere = [[i,9999999] for i in range(n)]                     # définit pere, la liste des sommets, celui avant lui dans le trajet le plus court vers init et le temps de trajet entre les deux sommets
    do = [0 for i in range(n)]                                 # liste qui vérifie qui a déja été parcouru
    temps_traj = [9999999 for i in range(n)]                   # temps_traj[i] = a -> temps entre initial et i est de a
    temps_traj[initial] = 0                                    # conditions initiales
    pere[initial][1] = 0
    for loop in range(n):
        ind = minimal(temps_traj, do)                          # regarde quel est le sommet à étudier
        do[ind] = 1                                            # l'annonce dans la liste do
        if ind == arrivee:                                     # si le sommet ind = arrivee alors on a le chemin le plus court entre initial et arrivee, donc on arêtte le programme
            return constru_rep(ind, pere)
        adjoint = adjacent(graphe, ind, do)                    # regarde les arêtes à étudier
        for i in adjoint:
            duree = int((graphe.arete)[i].longueur/(graphe.arete)[i].vitesse_max)   # duree entre les deux sommets, faire attention à faire la différence entre la fonction temps et la liste
            if temps_traj[ind] + duree < temps_traj[i[1]]:     # on vérifie que le trajet est plus rapide en passant par ind
                temps_traj[i[1]] = temps_traj[ind] + duree
                pere[i[1]][0] = ind                            # modifie le père du sommet étudié
                pere[i[1]][1] = duree                          # on y met la distance entre i et ind