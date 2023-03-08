import numpy as np

### dico description des arrêtes
dico_gens_T=dict()
dico_gens_T[personne]=[temps,couple noeud avant noeud après, destination, chemin, compteur]


### y est le dico qui recense la proba de prendre un chemin particulier pour OD donné
def genere_y():
    dico_y=dict()
    dico_y['chemin',[O,D]]=['proba']
    return (dico_y)


###fonction qui génère un nouveau dico_s
### s est le dico qui recense la proba de faire une origine/destination
def genere_s(set):
    dico_s=dict()
    s[(O,D)]=['proba']
    return dico_s

### fonction qui prends le dico des arrêtes, et qui le renvoie au temps suivant dictTplusun<-dictT
def temps(s,y,dico_gens_T,set):

###fonction qui un pour un s donné, boucle la fonction temps pour trouver la stationnarité
def bouclage(s,y, dico_gens_T,set):
    return(s,y)

