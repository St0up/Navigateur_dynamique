"""
Programme où sont définis quelques outils
"""

def convert_arete(l): 
    """
    ENTREE: l : liste de la forme [(a,b,l1,v1),...]
    SORTIE: rep : liste de la forme [(a,b),...]
    """
    rep = []
    for i in l:
        rep.append(i[:-2])
    return rep