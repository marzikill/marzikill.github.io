from time import time
from sys import getsizeof

a = [1, 1, 2, 3, 9, 16, 35, 65] # valeurs initiales
r = [-1, 0, 1, -1, 5, 0, 1, 1] # relation de récurrence
n = 200_000 # rang du terme à calculer

t0 = time()
for _ in range(8, n + 1):
    a.append(sum(ai * ri for ai, ri in zip(a[-8:], r)))
t1 = time()

print(f"Durée : {round(t1 - t0, 2)} s")
print(f"Taille des données : {round(sum(map(getsizeof, a))/10**9, 2)} Go")

m = 10**9 + 7
print(f"Preuve de calcul : {a[-1] % m}")

