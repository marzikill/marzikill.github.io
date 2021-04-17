# Pavages d'un rectangle 4×n par des rectangles d'aire 4 {ignore = true}

Auteur : Franck CHAMBON

!!! info "Info MkDocs pour les profs de NSI"
    cette figure est créée avec `ipythonblocs`, c'est du pur HTML et le code est ici inclus :sunglasses:  
    **Avec une macro, sans passer par un fichier temporaire.**

{{ pv_intro() }}


!!! abstract "Description du problème"
    Un rectangle est à côté entier $4×n$.  
    On le pave avec des rectangles à côtés entiers.  
    Chaque petit rectangle est d'aire $4$.  
    Ci-dessus, un exemple de pavage d'un rectangle $4\times 8$.

    [Combien y a-t-il de tels pavages ?](#){ .md-button }


!!! tip "Notation"
    On notera $a_n$ le nombre de pavages pour un rectangle $4\times n$.

!!! info "Les trois motifs"
    Ci-dessous, les rectangles d'aire $4$, à côtés entiers.

{{ trois_motifs() }}


---

!!! abstract "Au programme"
    Ce problème est résolu de manière progressive, et c'est l'occasion d'utiliser :

    - des méthodes de dénombrement de pavages ;
    - des suites récurrentes linéaires (autres que la très classique suite de Fibonacci) ;
    - des algorithmes de calcul de termes d'une telle suite :
        - par calcul successif ;
        - par calcul matriciel ;
        - par calcul polynomial.


## Problème simplifié

- Si on ne pave qu'avec des barres verticales, il n'y a qu'une seule façon de paver un rectangle $4\times n$.
    - $\forall n \in \mathbb N \quad a_n = 1$
- Si on ne pave qu'avec des barres verticales et des carrés, il est facile de voir que $(a_n)_n$ correspond à la suite de Fibonacci décalée, à savoir :
    - $a_0 = a_1 = 1$, et $\forall n \in \mathbb N \quad a_{n+2} = a_{n+1} + a_n$
- Si on a droit à la barre horizontale, le problème devient plus sérieux...


## Cas général

!!! tip "Notation"
    Pour tout $n$ entier, on note :

    - $a_n$ le nombre de pavages d'un rectangle $4\times n$.
    - $b_n$ le nombre de pavages d'un rectangle $4\times n$ modifié :
        - on y ajoute un carré $2\times2$ à droite (en haut ou en bas).
    - $c_n$ le nombre de pavages d'un rectangle $4\times n$ modifié :
        - on y ajoute un carré $2\times2$ à droite au milieu.


{{ rect4x8_0() }}

!!! info "Ci-dessus, un rectangle $4 \times 8$"
    Il y a $a_8$ façons de le paver.

{{ rect4x8_1() }}

!!! info "Ci-dessus, un rectangle $4\times 8$ avec un carré $2\times2$ à droite en bas."
    Il y a $b_8$ façons de le paver.

{{ rect4x8_2() }}

!!! info "Ci-dessus, un rectangle $4\times 8$ avec un carré $2\times2$ à droite au milieu."
    Il y a $c_8$ façons de le paver.

!!! note "À savoir"
    Typiquement, ce genre de problème se résout avec une suite récurrente linéaire.

    - On détermine les premiers termes,
    - puis on établit une formule de récurrence pour $a_n$, $b_n$ et $c_n$.

### Premières valeurs

!!! question "Trouver les premières valeurs et justifier"

    - $a_0$, $a_1$, $a_2$, $a_3$.
    - $b_0$, $b_1$. On calculera ensuite les autres...
    - $c_0$, $c_1$, $c_2$, $c_3$.

??? example "Réponses"
    
    1. $a_n$ pour $n<4$
        - $a_0 = 1$, il y a une unique façon de paver le vide ;
        - $a_1 = 1$, une barre verticale ;
        - $a_2 = 2$, deux barres verticales, ou bien deux carrés ;
        - $a_3 = 3$, trois barres verticales, ou bien deux carrés flanqués d'une barre verticale (à gauche ou à droite).

    2. $b_n$ pour $n<2$
        - $b_0 = 1$, un carré ;
        - $b_1 = 1$, un carré et une barre verticale ;

    3. $c_n$ pour $n<4$
    Pour $n<4$, on ne peut rien mettre d'autre qu'un carré à droite, et alors on a $c_n=a_n$ pour $n<4$.
        - $c_0 = 1$ ;
        - $c_1 = 1$ ;
        - $c_2 = 2$ ;
        - $c_3 = 3$ ;

### Récurrence pour a_n

Il y a plusieurs cas de motifs pour la partie droite d'un pavage de rectangle $4\times n$, avec $n\geqslant 4$ :

1. Il y a une barre verticale ;
2. il y a $4$ barres horizontales ;
3. il y a $2$ carrés ;
4. il y a un carré et deux barres horizontales
    1. carré en haut ;
    2. carré au milieu ;
    3. carré en bas.

Graphiquement, cela donne :


{{ rect4x8_3() }}

Dans ce cas, il y a $a_{n-1}$ façons de paver ce qu'il reste.

---

{{ rect4x8_4() }}

Dans ce cas, il y a $a_{n-4}$ façons de paver ce qu'il reste.

---

{{ rect4x8_5() }}

Dans ce cas, il y a $a_{n-2}$ façons de paver ce qu'il reste.

---

{{ rect4x8_6() }}

Dans ce cas, *par symétrie horizontale*, il y a $b_{n-4}$ façons de paver ce qu'il reste.

---

{{ rect4x8_7() }}

Dans ce cas, il y a $c_{n-4}$ façons de paver ce qu'il reste.

---

{{ rect4x8_8() }}

Dans ce cas, il y a $b_{n-4}$ façons de paver ce qu'il reste.

---

!!! faq "Quel bilan ?"
    Donner une relation de récurrence pour $(a_n)$, pour $n\geqslant 4$.

??? done "Réponse"
    Pour $n\geqslant 4$, on a $a_n = a_{n-1} + a_{n-4} + a_{n-2} + 2b_{n-4} + c_{n-4}$

### Récurrence pour b_n

Il y a plusieurs cas de motifs pour la partie droite d'un pavage de rectangle $4\times n$ flanqué d'un carré à droite en bas, avec $n\geqslant 2$ :

1. il y a un carré ;
2. il y a $2$ barres horizontales.

---

{{ rect4x8_9() }}

> Dans ce cas, il y a $a_{n}$ façons de paver ce qu'il reste.

---

{{ rect4x8_10() }}

Dans ce cas, il y a $b_{n-2}$ façons de paver ce qu'il reste.

---
!!! faq "Quel bilan ?"
    Donner une relation de récurrence pour $(b_n)$, pour $n\geqslant 2$.

??? done "Réponse"
    Pour $n\geqslant 2$, on a $b_n = b_{n-2} + a_{n}$


### Récurrence pour c_n

Il y a plusieurs cas de motifs pour la partie droite d'un pavage de rectangle $4\times n$ flanqué d'un carré à droite au milieu, avec $n\geqslant 4$ :

1. il y a un carré ;
2. il y a $2$ barres horizontales.

{{ rect4x8_11() }}

Dans ce cas, il y a $a_{n}$ façons de paver ce qu'il reste.

---

{{ rect4x8_12() }}

Dans ce cas, il y a $c_{n-4}$ façons de paver ce qu'il reste.

---

!!! faq "Quel bilan ?"
    Donner une relation de récurrence pour $(c_n)$, pour $n\geqslant 4$.

??? done "Réponse"
    Pour $n\geqslant 4$, on a $c_n = c_{n-4} + a_{n}$

## Calcul des valeurs suivantes

On utilise les premières valeurs et les relations de récurrence :

- d'abord pour calculer $b_2$ et $b_3$
    - $b_2 = b_0 + a_2 = 1+2 = 3$
    - $b_3 = b_1 + a_3 = 1+3 = 4$
- ensuite pour calculer des valeurs suivantes.


```python
a = [1, 1, 2, 3]
b = [1, 1, 3, 4]
c = [1, 1, 2, 3]
for n in range(4, 24):
    # On ajoute a[n], puis b[n], puis c[n]
    a.append(a[n-1] + a[n-2] + a[n-4] + 2*b[n-4] + c[n-4])
    b.append(a[n] + b[n-2])
    c.append(a[n] + c[n-4])
```

!!! check "Table des valeurs de $a_n$ pour $n < 24$."


{{ table_a() }}


!!! tip "Résultat"
    On déduit que dans l'exemple d'introduction, il y avait $143$ façons de paver le rectangle $4×8$, avec des rectangles d'aire $4$.

### Relation d'ordre 8 pour a_n

#### D'après OEIS<sup>®</sup>

Sur [*On-Line Encyclopedia of Integer Sequences*](oeis.org), cette suite est référencée sous [A220123](http://oeis.org/A220123). On y découvre une autre relation de récurrence :
> Pour $n\geqslant8$, on a : $-a_{n-8}+a_{n-6}-a_{n-5}+5a_{n-4}+a_{n-2}+a_{n-1} = a_{n}$

On peut vérifier cette relation sur nos valeurs :

```python linenums="10"
for n in range(8, 24):
    assert  -a[n-8] +a[n-6] -a[n-5] +5*a[n-4] +a[n-2] +a[n-1] == a[n], f"Avec {n}"
```

!!! tip "Remarque"
    Pour une suite qui ne serait pas référencée, sur OEIS
    : [l'algorithme de Berlekamp–Massey (*en*)](https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm) permet de déterminer une relation de récurrence en fonction des premiers termes.

#### Preuve de cette relation de récurrence

Pour $n\geqslant 8$, on a :

- $a_n = a_{n-1} + a_{n-4} + a_{n-2} + 2b_{n-4} + c_{n-4} \quad (I)$
- $b_{n-4} = b_{n-6} + a_{n-4} = b_{n-8} + a_{n-6} + a_{n-4}$
- $c_{n-4} = c_{n-8} + a_{n-4}$

On déduit :

- $a_n = a_{n-1} + a_{n-4} + a_{n-2} + 2b_{n-8}+ 2a_{n-6} +2a_{n-4}+ c_{n-8} + a_{n-4}\quad (II)$ 

Or, d'après $(I)$ (valable aussi pour $n\geqslant 4$), on a pour $n\geqslant 8$ :

- $a_{n-4} = a_{n-5} + a_{n-8} + a_{n-6} + 2b_{n-8} + c_{n-8}\quad (III)$

Par soustraction de $(II)$ par $(III)$, on obtient pour $n\geqslant 8$ :

- $a_{n} = -a_{n-8}+a_{n-6}-a_{n-5}+5a_{n-4}+a_{n-2}+a_{n-1}$

!!! check "CQFD."


### Calculs successifs des premiers termes

On ajoute à la liste des valeurs initiales les nouvelles valeurs avec la relation de récurrence.

!!! warning "Estimation de l'empreinte mémoire"
    Dans notre exemple, la valeur suivante est environ le double de la précédente, donc nécessite environ un bit de plus en moyenne. Le stockage de $200\,000$ valeurs prend donc une place mémoire de plus de $20$ milliards de bits ; environ $3$ Go.


{{ script('python', 'scripts/chrono_1.py') }}

```
Durée : 13.51 s
Taille des données : 2.75 Go
Preuve de calcul : 626139179
```



- C'est **la bonne méthode** à employer ==si== on a besoin de (*presque*) tous les premiers termes d'une suite récurrente linéaire.
- La dernière instruction affiche le dernier terme calculé, qui est réellement très grand, modulo un grand nombre premier sur 32bits. Cette *preuve* de calcul a plusieurs utilités :
    - elle initie au calcul modulaire omniprésent en cryptographie,
    - elle permet de vérifier plus aisément des calculs sur de grands nombres par différentes méthodes,
    - ou par différents langages qui ne travaillent pas avec des nombres plus grands que les mots machine.

!!! faq "Comment faire mieux ?"
    Sans stocker toutes les valeurs, juste les huit précédentes, peut-on calculer beaucoup plus de termes ?

    Il suffit de supprimer, avec `del a[0]`, le terme qui devient inutile à chaque tour de boucle. Cette opération permet de conserver une empreinte mémoire faible, donc d'utiliser de la mémoire cache qui est plus rapide que la RAM !!!

{{ script('python', 'scripts/chrono_2.py') }}

```
Durée : 12.23 s
Taille des données : 219.84 ko
Preuve de calcul : 626139179
```

C'est à peine plus rapide, mais l'empreinte mémoire est bien plus faible.


Dans un fichier `outils.py` (que nous donnerons à la fin[^1]), créons une fonction `rec_lin_suc` qui renvoie un terme d'une suite récurrente linéaire par calcul des termes successifs. C'est uniquement pour être plus commode à réutiliser, et améliorer légèrement les performances, ce code étant semi-interprété au lieu de l'être totalement.

[^1]: Ce script mérite une belle discussion.

Utilisation :

{{ script('python', 'scripts/chrono_3.py') }}

```
Durée : 12.29 s
Preuve de calcul : 626139179
```

!!! faq "Faire mieux ?"
    Peut-on calculer un terme lointain plus rapidement avec une autre méthode ?

    - Oui, avec l'exponentiation rapide de matrices.
    - Oui, avec l'exponentiation rapide modulaire de polynômes.


### Calcul matriciel d'un terme lointain

Dans le code précédent, les deux instructions :

```python
a.append(sum(ai * ri for ai, ri in zip(a, r)))
del a[0]
```

peuvent être traduites sous forme matricielle par :

$a \leftarrow aM$,

-  où $M$ est la [matrice compagnon](https://fr.wikipedia.org/wiki/Matrice_compagnon) associée au polynôme unitaire $P(X) = 1 - X^2 + X^3 -5X^4 - X^6 - X^7 + X^8$ ;
- et où $a$ est un vecteur ligne.
- On a :
    - $P(X) = 0 \iff X^8 = -1 + X^2 - X^3 +5X^4 + X^6 + X^7$
    - La dernière colonne de la matrice est notre vecteur de la relation de récurrence linéaire.


$$
M = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & -1 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & -1 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 5 \\
0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
\end{pmatrix}
$$

Avec $a = (a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7)$, on a pour $n\in \mathbb N$ :

$$aM^n = (a_{n}, a_{n+1}, a_{n+2}, a_{n+3}, a_{n+4}, a_{n+5}, a_{n+6}, a_{n+7})$$

De sorte que l'on peut calculer plus rapidement $a_n$ avec l'exponentiation rapide de matrices.

!!! hint "À savoir"
    Si la récurrence est d'ordre $d$,

    - le temps de calcul est en $\Theta(d^3 \log n)$ opérations élémentaires (pas secondes) ;
    - l'empreinte mémoire est en $\Theta(d^2)$ coefficients (pas bits) ;
    - **Attention**, les coefficients peuvent être de grands nombres, et donc le temps de calcul peut ne pas être en $\Theta(d^3 \log n)$...

!!! tip "Concrètement"
    Comparons avec notre exemple et avec un code non optimisé inclus dans notre petit module `outils.py` (que nous donnons en annexe).

{{ script('python', 'scripts/chrono_4.py') }}

```
Durée : 2.12 s
Preuve de calcul : 626139179
```

!!! done "Encore mieux ?"
    On peut faire mieux en travaillant avec des polynômes.



### Calcul polynomial d'un terme lointain

Nous avons pu déterminer un terme de rang $n$ d'une suite récurrente linéaire d'ordre $d$ en regardant un élément du vecteur calculé avec $a\times M^n$, où $a$ est le vecteur des termes initiaux, et $M$ la matrice compagnon associée à la récurrence.

Le calcul de $M^n$ coûte $\Theta(d^3\times \log n)$ opérations élémentaires (entre des entiers dont la taille peut devenir très grande...)

On peut réduire sérieusement le coût en considérant que $M$ possède $P$ comme polynôme minimal, le polynôme associé à la récurrence, et que l'on peut calculer $Q_n = X^n \pmod P$, par exponentiation rapide ; le coût est $\Theta(d^2\times \log n)$. Il suffit d'évaluer $Q_n$ en $M$ au lieu de $X^n$ en $M$ afin d'obtenir $M^n$.


Mieux encore, on peut se passer totalement de la matrice $M$.

- On a besoin de la première colonne de $M^i$ pour $i\in [\![0..d[\![$,
- or il s'agit d'un simple vecteur colonne $(\delta_{i,j})_{j \in [\![0..d[\![}$ (0-indexation).

!!! abstract "En résumé"
    Avec $Q_n = X^n \pmod P$, qui s'écrit : $q_0 + q_1X + \cdots + q_{d-1}X^{d-1}$

    On a : $a_n = a_0\times q_0 + a_1\times q_1 + \cdots + a_{d-1}\times q_{d-1}$

{{ script('python', 'scripts/chrono_5.py') }}

```
Durée : 0.26 s
Preuve de calcul : 626139179
```

!!! done "Conclusion"
    L'exponentiation rapide de polynômes modulo la relation de récurrence permet d'avoir une bien meilleure complexité temporelle.

    Si la récurrence est d'ordre $d$ :

    - le temps de calcul est en $\Theta(d^2 \log n)$ opérations élémentaires (pas en secondes) ;
    - l'empreinte mémoire est en $\Theta(d^2)$ coefficients (pas bits) ;
    - **Attention**, les coefficients peuvent être de grands nombres, et donc le temps de calcul (en secondes donc) peut ne pas être en $\Theta(d^2 \log n)$...


!!! faq  "Peut-on faire mieux ?"

    - Oui, avec la [transformation de Fourier rapide](https://fr.wikipedia.org/wiki/Transformation_de_Fourier_rapide) (FFT) qui permet de faire la multiplication de deux polynômes de taille $d$ en $\Theta(d\log d)$ au lieu de $\Theta(d^2)$. Cela dépasse largement le niveau de ce papier.
    - Oui, si l'on fait du calcul modulaire en lieu et place du calcul sur les grands entiers. Il y a plusieurs justifications :

        - Posséder plusieurs résidus permet de reconstruire le grand nombre avec le théorème des restes chinois.
        - Le calcul des résidus est parallélisable ; un par machine.
        - Le calcul modulaire est pédagogique, et omniprésent en cryptographie.
        - Le calcul modulaire est possible facilement avec la plupart des langages tant que le modulo tient sur un mot machine. Par contre le calcul sur les grands entiers est plus délicat, en C par exemple.
        - Le calcul modulaire peut faire office de preuve de calcul dans la recherche de nouveaux algorithmes ou les exercices d'algorithmiques.




## Quelques problèmes similaires

Voici une liste d'exercices, souvent difficiles à résoudre avec Python, autour des suites récurrentes linéaires.

Plusieurs problèmes de pavages sont indiqués en suivant ce lien : [M5TILE](https://www.spoj.com/problems/M5TILE/).

- Il y en a des plus faciles, comme [M3TILE](https://www.spoj.com/problems/M3TILE/) et [M4TILE](https://www.spoj.com/problems/GNY07H/).
- Il y en a des plus durs, comme [MNTILE](https://www.spoj.com/problems/MNTILE/), [DOJ1](https://www.spoj.com/problems/DOJ1/) et [DOJ2](https://www.spoj.com/problems/DOJ2/).


!!! info "Des problèmes variés, de pavage ou non"
    L'énoncé est en anglais. Dans le tableau suivant, édité en mars 2020,

    - *Solvers* indique une forme de difficulté ; le nombre de participants qui ont résolu le problème. Attention, beaucoup de participants utilisent le langage C.
    - Le temps (*Time*) indique un temps personnel (le mien, en Python3) avec un code optimisé. **C'est souvent le temps à battre.**
    - Un titre en gras indique un problème particulièrement difficile en Python3 ; une première résolution en C étant conseillée.
    - *Py3Solvers* indique le nombre de personnes ayant réussi avec Python3.
    - Un symbole :fontawesome-solid-home: indique un problème créé par votre serviteur.

|Title|Solvers|Time|Py3Solvers|
|:----|:-----:|---:|:-------:|
|[Fibonacci Sum](https://www.spoj.com/problems/FIBOSUM/)|5227|0.02s|[43](https://www.spoj.com/ranks/FIBOSUM/lang=PYTH%203.2.3)
|[Just Add It](https://www.spoj.com/problems/ZSUM/)|3985|0.01s|[19](https://www.spoj.com/ranks/ZSUM/lang=PYTH%203.2.3)
|**[Recursive Sequence](https://www.spoj.com/problems/SEQ/)**|2110|1.12s|[4](https://www.spoj.com/ranks/SEQ/lang=PYTH%203.2.3)
|**[Flibonakki](https://www.spoj.com/problems/FLIB/)**|785|0.08s|[2](https://www.spoj.com/ranks/FLIB/lang=PYTH%203.2.3)
|**[Recursive Sequence (Version II)](https://www.spoj.com/problems/SPP/)**|710|0.04s|[2](https://www.spoj.com/ranks/SPP/lang=PYTH%203.2.3)
|[Arya Rage](https://www.spoj.com/problems/MNNITAR/)|310|0.02s|[2](https://www.spoj.com/ranks/MNNITAR/lang=PYTH%203.2.3)
|**[Nacci Fear](https://www.spoj.com/problems/NACCI/)**|283|0.28s|[2](https://www.spoj.com/ranks/NACCI/lang=PYTH%203.2.3)
|[Fun with numbers](https://www.spoj.com/problems/NUMPLAY/)|263 | 0.01s|[27](https://www.spoj.com/ranks/NUMPLAY/lang=PYTH%203.2.3)
|[Sum of products](https://www.spoj.com/problems/SUMMUL/)|255|0.02s|[6](https://www.spoj.com/ranks/SUMMUL/lang=PYTH%203.2.3)
|**[Sum of Tetranacci numbers](https://www.spoj.com/problems/TETRAHRD/)**|217|0.07s|[1](https://www.spoj.com/ranks/TETRAHRD/lang=PYTH%203.2.3)
|**[Fibonacci With a Square Root](https://www.spoj.com/problems/FIBOSQRT/)**|139|2.73s|[2](https://www.spoj.com/ranks/FIBOSQRT/lang=PYTH%203.2.3)
|**[R Numbers](https://www.spoj.com/problems/ITRIX12E/)**|181|0.02s|[3](https://www.spoj.com/ranks/ITRIX12E/lang=PYTH%203.2.3)
|**[Easy Sequence!](https://www.spoj.com/problems/SEQAGAIN/)**|136|0.32s|[2](https://www.spoj.com/ranks/SEQAGAIN/lang=PYTH%203.2.3)
|**[Blocks for kids](https://www.spoj.com/problems/PBOARD/)**|75|0.07s|[1](https://www.spoj.com/ranks/PBOARD/lang=PYTH%203.2.3)
|**[Snaky Numbers](https://www.spoj.com/problems/SNAKYNUM/)**|73|0.08s|[1](https://www.spoj.com/ranks/SNAKYNUM/lang=PYTH%203.2.3)
|**[Grid Tiling](https://www.spoj.com/problems/BTCODE_J/)**|18|0.11s|[1](https://www.spoj.com/ranks/BTCODE_J/lang=PYTH%203.2.3)
|:fontawesome-solid-home: [Moon Safari (Hard)](https://www.spoj.com/problems/MOON2/)|15|23.32s|[0](https://www.spoj.com/ranks/MOON2/lang=PYTH%203.2.3)
|:fontawesome-solid-home: [100pct failure in 72 hours](https://www.spoj.com/problems/HAL9000/)|4|0.32s|[1](https://www.spoj.com/ranks/HAL9000/lang=PYTH%203.2.3)


Des challenges (amélioration de la constante) sur ce genre de problèmes :

- :fontawesome-solid-home: [The SPP constant challenge](https://www.spoj.com/problems/SPPC/)
- :fontawesome-solid-home: [Matrix Exponentiation](https://www.spoj.com/problems/MATEX/)

Des problèmes difficiles sur les suites, en général.

|Title|Solvers|Time|Py3Solvers|
|:----|:-----:|---:|:--------:|
|[A Summatory (HARD)](https://www.spoj.com/problems/ASUMHARD/)|52|0.77s|[1](https://www.spoj.com/ranks/ASUMHARD/lang=PYTH%203.2.3)
|[Pibonacci](https://www.spoj.com/problems/PIB/)|41|0.54s|[5](https://www.spoj.com/ranks/PIB/lang=PYTH%203.2.3)
|[Hofstadter–Conway 10000 dollar sequence](https://www.spoj.com/problems/HC10000/)|5|0.48s|[1](https://www.spoj.com/ranks/HC10000/lang=PYTH%203.2.3)

Et voici d'autres [problèmes](https://www.spoj.com/problems/FRANCKY/) essentiellement d'arithmétique. Des problèmes qui m'ont personnellement fait grandement progresser à la fois en mathématiques, et en informatique.

!!! danger "Problèmes récents ; :warning: impossible avec Python."
    - [MOON4](https://www.spoj.com/problems/MOON4/)
    - [SPP3](https://www.spoj.com/problems/SPP3/)

## ANNEXE : `fichier outils.py`

{{ script('python', 'scripts/outils.py') }}

