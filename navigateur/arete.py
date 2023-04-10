"""
Ce fichier définit la classe arête.
"""

class Arete:

    def __init__(self,info_arete):
        """
        ENTREE: info_arete : list
                vitesse: int

        définie les informations de l'arête
        """
        self.nom = (info_arete[0], info_arete[1])    # sommet de départ
        self.vitesse_max = info_arete[3]             # vitesse limite de la route (m/s)
        self.longueur = info_arete[2]                # longueur de l'arête
        self.vitesse = []                            # liste de la vitesse sur la route de t = 0 à n (lié à la table état)
    
    def calcul_vitesse(self, nb_car):
        """
        ENTREE: self
                nb_car : le nombre de voitures sur la route
        SORTIE: int

        renvoie La vitesse sur la route selon le nombre de voitures
        """
        if nb_car == 0 : 
            return self.vitesse_max
        if nb_car > 142:
            return 0
        elif self.vitesse_max == 8.3:
            v = (self.longueur/(2.4*nb_car))-(7/2.4)
        elif self.vitesse_max == 13.9:
            v = (self.longueur/(2*nb_car))-(7/2)
        elif self.vitesse_max == 19.4:
            v = (self.longueur/(1.6*nb_car))-(7/1.6)
        elif self.vitesse_max == 22.2:
            v = (self.longueur/(1.5*nb_car))-(7/1.5)
        elif self.vitesse_max == 25.0:
            v = (self.longueur/(1.4*nb_car))-(7/1.4)
        elif self.vitesse_max == 30.5:
            v = (self.longueur/(nb_car))-7
        if v > self.vitesse_max:
            return self.vitesse_max
        return v
    
    def vitesse_t(self, l):
        """
        ENTREE: self
                l : le nombre de voitures sur l'arête
        SORTIE: None

        met a jour la liste des vitesses selon la table état
        """
        self.vitesse = []                                    # réinitialise la fonction vitesse
        for i in l:
            (self.vitesse).append(self.calcul_vitesse(i))    # vitesse apprends la vitesse moyenne sur la route selon le nombre de voiture 
            
    def temps(self, t, tau = 1):
        """
        ENTREE: selfs
            tau : la duree entre deux valeurs
            t : L'indice a partir duquel on calcule le temps
        SORTIE: duree: Le temps de trajet pour traverser l'arrête selon le nombre de véhicules sur l'arête
        
        Cette fonction met à jour la liste vitesse, grâce à la table état
        """
        distance = 0                                 # Condition limite qui calcule le temps parcouru après un certain tau
        duree = 0                                    # Le temps de trajet pour traverser l'arrête selon le nombre de véhicules sur l'arête
        while distance < self.longueur:              # Cette condition nous permet de savoir si la voiture à parcouru l'arête
            if t+duree >= len(self.vitesse):         # Condition pour ne pas dépasser la liste vitesse et donc générer une erreur
                distance += self.vitesse_max
            else:
                distance += self.vitesse[t+duree]    
            duree += tau
        return duree
        
    

#exemple = Arete((1,2, 400), 13.9)                           # exemple d'arête
#print(exemple.calcul_vitesse(15))                           # exemple du calcul de la vitesse sur la route
#exemple.vitesse_t([4,7,12,16,14,17,21,24,25,28,34,26,22]) 
#print(exemple.vitesse)                                      # exemple de ce que renvoie vitesse_t
#print(exemple.temps(1,3))                                   # exemple de ce que renvoie la fonction temps