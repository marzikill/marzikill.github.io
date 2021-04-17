# Premier code complet fonctionnel !!!

# Auteur : Franck CHAMBON

def gen_rangées(n):
    """Renvoie un itérateur : les rangées possibles.
    Elles sont stockées dans un entier, en binaire
    100101010 → [3, 2, 2, 2], une rangée de longueur 9
    """
    if n < 0:
        # on ne peut rien construire
        return
    if n == 0:
        # on pourrait 'construire' un mur vide, oui.
        yield 0
        return
    for rangée in gen_rangées(n - 2):
        yield (rangée << 2) | 0b10
    for rangée in gen_rangées(n - 3):
        yield (rangée << 3) | 0b100

def nb_murs_sans_fissure(n, h):
    "Pour un mur de largeur n, et de hauteur h"
  
    if (n < 0) or (h < 0):
        return 0 # construction impossible
    if (n == 0) or (h == 0):
        return 1 # un seul mur ; un mur vide

    sommets = list(gen_rangées(n))
    nb_rangées = len(sommets)
    arêtes_brutes = dict()
    for r1 in sommets:
        arêtes_brutes[r1] = [r2 for r2 in sommets if r1 & r2 == 1 << (n-1)]

    numéro = dict(zip(sommets, range(nb_rangées)))
    arêtes = dict()
    for r1 in sommets:
        arêtes[numéro[r1]] = [numéro[r2] for r2 in arêtes_brutes[r1]]

    vectV = [1] * nb_rangées
    for _ in range(h-1):
        vectMV = [0] * nb_rangées
        for i in range(nb_rangées):
            nb_arêtes_depuis_i = vectV[i]
            for j in arêtes[i]:
                vectMV[j] += nb_arêtes_depuis_i
        vectV = vectMV
  
    return sum(vectV)


n, h = 9, 3
print(f"W({n}, {h}) = {nb_murs_sans_fissure(n, h)}")
