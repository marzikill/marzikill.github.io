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

for rangée in gen_rangées(9):
  print(bin(rangée))
