import drawSvg as draw

n, m = 6, 10
w = 25
l = (m//2)*w
d = draw.Drawing((m+2)*w, (n+2)*w, origin='center')


A = (-l, -75)
B = (-l + m*w, -75)
C = (-l, -75 + n*w)

for i in range(n+1):
    d.append(draw.Lines(A[0], A[1]+i*w,
                        B[0], B[1]+i*w,
                        stroke='black'))

for i in range(m+1):
    d.append(draw.Lines(A[0]+i*w, A[1],
                        C[0]+i*w, C[1],
                        stroke='black'))

d.append(draw.Text('Exemple avec n = 6 et m = 10', 12, -90, -100))  # Text with font size 12


d.saveSvg("rectangles.svg")
