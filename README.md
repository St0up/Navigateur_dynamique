# Navigateur dynamique

-----------------------------

Quel est le problème ?
----------------------

La question du transport est évidemment une question cruciale dans le fonctionnement des villes. Avec une spécificité : les migrations pendulaires. Chaque matin et chaque soir, des flux importants de véhicules circulent entre le domicile des personnes et leur lieu de travail (et inversement), saturant les réseaux routiers.  
Dans les dernières années, les navigateurs GPS (applications sur smartphone de type Waze ou logiciels intégrés dans les véhicules) sont devenus banals, avec deux usages sensiblement différents :  

*	Se faire guider pour trouver un lieu inconnu ;
*	Trouver l’itinéraire le plus rapide dans un réseau routier surchargé.  
      
De nombreux exemples – et souvent l’expérience personnelle – montrent que ce 2ème usage n’est pas toujours très efficace.   

**Problème :** Dans quelles conditions les navigateurs GPS pourraient améliorer la circulation en situation de trafic dense, par exemple pendant les migrations pendulaires ?

---------------------

Comment modéliser le problème ?
--------------------------------

Pour étudier le problème posé, nous modéliserons le contexte de la manière suivante :  

*	Le réseau routier sera représenté par un réseau de flots : une source, un puits, un graphe orienté et pondéré reliant la source au puits.  
* N véhicules seront introduits sur le réseau routier au niveau de la source. Chaque véhicule partira avec un écart de Tau secondes après celui qui le précède (pour une durée totale de N x Tau secondes).  
*	Pour tenir compte de la possible saturation des routes, la pondération des arêtes ne sera pas fixe, mais elle sera fonction du nombre de véhicules présents sur l’arête.  
*	Enfin, on considèrera que les indications du navigateur sont impératives : chaque conducteur respectera scrupuleusement les consignes (si l’on n’est pas convaincu par cette hypothèse, on pourra imaginer que l’on anticipe l’usage de véhicules autonomes !). 

Ainsi, le réseau routier sera modélisé par :  

*	Un graphe G (S,A) selon la notation conventionnelle où S est la liste des sommets et A la liste des arêtes ;
*	Un sommet d’entrée (appartenant à la liste des sommets S) : la source ;
*	Un sommet de sortie (appartenant à S également) : le puits ;

où chaque arête de la liste A est caractérisée par :  

*	Une longueur (exprimée en mètre) ;  
*	Une loi de vitesse v (exprimée en mètre par seconde), fonction du nombre n de véhicules présents sur l’arête, avec :  
    *	v (n) = Vmax si n < n1   
    *	v (n) = Vmin si n > n2  
    *	v (n) décroissant entre Vmax et Vmin si n est compris entre n1 et n2.  
