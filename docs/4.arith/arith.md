# La quantité de nombres premiers

Auteur : Franck CHAMBON

Il y a une infinité de nombres premiers.

!!! cite "Le théorème d'Euclide"
    - $2$ est un nombre premier.
    - On suppose que l'ensemble des nombres premiers est fini.
        + Notons $N$ le produit de ces nombres, où il y a au moins le facteur $2$.
        + $N>1$ d'après le point précédent, et donc $N+1>2$.
        + Soit $p$ le plus petit facteur premier de $N+1$.
        + Par définition, il divise $N$ mais ne divise pas $1$, donc ne peut pas diviser $N+1$.
    - Contradiction, il y a une infinité de nombres premiers.

Cependant, il y a un nombre fini de nombres premiers jusqu'à $n$ quand $n$ est fixé.

!!! faq "L'hypothèse de Riemann"
    La répartition des nombres premiers et sa connaissance fine est en lien direct avec la célèbre [Hypothèse de Riemann](https://fr.wikipedia.org/wiki/Hypoth%C3%A8se_de_Riemann).

    - L'article Wikipédia (en anglais) [*Prime-counting function*](https://en.wikipedia.org/wiki/Prime-counting_function) fournit vite de nombreuses informations à ce sujet.[^1]
    - [Une entrée du blog](https://scienceetonnante.com/2019/10/04/lhypothese-de-riemann/) de David Louapre (Science étonnante) en montre quelques aspects.[^2]

[^1]: Article Wikipédia (en anglais) [*Prime-counting function*](https://en.wikipedia.org/wiki/Prime-counting_function)

[^2]: Article du blog de David Louapre [(Science étonnante) ; sur l'hypothèse de Riemann](https://scienceetonnante.com/2019/10/04/lhypothese-de-riemann/)

Montrons différents algorithmes pour calculer la quantité nombres premiers jusqu'à $n$, pour $n$ fixé.

## Méthode par force brute

### Avec un premier test de primalité

!!! note "Définition : nombre premier"
    Un entier $n>1$ est premier si ses seuls diviseurs sont $1$ et lui-même.

{{ py('brute1') }}

```py3
>>> _test_est_premier()
>>> e = 4
>>> n = 10**e
>>> f"Il y a {quantité_premiers(n)} nombres premiers jusqu'à 10^{e}."
"Il y a 1229 nombres premiers jusqu'à 10^4."
```

!!! info "Tester ses fonctions"
    - On conseille d'écrire des fonctions.
    - D'écrire des fonctions qui testent ces fonctions.
    - `assert` vérifie la condition suivante.
        - Si elle est vérifie, le programme continue normalement.
        - Si elle n'est pas vérifiée,
            - le programme s'arrête, et
            - on peut essayer de trouver l'origine du problème.
    - C'est une très bonne méthode à avoir !

!!! abstract "Complexité de cet algorithme"
    - L'appel à la fonction `est_premier(x)` a un coût en $\mathcal O(x)$ ; dans le pire des cas ($x$ un nombre premier), la boucle fait presque $x$ tours à coûts constants.
    - L'appel à la fonction `quantité_premiers(n)` a donc un coût majoré par $\mathcal O \left(\sum\limits_{x=2}^{n-1} x\right)$, qui est en $\mathcal O\left(n^2\right)$.
    - Mais en pratique, la boucle fait un tour complet uniquement pour les nombres premiers, dont on sait que la proportion parmi les nombres de $1$ à $n$ est environ $\dfrac{n}{\ln n}$. Ce qui conduit à la minoration du coût en $\mathcal O\left(\dfrac{n^2}{\ln n}\right)$.
    - En conclusion, la complexité est ici presque quadratique, il est alors possible de l'utiliser raisonnablement jusqu'à $n \approx 10^4$.

### En améliorant le test de primalité

!!! tip "Propriété d'arithmétique"
    Un nombre composé $n$ possède un diviseur strict inférieur à $\sqrt n$.

    Sa contraposée nous sera utile :

    - Si un nombre $n>1$ ne possède aucun diviseur strict inférieur à $\sqrt n$, alors $n$ est un nombre premier.

Il suffit d'ajouter deux lignes au code précédent :


{{ script('py3 hl_lines="6 7"', 'scripts/brute2.py') }}

```py3
>>> _test_est_premier()
>>> e = 5
>>> n = 10**e
>>> f"Il y a {quantité_premiers(n)} nombres premiers jusqu'à 10^{e}."
"Il y a 9592 nombres premiers jusqu'à 10^5."
```

!!! abstract "Complexité de cet algorithme"
    - L'appel à la fonction `est_premier(k)` a un coût en $\mathcal O(\sqrt k)$ ; dans le pire des cas ($k$ un nombre premier), la boucle fait presque $\sqrt k$ tours à coûts constants.
    - L'appel à la fonction `répartition_premiers(n)` a donc un coût majoré par $\mathcal O \left(\sum\limits_{k=2}^{n-1} \sqrt k\right)$, qui est en $\mathcal O\left(n^{3/2}\right)$.
    - Mais en pratique, la boucle fait un tour complet uniquement pour les nombres premiers, dont on sait que la proportion parmi les nombres de $1$ à $n$ est environ $\dfrac{n}{\ln n}$. Ce qui conduit à la minoration du coût en $\mathcal O\left(\dfrac{n^{3/2}}{\ln n}\right)$.
    - Concrètement, la complexité est **un peu meilleure**, il est alors possible de l'utiliser raisonnablement jusqu'à $n \approx 10^5$.

!!! faq "Comment être plus efficace ?"
    Pour être plus efficace, il faut pouvoir donner la primalité des nombres ==par paquets, et non plus de manière individuelle==.
    
    C'est un **principe général à retenir** en algorithmique.

## Utilisation du crible d'Ératosthène

Le crible d'Ératosthène permet d'**obtenir la liste de tous les nombres premiers** jusqu'à une certaine limite.

!!! note "nombre composé"
    - $0$ et $1$ ne sont ni premiers, ni composés. *Remarque : le statut pour $1$ a varié au cours du temps.*
    - Un entier supérieur à $1$ est soit premier, soit composé.
    - Un entier composé $n$ s'écrit $d\times k$ avec $d, k$ entiers et $1 < d\leqslant k < n$.

Pendant le crible d'Ératosthène, on marque $0$, $1$ non premiers, puis tous les nombres composés jusqu'à une certaine limite, ne laissant non marqués que les nombres premiers.

!!! tip "Propriété 1"
    Si $n>1$ alors
    
    - $n$ possède au moins un diviseur distinct de $1$, et
    - le plus petit d'entre eux est premier.
    
    ??? abstract "Preuve"
        - $n>1$ divise $n$, donc
            - l'ensemble des diviseurs de $n$ distincts de $1$ est non vide.
        - Soit $p$ le plus petit d'entre eux.
        - On suppose que $p$ est composé,
            - il s'écrit $k\times d$ avec $d, k$ entiers et $1 < d\leqslant k < n$,
            - or $d$ est aussi un diviseur distinct de $n$ de $1$
            - ceci contredit la minimalité de $p$.
        - Ainsi $p$ est premier.

!!! tip "Propriété 2"
    Si $n>1$ est composé, alors son plus petit facteur premier $p$ vérifie

    - $p^2\leqslant n$

    ??? abstract "preuve"
        - $n=p×k$, avec $k$ qui est aussi un diviseur de $n$ distinct de $1$,
        - par minimalité de $p$, on a $p\leqslant k$, donc
        - $p×p\leqslant p×k$, d'où $p^2\leqslant n$.

!!! done "Propriété utile"
    On en déduit que tous les entiers composés inférieurs à $n$ possèdent un diviseur premier inférieur à $\sqrt n$.

!!! example "Crible en animation, jusqu'à 120"
    ![crible animé d'Ératosthène](crible.gif)
    
    *Source* : [Wikipédia](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne)

    Une fois les multiples de $2$ marqués, on marque les multiples de $3$, puis de $5$, puis de $7$. Il est inutile de marquer les multiples de $11$ en vertu de la propriété 2 ; $11^2 = 121 > 120$.

    Quand on commence à marquer les multiples de $p$ premier, il suffit de commencer à $p^2$, en effet tous les nombres composés inférieurs à $p^2$ ont déjà été marqués ; ils possèdent un diviseur premier inférieur à $p$, toujours en vertu de la propriété 2.

!!! info "Motivation"
    Cette méthode, le crible d'Ératosthène, possède une bonne complexité, et sa simplicité lui permet de nombreuses variations et optimisations.
    
    En pratique cette méthode est plus rapide que d'autres cribles, plus délicats à implémenter, ayant pourtant une meilleure complexité théorique.

    Cette méthode est aussi une base de réflexion pour construire d'autres cribles : **on peut parfois construire globalement un tableau de valeurs** d'une fonction sur un intervalle, plutôt que de calculer individuellement chaque valeur.
    
    ==Ces méthodes sont efficaces et génériques.==

### Implémentation

!!! abstract "Comprendre le code `Ératosthène` proposé ci-dessous"
    - On donne la *docstring*.
    - On initialise une liste de booléens `crible`, on fait comme si tous les entiers étaient premiers, ils sont marqués à `True`.
    - On marque $0$ et $1$ comme non premiers, avec  `False`.
    - On fait une boucle pour $p$ partant de $2$, en incrémentant $p$ de $1$ à chaque tour :
        - si $p$ est premier, alors on va marquer tous les entiers $k$ multiples de $p$ à partir de $p^2$ comme composés.
        - `range(p*p, n+1, p)` donne exactement les multiples de p allant de $p^2$ inclus, jusqu'à $n$ inclus.
    - Quand $p^2 > n$, on est sûr d'avoir marqué tous les composés ; d'après la propriété 2.

{{ py('eratosthene') }}

```py3
>>> n = 100
>>> crible = Ératosthène(n)
>>> premiers = [p for p in range(n) if crible[p]]
>>> f"La liste des nombres premiers jusqu'à {n} : {premiers})"
La liste des nombres premiers jusqu'à 100 : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>> e = 7
>>> n = 10**e
>>> f"Il y a {quantité_premiers(n)} nombres premiers jusqu'à 10^{e}."
Il y a 664579 nombres premiers jusqu'à 10^7.
```

### Complexités

#### Complexité du crible d'Ératosthène

!!! warning "Uniquement compréhensible en post-bac"
    Le nombre d'opérations élémentaires pour faire ce crible sur les entiers inférieurs ou égaux à $n$ est :

    $$\sum_{p=2}^{\sqrt n} \frac {n-p^2} {p\ln p} \sim \int_{2}^{\sqrt n} \frac {n-x^2}{x\ln x} \mathrm{d}x \sim n\ln(\ln n)$$

    ??? done "Preuve personnelle"
        Avec la probabilité $\ln p$, $p$ est premier, et dans ce cas, on raye des nombres de $p^2$ à $n$, par pas de $p$.
        
        Ensuite on obtient un équivalent sous forme d'intégrale, et le [résultat attendu](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithmic_complexity).

    Ainsi, la complexité est :
    
    - quasi-linéaire en temps : $\Theta\left(n \ln(\ln n)\right)$,
    - et linéaire en espace.

#### Complexité pour le compte de nombres premiers

Faire le compte à la fin est plus rapide que le crible, ainsi on obtient une complexité finale en $\Theta\left(n \ln(\ln n)\right)$ avec cette méthode.

!!! faq "Peut-on faire mieux ?"
    En pratique, on a pu compter la quantité de nombres premiers jusqu'à $10^7$ avec ce code simple en Python et en quelques secondes. Il est possible de l'améliorer un peu :

    - En travaillant par tranches pour utiliser moins de mémoire, et donc rester dans la mémoire cache de l'ordinateur ; calculs bien plus rapides. On parle de crible par segments (*segmented sieve*).
    - En utilisant une autre structure de données que la liste d'entiers Python. Il vaudra mieux utiliser les `bytearray`.
    - En ne considérant que $2$, puis les nombres impairs : on gagne un facteur $2$ en espace et en temps.
    - En mettant à part $2$ et $3$, les nombres premiers sont de la forme $6k±1$, où $k\in\mathbb N^*$. Ce qui peut faire gagner encore un peu de temps et d'espace.
    - On pourrait continuer un peu ainsi ; avec $2$, $3$ et $5$ à part, les nombres premiers sont congrus à $±1$, $±7$, $±11$, ou $±13$ modulo $30$. Ces considérations s'avèrent **contre-productives en Python**, où un code avec un style plus fonctionnel sera plus rapide qu'un code élaboré au style impératif. La raison étant que les parties fonctionnelles sont traitées avec des fonctions bien plus rapides, écrites en C, optimisées et compilées. On réservera donc ces considérations d'optimisation pour un code écrit en C, par exemple.

    On peut alors, avec Python, _sans trop de mal_, aller jusqu'à $n = 10^9$ en moins d'une minute.
    Pour une description détaillée d'une implémentation très efficace en `C++`, on se référera à [cet article en anglais](https://github.com/kimwalisch/primesieve/wiki/Segmented-sieve-of-Eratosthenes).

    ??? faq "Peut-on faire **nettement** mieux ?"
        OUI !

## L'algorithme de Meissel-Lehmer

* [Ernst Meissel](https://fr.wikipedia.org/wiki/Ernst_Meissel) (1826-1895) était un astronome et mathématicien allemand.
* [Derrick Lehmer](https://fr.wikipedia.org/wiki/Derrick_Lehmer) (1905-1991) était un mathématicien américain.

!!! tip "Pour obtenir la quantité de nombres premiers"
    Seule la quantité de nombres premiers nous intéresse ici, pas la liste des nombres premiers, ni même un tableau de booléens. En s'inspirant du crible d'Ératosthène, on va compter le nombre de nombres non rayés, sans en faire la liste !

!!! example "Un peu d'histoire"
    La méthode initiée par Meissel, simplifiée par Lehmer en 1959, a été ensuite améliorée en 1985 par Lagarias, Millerand et Odlyzko.

    Un papier de [M. Deleglise et J. Rivat](https://www.ams.org/journals/mcom/1996-65-213/S0025-5718-96-00674-6/S0025-5718-96-00674-6.pdf) en fait l'écho. Le compte des nombres premiers jusqu'à $10^{18}$ a pu alors être effectué.
    
    En 2001, Xavier Gourdon a encore amélioré la méthode pour atteindre $10^{22}$.
    
    Actuellement les travaux de [Kim Walish](https://github.com/kimwalisch/primecount) ont permis d'atteindre un record à $10^{27}$.

### La méthode

!!! note "Les entiers lisses"
    Notons $Q(n, B)$ le nombre d'entiers dans $[\![2..n]\!]$ qui restent après avoir rayé tous les multiples $kp$ pour $p\leqslant B$, et $k>1$.

!!! example "Exemples"
    - $Q(100, 1) = 99$ ; seuls $0$ et $1$ sont rayés.
    - $Q(100, 2) = 50$ ; il reste $2$ et $3, 5, 7, 9, 11, \cdots 99$.
    - $Q(100, 10) = 25$; il ne reste que les nombres premiers inférieurs à $100$.

!!! faq "Comment calculer $Q(n, B)$ ?"
    - $Q(n, 1) = n-1$ ; aucun nombre n'a été rayé.
    - Si $B$ est composé, alors $Q(n, B) = Q(n, B-1)$ ; on ne raye rien.
    - Si $B^2 > n$, alors $Q(n, B) = Q(n, B-1)$ ; tous les composés inférieurs à $n$ ont déjà été rayés. Il ne reste que des nombres premiers.

Il reste donc uniquement à déterminer $Q(n, p)$, pour $p$ premier inférieur ou égal à $\sqrt n$.

!!! faq "Quels sont les nombres rayés associés au nombre premier $p$ ?"
    Il s'agit des nombres $p\times k$ où $k\in [\![2..n/p]\!]$ avec $k$ dont le seul diviseur inférieur à $p$ est $1$.

!!! example "Exemple"
    - À l'étape $p=5$, on raye les nombres : $5\times 5,5\times 7,5\times 11, 5\times 13, 5\times 17,\cdots, 5\times 25,\cdots,5\times 35,5\times 37,\cdots$ 
    - Il s'agit de rayer le produit de $5$ par : $5, 7, 11, 13, 17,\cdots, 25,\cdots, 35, 37,\cdots$

!!! abstract "De manière générale"
    - La liste précédente est l'ensemble des nombres non rayés avant l'étape $p$, que l'on limite à $n/p$, et sans compter les nombres premiers inférieurs à $p$.
    - La quantité de nombre premiers inférieurs à $p$ est $Q(p-1, p-1)$.
    - La quantité de nombres non rayés avant l'étape $p$, limité à $n/p$, est $Q(n/p, p-1)$.

!!! done "Conclusion"
    On en déduit que pour $p$ premier inférieur ou égal à $\sqrt{n}$ :

    $$Q(n, p) = Q(n, p-1) - (Q(n/p, p-1) - Q(p-1, p-1))$$

    On rappelle que si $p$ n'est pas premier, on a : $Q(n, p) = Q(n, p-1)$ pour tout $n$.

!!! tip "Astuces"
    Ceci nous pousse naturellement à utiliser de la **programmation dynamique**.

    On garde un ensemble de valeurs $Q(m, p-1)$ pour $m$ variés.
    
    On en déduira un ensemble de valeurs $Q(m, p)$ pour les mêmes $m$.

    Les valeurs de $m$ nécessaires sont les nombres $k$ inférieurs ou égaux à $\sqrt n$ et les quotients entiers $n/k$ toujours pour $k$ inférieur ou égal à $\sqrt n$.

    On stocke ces valeurs dans un dictionnaire.

### Implémentation

{{ py('meissel-lehmer') }}

```py3
>>> _test_quantité_premiers()
>>> e = 10
>>> n = 10**e
>>> f"Il y a {quantité_premiers(n)} nombres premiers jusqu'à 10^{e}."
Il y a 455052511 nombres premiers jusqu'à 10^10.
```

!!! done "Victoire"
    Nous avons obtenu assez rapidement la réponse pour $n=10^{10}$.

### Toujours un peu plus loin

La complexité de ce code est proche de $n^{0.75}$.

Cette méthode a été très nettement améliorée ; nous l'avons évoqué plus haut.

Mais elle est aussi très intéressante, car elle peut être **légèrement modifiée**, non pas pour compter les nombres premiers, mais pour en **faire la somme** (ou la somme des carrés), jusqu'à une certaine limite, sans déterminer la liste pour autant.

!!! danger "Pour les motivés"
    Nous proposons deux problèmes raisonnables en difficulté où le lecteur pourra confronter ses idées d'implémentation :

    1. [Calcul de la somme des nombres premiers jusqu'à $N$](https://www.spoj.com/problems/SUMPRIM1/).
    2. [Calcul du dernier nombre premier quand la somme précédente est donnée](https://www.spoj.com/problems/SUMPRIM2/).

    Il y a aussi des liens vers des exercices d'entraînement, plus accessibles.
