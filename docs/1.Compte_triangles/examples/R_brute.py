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

"""
Appuyer sur [⛭ Exécuter], puis
à droite, dans la console, tester
>>> R_brute(6, 10)
"""
