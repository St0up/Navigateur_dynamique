"""
Programme ayant pour projet de conserver les trajets des voitures et différentes informations
"""

class Flotte : 
    
    def __init__(self):
        """
        ENTREE: NONE
        
        définie la flotte de voitures
        """
        self.trajets = {}    # Conserve les trajets et le nombre
        self.nombre = 0      # Nombre de voitures sur la route
        self.data = []       # Le temps de trajet de chaque voiture
        
    def crea_traj(self, traj):
        """
        ENTREE: trajet : le trajet d'une nouvelle voiture
        
        convertie le trajet en une forme plus générale
        """
        l = []
        for i in traj:
            l.append(i[1])
        return l
        
    def introduit(self, trajet, t):
        """
        ENTREE: trajet : le trajet d'une nouvelle voiture
        
        Modifie les différentes données de la flotte lors de l'arrivée d'une nouvelle voiture
        """
        # on l'introduit dans le dictionnaire
        self.nombre += 1
        self.data.append(trajet[0]-t)
        traj = self.crea_traj( trajet[1])
        if str(traj) in list((self.trajets).keys()):
            (self.trajets)[str(traj)] = (self.trajets).get(str(traj)) + 1    # Si le trajet a déjà été pris
        else:
            (self.trajets)[str(traj)] = 1                         # Sinon on le définit
        
    
    def analyse(self):
        """
        SORTIE : rep : 0 : maximum, 1 : minimum, 2 : médiane, 3 : moyenne, 4 : écart type

        Donne une analyse des données produits par l'algorithme
        """
        rep = []
        self.data.sort()
        rep.append(max(self.data))
        rep.append(min(self.data))
        rep.append(self.data[self.nombre//2])
        rep.append (sum(self.data)//self.nombre)
        ecart_type = 0
        for i in self.data:
            ecart_type += (i - rep[3])**2
        ecart_type =(ecart_type/self.nombre)**(1/2)
        rep.append(int(ecart_type))
        return rep
        