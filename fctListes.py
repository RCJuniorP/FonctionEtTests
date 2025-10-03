# Pour chaque fonction une personne différente va :
# a. Programmer la fonction
# b. Créer le plan de tests
# c. Programmer les tests

def fonction1(points_de_vie : float, defense : float, attaque : float) -> float:
    """
    1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et les points d'attaques de l'autre et
    qui retourne les points de vie restants après l'attaque.
    :param points_de_vie: Les points de vies joueur attaqué.
    :param defense: Les points de défense du joueur attaqué.
    :param attaque: Les points d'attaque de l'autre joueur.
    :return: Les points de vie restants après l'attaque.
    """
    difference_attaque_def : float = attaque - defense
    if difference_attaque_def <= 0:
        return points_de_vie
    else:
        return points_de_vie - difference_attaque_def

def fonction2(liste_legos: list, couleur: str):
    """
     2. Fonction qui reçoit une liste de legos et une couleur et qui return le pourcentage de blocs de cette couleur
    :param liste_legos: reçoit la liste de légos
    :param couleur: reçoit la couleur de legos
    :return:
    """
    pourcentage = couleur /len(liste_legos) *100

    print(f"{pourcentage:.2f}")


    pass

def moyenne_par_couleur(listede_legos: list):
    """
    3. Fonction qui reçoit une liste de legos et qui retourne il y a combien de blocs de chaque couleur en moyenne
    :param listede_legos: liste de legos
    """
    from collections import Counter
    listede_legos = ["jaune", "rouge", "jaune", "bleu", "rouge", "bleu"] #exemple
    compteur = Counter(listede_legos)
    print(compteur) #nombre de legos par couleur

    #Total de tous les blocs
    total = len(listede_legos) #nombre de legos total

    for couleur in compteur: #pour chaque couleur dans le compteur -> trouve la moyenne
        moyennes = compteur[couleur] / total
        print(f"{couleur} = {moyennes:.2f}")









    pass

# Répartition des tâches :
"""                     a   b   c
Nom : Junior            1   2   3
Nom : Omar              2   3   1
Nom : Jacob             3   1   2
"""