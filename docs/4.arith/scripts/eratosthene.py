def est_premier(n):
    "Renvoie un booléen, True si n est premier, False sinon"
    if n <= 1:
        return False
    for d in range(2, n):
        if d * d > n: # ie d > √(n)
            return True
        if n % d == 0:
            return False
    return True

def _test_est_premier():
    for n in range(29):
        assert est_premier(n) == n in [2, 3, 5, 7, 11, 13, 17, 19, 23]


def Ératosthène(n):
    """
    Renvoie le crible des nombres premiers inférieurs ou égaux à n.
    crible[k] vaut True ou False, suivant que k est premier ou non.
    """
    if n < 0:
        return []
    crible = [True] * (n+1)
    crible[0] = False
    if n >= 1:
        crible[1] = False
    p = 2
    while p * p <= n:
        if crible[p]:
            for k in range(p * p, n+1, p):
                crible[k] = False
        p += 1
    return crible

def _test_Érathostène():
    for n in range(1000):
        crible = Ératosthène(n)
        for k in range(1, n+1):
            assert crible[k] == est_premier(k), f"Avec {n=}, et {k=}"


def quantité_premiers(n):
    "Renvoie la quantité de nombres premiers jusqu'à n"
    crible = Ératosthène(n)
    return sum(1 for x in range(2, n+1) if crible[x])
