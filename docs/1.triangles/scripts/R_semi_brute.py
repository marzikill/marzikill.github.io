def comb_2(n):
    "Renvoie le coefficient binomial (n, 2)"
    return n * (n-1) // 2

def R_brute(n, m):
    """Renvoie de nombre de rectangles dessinés dans une grille n×m
    Force brute : complexité n²×m²
    """
    cpt = 0
    for A_i in range(n+1):
        for A_j in range(m+1):
            for B_i in range(n+1):
                for B_j in range(m+1):
                    if (A_i < B_i) and (A_j < B_j):
                        cpt += 1
    return cpt

def R_semi_brute(n, m):
    # À compléter
    return ...

def R(n, m):
    """Renvoie de nombre de rectangles dessinés dans une grille n×m
    Formule combinatoire : coût constant (pour n et m de taille raisonnable)
    """
    return comb_2(n+1) * comb_2(m+1)


# tests
for n in range(10):
    for m in range(10):
        assert R(n, m) == R_semi_brute(n, m) == R_brute(n, m)

print("Bravo")

"""
# Exercice

1. Compléter la fonction R_semi_brute(n, m)
2. Appuyer sur [⛭ Exécuter]
3. Bravo ?

Conseil : [👁] pour n'afficher que l'éditeur
"""
