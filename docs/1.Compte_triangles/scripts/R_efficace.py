"""
Méthode force brute
"""

def lst_triangle(n):
    """Renvoie la liste des points distincts
       - à coordonnées entières ;
       - inclus dans le triangle de côté n.
    """
    return [(i, j) for i in range(n+1) for j in range(n+1) if i + j <= n]

def est_triangle(A_i, A_j, B_i, B_j, C_i, C_j):
    """Renvoie un booléen,
    - True, si ABC est un triangle sur le réseau ;
    - False, sinon.
    """
    return (A_j == B_j) and (A_i == C_i) and (B_i - A_i == C_j - A_j != 0)

def force_brute(n):
    ans = 0
    points = lst_triangle(n)
    for (A_i, A_j) in points:
        for (B_i, B_j) in points:
            for (C_i, C_j) in points:
                if est_triangle(A_i, A_j, B_i, B_j, C_i, C_j):
                    ans += 1
    return ans

"""
Méthode efficace

Exercice : supprimer l'utilisation de `factorial`
"""

from math import factorial as f

def comb(n, k):
    "Renvoie le nombre de combinaisons de k choix parmi n"
    if 0 <= k <= n:
        return f(n) // f(k) // f(n-k)
    else:
        return 0

def formule1(n):
    "Calcul rapide"
    return (12*comb(n+2, 3) - 2*comb(n+1, 2) - comb(n, 1) - (n&1)) // 8

# Tests 1
for n in range(10):
        assert formule1(n) == force_brute(n), f"Échec avec n = {n}"

"""
Méthode très efficace
"""

def formule2(n):
    "Calcul très efficace !!!"
    rising = n
    ans = -rising - (n&1)

    n += 1
    rising *= n
    ans -= rising
    
    n +=1
    rising *= n
    ans += rising << 1
    
    return ans >> 3

# Tests 2
for n in range(100):
        assert formule1(n) == formule2(n), f"Échec avec n = {n}"

print("Bravo")
