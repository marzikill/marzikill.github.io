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

def quantité_premiers(n):
    """Renvoie la quantité de nombres premiers inférieurs ou égaux à n.
    Utilisation de l'algorithme de Meissel-Lehmer.
    """
    if n <= 1:
        return 0
    r = int(n**0.5) # partie entière de racine carrée de n
    m_lst = [n//k for k in range(1, r+1)]
    m_lst += [k for k in range(m_lst[-1]-1, 0, -1)]
    p = 1
    Q = {m: m-1 for m in m_lst}
    for p in range(2, r+1):
        if Q[p-1] < Q[p]: # p est premier
            qp = Q[p-1] # quantité de premiers inférieurs à p
            p2 = p*p
            for m in m_lst:
                if m < p2:
                    break
                Q[m] -= Q[m//p] - qp
    return Q[n]

def _test_quantité_premiers():
    for n in range(100):
        assert quantité_premiers(n) == \
            sum(1 for x in range(2, n+1) if est_premier(x)), n
