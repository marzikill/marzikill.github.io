def est_premier(n):
    "Renvoie un booléen, True si n est premier, False sinon"
    if n <= 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def _test_est_premier():
    for n in range(29):
        assert est_premier(n) == (n in [2, 3, 5, 7, 11, 13, 17, 19, 23])


def quantité_premiers(n):
    "Renvoie la quantité de nombres premiers jusqu'à n"
    return sum(1 for k in range(2, n+1) if est_premier(k))
