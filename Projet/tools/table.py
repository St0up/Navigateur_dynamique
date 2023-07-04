"""
programme qui définit la table état.
"""

class TableEtat:
    
    def __init__(self,ens_arete):
        """
        ENTREE: ens_arete : list (liste des arêtes)
        
        crée la table_etat initial sans aucun trajet
        """
        self.table = [[]]              #initialise la table état
        self.dic_ind = dict()          #initialise le dictionnaire donnant l'indice des arêtes
        self.size = 0                  #longueur de la table état initialisé a 0
        n = 0
        for i in ens_arete:
            self.table[0].append(i)    #crée la première ligne de la table état
            self.dic_ind[i] = n 
            n+=1
    
    def add_lignes(self, nb):
        """
        ENTREE: self : list*list
                nb : int
        
        Modifie la table état avec nb-lignes en plus
        """
        self.size = self.size + nb                                          #ajoute nb à la longueur de la table état
        for i in range(nb):
            self.table.append([0 for loop in range(len(self.table[0]))])    #rajoute nb lignes de taille le nombre d'arêtes utilisé
            
    def new_traj_car(self, trajet, t):
        """
        ENTREE: trajet : (int, int*list) donne le temps de trajet et les chemins parcourus avec le temps de parcours
                t : 
        
        modifie la table état en prenant en compte le trajet d'une nouvelle voiture
        """
        if trajet[0]>self.size:
            self.add_lignes(trajet[0]-self.size)                        # Ajoute le nombre nécessaire de lignes à la table état
        ligne = t + 1                                                   # ligne où la table état va être modifié
        for arete in trajet[1]:
            for loop in range (arete[0]):
                self.table[ligne][(self.dic_ind).get(arete[1])] += 1    # Ajoute le véhicule à l'instant t sur l'arête où il sera
                ligne+=1
                
    def transpo_j(self, j):
            """
            ENTREE: j : int    ligne à transposer
            SORTIE: rep : list 
            
            transposition de la colonne j du tableau
            """
            rep = []
            for i in range(1, len(self.table)):
                rep.append(self.table[i][j])
            return rep
        
    def show(self):
        """
        impression de la table état
        """
        for i in range(1,len(self.table)):
            for j in range(len(self.table[0])):
                print(self.table[i][j], end = " ")
            print("\n")