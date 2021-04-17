n = 0
u_n, u_np1, u_np2 = 1, 0, 1
largeur = 32

for _ in range(1000):
    if n == largeur:
        print(f"Il y a {u_n} sommets dans le graphe pour un mur de largeur {largeur}.")
    n += 1
    u_n, u_np1, u_np2 = u_np1, u_np2,   u_n + u_np1


rho_expérimental = u_np1 / u_n
rho_théorique    = 1.32471795724475

print(rho_expérimental / rho_théorique, ", proche de 1 ?")
print("K ≈", u_n / rho_expérimental**n)
