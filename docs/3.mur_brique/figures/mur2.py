import drawSvg as draw

l = 50
d = draw.Drawing(12*l, 6*l)


def brique(x, y, w):
  """ Dessine une brique horizontale de taille w = 2|3,
  à partir du point (x, y) ; coordonnées entières.
  """
  d.append(draw.Rectangle(10+x*l ,10+y*l , w*l-2, l-2, fill='red' if w<4 else autre_couleur, stroke_width=8, stroke='black'))

# le mur
autre_couleur = 'blue'
y = 0
for largeurs in [[2, 7, 2], [3, 5, 3]]:
  x = 0
  for w in largeurs:
    brique(x, y, w)
    x += w
  y += 1
autre_couleur = 'green'
y+=1
for largeurs in [[2, 6, 3], [3, 6, 2]]:
  x = 0
  for w in largeurs:
    brique(x, y, w)
    x += w
  y += 1

d.saveSvg('mur2.svg')
