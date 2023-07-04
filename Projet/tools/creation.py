import random

def identite_arete ():
    """
        ENTREE: NONE

        Donne une longueur aléatoire allant de 500m à 10000m à la route
        et donne une valeur de vitesse limite aléatoire
    """
    longueur = 100*random.randint(5,100)    
    v_rand  = random.randint(1,100)
    if v_rand <= 20 :                        
        v_lim = 8.3
    elif v_rand <= 70 : 
        v_lim = 13.9
    elif v_rand <= 85 :
        v_lim = 19.4
    elif v_rand <= 95 :
        v_lim = 22.2
    else:
        v_lim = 25.0
    return (longueur, v_lim)

def alea(nb_points, degree_voul):
    """
        ENTREE: nb_points : le nombre de points du graphe 
                degree_voulu : le degrée maximal de tous les sommets du graphe

        C'est la fonction qui crée le graphe aléatoire
    """
    degree = [0 for i in range(nb_points)]                               #liste vérifiant le degré de tous les sommets du graphe
    mat = [[-1 for i in range (nb_points)] for i in range(nb_points)]    #Le graphe est définit sous la forme d'une matrice d'adjacence
    for i in range(nb_points-degree_voul):
        deg = degree[i]
        tour = 0 
        while deg < degree_voul and tour < 1000:                         #
            som = random.randint(i+1, nb_points-1)                       # Choix du prochain sommet avec lequel il sera ajacent
            tour += 1
            if degree[som] < degree_voul and mat[i][som] == (-1):        # Vérifie que le choix de ce sommet est possible
                deg += 1
                degree[som] += 1
                id = identite_arete ()                                   # Crée une
                mat[i][som] = id
                mat[som][i] = id
        degree[i] = 5
    return mat

def trans_te(mat):
    """
        ENTREE: mat : la matrice d'adjacence du graphe

        fonction tansformant la matrice d'adjacence dans le format compatible avec le modèle de navigation
    """
    s = [i for i in range(len(mat))]
    a = []
    pere = [i for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != -1:
                a.append((i,j,mat[i][j][0],mat[i][j][1]))
    return (s,a)

def bfs(mat, s1):
    """
        ENTREE: mat : la matrice d'adjacence du graphe
                s1 : le sommet source

        fonction va faire un parcours en largeur pour pouvoir trouver tous les sommets connexe avec le sommet source
        puis va prendre un de ces sommets au choix et va le renvoyer : ce sera le puits
    """
    view = [0 for i in range(len(mat))]
    ind = 0
    view[s1] = 1
    pile = [s1]
    while ind<len(pile):
        for i in range(len(mat)):
            if (mat[pile[ind]][i] != -1) and view[i] == 0:
                view[i] = 1
                pile.append(i)
        ind += 1
    pile.remove(s1)
    return random.choice(pile)
                

def creation_graphe(nb_points, deg_voulu):
    """
        ENTREE: nb_points : le nombre de points du graphe 
                degree_voulu : le degrée maximal de tous les sommets du graphe

        C'est la fonction qui renvoie à main.py l'ensemble des informations utiles.
    """
    mat = alea(nb_points, deg_voulu)
    puits = bfs(mat,0)
    s,a = trans_te(mat)
    return s,a,puits

#s,a,puits=creation_graphe(50, 3)
#print(s,a,puits)
#print(len(a))