import drawSvg as draw

def lines(n, A, B, C):
    for i in range(1, 1+n):
        d.append(draw.Lines((i*A[0]+(n-i)*C[0])/n,
                            (i*A[1]+(n-i)*C[1])/n,
                            (i*B[0]+(n-i)*C[0])/n,
                            (i*B[1]+(n-i)*C[1])/n,
                            stroke='black'))

l = 20
d = draw.Drawing(2*l, 2*l, origin='center')

A = (-l, -75)
B = (+l, -75)
C = (0 , -75 + l*3**0.5)
n = 1
lines(n, A, B, C)
lines(n, B, C, A)
lines(n, C, A, B)

d.saveSvg("triangles_1.svg")
