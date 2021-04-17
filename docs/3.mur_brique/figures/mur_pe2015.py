import drawSvg as draw

l = 50
d = draw.Drawing(10*l, 4*l)


def brique(x, y, w):
  """ Dessine une brique horizontale de taille w = 2|3,
  à partir du point (x, y) ; coordonnées entières.
  """
  d.append(draw.Rectangle(10+x*l ,10+y*l , w*l-2, l-2, fill='red', stroke_width=8, stroke='black'))

# le mur
y = 0
for largeurs in [[3, 3, 3], [2, 2, 3, 2], [3, 2, 2, 2]]:
  x = 0
  for w in largeurs:
    brique(x, y, w)
    x += w
  y += 1

# et la fissure
d.append(draw.Rectangle(9+7*l ,10+1*l , 1, 2*l-2, stroke_width=1, stroke='yellow'))

d.saveSvg('mur_pe215.svg')

