def gen_rangées(n):
  """itérateur qui renvoie les rangées d'un mur de largeur n
  Modélisation binaire des rangées."""
  if n < 0:
    # on ne peut rien construire
    return
  if n == 0:
    # on peut construire un mur vide, oui.
    yield 0
    return
  for rangée in gen_rangées(n - 2):
    yield (rangée << 2) | 0b10
  for rangée in gen_rangées(n - 3):
    yield (rangée << 3) | 0b100

n = 9
sommets = list(gen_rangées(n))
arêtes_brutes = dict()
for r1 in sommets:
  arêtes_brutes[r1] = [r2 for r2 in sommets if r1 & r2 == 1 << (n-1)]

numéro = dict(zip(sommets, range(len(sommets))))
arêtes = dict()
for r1 in sommets:
  arêtes[numéro[r1]] = [numéro[r2] for r2 in arêtes_brutes[r1]]

for clé, valeur in arêtes.items():
  print(f"{clé} reliée à {valeur}")
