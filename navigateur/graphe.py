"""
Ce fichier définit la classe graphe, de manière conventionelle. G = (S,A)
"""

from arete import*

class Graphe:
    
    def __init__(self, s, a):
        """
        ENTREE: s :  la liste des sommets
                a : la liste des arrêtes [(a,b,distance,vitesse limite)...]

        initialise le graphe
        """
        self.sommet = s    #la liste des sommets dans le graphe.
        self.arete = {}    #Dictionnaire qui associe chaque couple de sommets, à l'objet arrête associé
        for j in a:
            self.arete[(j[0],j[1])] = Arete(j)
        
    def new_sommet(self, s):
        """
        ENTREE: s : int

        introduit un nouveau sommet dans le graphe
        """
        (self.sommet).append(s)
        
    def new_arete(self, j): 
        """
        ENTREE: a : element de la forme (a,b,distance,vitesse limite)

        introduit une nouvelle arête dans le graphe
        """
        self.arete[(j[0],j[1])] = Arete(j)
    
    def ens_aretes(self):
        """
        ENTREE: NONE
        SORTIE: une liste des arêtes du graphe
        """
        return list(self.arete.keys())
    
    def show_arete(self):
        """
        ENTREE: NONE
        SORTIE: le dictionnaire arete
        """
        return self.arete