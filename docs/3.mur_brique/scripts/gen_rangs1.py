def gen_rangées(n):
    "itérateur qui envoie les rangées d'un mur de largeur n"
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

for rangée in gen_rangées(9):
  print(rangée)
