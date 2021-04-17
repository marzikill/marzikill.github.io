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

def sans_fissure(r1, r2):
  """Renvoie un booléen :
  les rangées r1 et r2 sont-elles sans fissure ?"""
  def accumule(r):
    "Renvoie la liste des sommes partielles de la liste r"
    cumul_r = [0]
    for w in r:
      cumul_r.append(cumul_r[-1] + w)
    return cumul_r

  cumul_r_1 = accumule(r1)
  cumul_r_2 = accumule(r2)
  assert cumul_r_1[-1] == cumul_r_2[-1], \
         "les listes r1 et r2 doivent être de même somme"
  cumul_r_1.pop() # on enlève cette somme en commun
  cumul_r_2.pop()
  cumul_r_1.pop(0) # on enlève la première valeur commune : zéro
  cumul_r_2.pop(0)

  for x in cumul_r_1:
    if (x in cumul_r_2):
      return False # il y a une fissure !!!
  return True # pas de fissure !

n = 32 # la largeur du mur

sommets = [tuple(r) for r in gen_rangées(n)]
# les sommets sont des 'tuple',
# un peu comme des listes mais immuables.

arêtes = dict()
# les clés de dictionnaires doivent être immuables !

for r1 in sommets:
  arêtes[r1] = [r2 for r2 in sommets if sans_fissure(r1, r2)]

total = 0
for clé, valeur in arêtes.items():
  total += len(valeur)

print(f"Nombre de rangées : {len(sommets)}")
print(f"Nombre moyen de rangées compatibles : {total / len(sommets)}")
