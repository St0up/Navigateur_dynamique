# Navigateur dynamique

-----------------------------

Le but du projet
----------------

Ce projet est celui que j'ai proposé comme oral de TIPE durant ma 3/2 de MPI en classe préparatoire.  
Pour pouvoir comprendre le projet et l'ensemble de ces objectifs, il vous suffit d'aller sur le pdf : rapport.pdf  


Comment faire marcher le programme ?
----------------------

Il suffit juste de lancer le programme main.py.  
Vous pouvez d'ailleurs paramètrer les différentes caractéritstiques de la modélisation dans ce même fichier.
Il y a différentes options :  
* pour pouvoir faire un test sur un graphe unique utiliser main.py  
* pour pouvoir tester sur 50 graphes aléatoires utiliser main_alea.py  
* pour pouvoir créer une courbe utiliser main_graphe.py, attention il est nécessaire de télécharger le module pyplot   
     
Que font les différents fichiers du programme ?
-----------------------

Il y a deux types de fichiers.  
Les fichiers **objet**, ces fichiers m'ont permis de définir les différents objets et les fonctions associées dont j'ai eu besoin.
* arete.py permet de définir la classe arête
* graphe.py définit ce qu'est un graphe, selon son ensemble de sommets et d'arêtes.
* table.py définit la table d'état (si vous voulez plus de détails sur son utilité, il faut lire le document pdf associé.
* flotte.py garde en mémoire les informations sur toutes les voitures qui ont parcouru le graphe.
    
Les fichiers **action** qui permettent de séquencer les différentes actions du programme pour plus de lisibilité.  
Les fichiers finissant par naif, dynamique, initial sont spécifiques aux différents modèles de navigation.  
* creation.py permet de créer des graphes aléatoires ayant pour chaque sommet le même degré et pour un nombre de sommets définit.
* trajet_ .py est le programme principal qui injecte les voitures sur le réseau routier.
* dijkstra_ .py calcule le plus court chemin selon les différentes techniques utilisées.

Nota Bene
---------

Pour toutes questions possibles sur le projet, vous pouvez me contacter à l'adrtesse mail suivante : gregoirestoupy@gmail.com
