from time import time

from outils import rec_lin_suc

a = [1, 1, 2, 3, 9, 16, 35, 65] # valeurs initiales
r = [-1, 0, 1, -1, 5, 0, 1, 1] # relation de récurrence
n = 200_000 # rang du terme à calculer

t0 = time()
a_n = rec_lin_suc(a, r, n)
t1 = time()

print(f"Durée : {round(t1 - t0, 2)} s")
m = 10**9 + 7
print(f"Preuve de calcul : {a_n % m}")

