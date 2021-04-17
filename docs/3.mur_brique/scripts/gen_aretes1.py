def gen_rangées(n):
    "itérateur qui renvoie les rangées d'un mur de largeur n"
    if n < 0:
        # on ne peut rien construire
        return
    if n == 0:
        # on peut construire un mur vide, oui.
        yield []
        return
    for rangée in gen_rangées(n - 2):
        yield rangée + [2]
    for rangée in gen_rangées(n - 3):
        yield rangée + [3]

def sans_fissure(r1, r2):
    """Renvoie un booléen :
    les rangées r1 et r2 sont-elles sans fissure ?"""

    def accumule(r):
        "Renvoie la liste des sommes partielles de la liste r"
        r_cumul = [0]
        for w in r:
            r_cumul.append(r_cumul[-1] + w)
        return r_cumul

    r_cumul_1 = accumule(r1)
    r_cumul_2 = accumule(r2)
    assert r_cumul_1[-1] == r_cumul_2[-1], \
            "les listes r1 et r2 doivent être de même somme"
    r_cumul_1.pop() # on enlève cette somme en commun
    r_cumul_2.pop()
    r_cumul_1.pop(0) # on enlève la première valeur commune : zéro
    r_cumul_2.pop(0)

    for x in r_cumul_1:
        if (x in r_cumul_2):
            return False # il y a une fissure !!!
    return True # pas de fissure !

n = 9 # la largeur du mur

sommets = [tuple(r) for r in gen_rangées(n)]
# les sommets sont des 'tuple',
# un peu comme des listes mais immuables.

arêtes = dict()
# les clés de dictionnaires doivent être immuables !

for r1 in sommets:
    arêtes[r1] = [r2 for r2 in sommets if sans_fissure(r1, r2)]

print(f"Pour un mur de largeur {n} :")
for clé, valeur in arêtes.items():
    print(f"La rangée {clé} \t est reliée aux rangées {valeur}")
