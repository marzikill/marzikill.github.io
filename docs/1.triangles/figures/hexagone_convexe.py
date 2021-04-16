import drawSvg as draw

def lines(n, A, B, C):
    for i in range(2*(n+1)//6, 4*(1+n)//6+1):
        d.append(draw.Lines((i*A[0]+(n-i)*C[0])/n,
                            (i*A[1]+(n-i)*C[1])/n,
                            (i*B[0]+(n-i)*C[0])/n,
                            (i*B[1]+(n-i)*C[1])/n,
                            stroke='black'))

l = 350
n = 5

h = l/3**0.5
d = draw.Drawing(3*l//2, 5*l//4 + 100, origin='center')
n *= 3
A = (-l, -h)
B = (+l, -h)
C = (0 , -h + l*3**0.5)

lines(n, A, B, C)
lines(n, B, C, A)
lines(n, C, A, B)

A = (+l, -h + 2*l/3**0.5)
B = (-l, -h + 2*l/3**0.5)
C = (0 , -h - 1*l/3**0.5)

lines(n, A, B, C)
lines(n, B, C, A)
lines(n, C, A, B)
d.append(draw.Text('Exemple avec n = 5', 12, -50, -250))  # Text with font size 12

d.saveSvg("hexagone_convexe.svg")
