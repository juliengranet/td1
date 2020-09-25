# Première initiation à git, python, markdown en programmant des formules de quadrature en python

## Introduction
Ce fichier fait en même temps office d'énoncé du travail et de compte
rendu. Il doit donc être complété au cours de la séance, au fur et à
mesure que vous réalisez le travail. Les modifications de ce fichier
[./README.md](./README.md) et des fichiers modifiés et ajoutés par
exemple dans les répertoires [./src](./src) ou [./img](./img) doivent
donc être décrit dans l'historique du dépôt git, à travers une série de
*commit* les plus simples possible (dits *atomiques*).

Ce fichier est rédigé, et doit être complété en utilisant le formatage
*markdown*.

Ce travail me permet d'évaluer
- vos capacités initiales de programmation en python
- votre capacité à utiliser un document mathématique pour réaliser un
  programme
- votre capacité à apprendre un nouveau formalisme (*python* et surtout *markdown*)
- vos compétences techniques relatives à l'utilisation de git
- vos capacités à documenter avec un niveau de détail adapté votre
  travail. 

*Il n'est pas nécessaire d'aller au bout des questions de programmation
(le niveau de départ en programmation au sein du groupe est très
hétérogène), l'essentiel est que j'ai la possibilité de comprendre quels
sont vos acquis sur les points ci-dessus.*

**À la fin de votre travail, il est donc capital de pousser (*git push*)
  vos modifications sur le serveur, afin que je puisse les voir**

## Avant de commencer
* prenre connaissance, brièvement, du [langage
Markdown](https://guides.github.com/features/mastering-markdown) propre
à la plateforme Github.

Si vous lisez ceci, c'est que vous avez:

- un compte sur la plateforme github.com, et un email validé de
  l'Université (IDNum)

- utilisé le lien déposé sur moodle, et accepté la création automatique
  d'un dépôt git contenant ce répertoire de travail.

## Première partie: environnement de travail et initiation à Python

1. Une fois le dépôt créé, vous le voyez sur votre compte github (en
ligne). Vous pouvez donc récupérer l'adresse et commencer à travailler
(*git clone <url à récupérer en ligne>*).

2. N'oubliez pas de configurer git si nécessaire: *git config --list,
git config --local user.{name,email}* pour regler vos identifiant et
adresse email..

3. Préparez votre environnement de travail: éditeur de texte (*emacs*,
*vim*, *atom*...) et terminaux (terminal par défaut du système, pour git
et pour l'interpréteur *ipython3*), ou bien environnement de
développement intégré (comme *spyder3* ou *pycharm*). 

Détaillez ci-dessous votre choix d'environnement de travail et les
raisons de ce choix.

J'ai choisi d'utiliser spyder3 pour effectuer le tp car c'est un logiciel que j'ai l'habitude d'utiliser pour coder en python depuis l'an dernier

4. Puisque vous avez apporté des modifications cohérentes (réponse à la
question 3. ci-dessus), validez ces modifications (*git add* et *git
commit -m "..."*).

5. Familiarisez vous avec le contenu du répertoire, qui devrait
ressembler à :
    
```
├── README.md
├── img
│   └── test_1.png
├── src
│   ├── fonctions_test.py
│   ├── quadratures.py
│   └── tests.py
└── tex
    ├── memo_quadratures.pdf
    ├── memo_quadratures.tex
```

Quel est la nature (langage ?) et le rôle (texte, programme, autre) de
chacun des fichiers présents ?

1.Le rôle du fichier README.md est de décrire la nature des divers fichiers accessibles à l'utilisateur, il est écrit en Markdown

2.test_1.png est un graphique représentant la convergence de la méthode du point milieu en fonction du degré du monôme, l'image est donnée par un code en python

3.fonction_test.py est un code en python qui définit des fonctions vérifiant la précision et l'ordre de convergeance des formules de quadratures

4.quadratures.py est un code en python donnant la quadrature de f par la méthode du point milieu

5.test.py est un code en python qui compare l'application des méthodes précédentes sur l'intervalle [0;1] de différents monômes. Le code créer ensuite l'image test_1.png pour comparer la convergence.

6.memo_quadratures.tex en est fichier écrit en LaTeX qui explique les propriétés des divers formules de quadratures

7.memo_quadratures.pdf est la version pdf du fichier précédent.


**Pensez à valider régulièrement votre travail, et à pousser les
  changements sur le serveur (*git push*) de temps en temps et surtout à
  la fin de la séance de travail**

## Deuxième partie: formules de quadrature

### Exemple: brève analyse de l'ordre de la formule du point milieu
Le programme fournit permet de tester la formule du point milieu sur les
monomes (puissance 0, 1, 2). Les résultats obtenus sont donnés dans le
tableau et le graphe ci-dessous:

n   | erreur x^0 | erreur x^1 | erreur x^2
--- | ---------- | ---------- | ----------
1   |          0 |          0 | 8.333e-02
2   |          0 |          0 | 2.083e-02
4   |          0 |          0 | 51208e-03
8   |          0 |          0 | 1.302e-03
16  |          0 |          0 | 3.255e-04
32  |          0 |          0 | 8.138e-05
64  |          0 |          0 | 2.035e-05
128 |          0 |          0 | 5.086e-06
256 |          0 |          0 | 1.272e-06
512 |          0 |          0 | 3.179e-07

![Illustration de l'ordre de la méthode du point
milieu](./img/test_1.png)

L'erreur est nulle pour l'intégration des fonctions $x^0$ et $x^1$ car
la formule utilisée est exacte pour les polynômes jusqu'au degré 1. La
courbe ne s'affiche donc pas (en échelle logarithmique, $0$ est à
$-\infty$). 

Pour la fonction $x^2$, on voit que l'erreur décroit proportionnellement
à $1/n^2$: elle est divisée par 4 à chaque fois que $n$ est multiplié
par 2 (dans le tableau) ou encore est divisée par 10^2 chaque fois que
$n$ est multiplié par 10 (visible sur le graphe). C'est cohérent avec la
théorie pour une formule composée d'ordre 1.

### Programmation et analyse d'autres formules

1. En suivant le modèle de la formule du point milieu, dans le fichier
[./src/quadratures.py](./src/quadratures.py) programmer la méthode des
trapèzes (programmer une autre fonction dans le même fichier
[./src/quadratures.py](./src/quadratures.py)).

2. Tester cette nouvelle quadrature en utilisant comme modèle le
programme [./src/tests.py](./src/tests.py): vérifier que cette formule
calcul de manière exacte les intégrales de polynomes de degré au plus 1,
et commet une erreur équivalente à $h^2$ (ou encore
$N^{-2}$). Reproduire ci-dessous les tableaux d'erreurs qui démontrent
ce résultat, et inclure le graphe de convergence des approximations.

n   | erreur x^0 | erreur x^1 | erreur x^2
--- | ---------- | ---------- | ----------
1   |          0 |          0 | 1.3333333
2   |          0 |          0 | 0.33333333
4   |          0 |          0 | 0.083333333
8   |          0 |          0 | 0.020833333
16  |          0 |          0 | 0.0052083333
32  |          0 |          0 | 0.0013020833
64  |          0 |          0 | 0.00032552083
128 |          0 |          0 | 8.1380208e-05
256 |          0 |          0 | 2.0345052e-05
512 |          0 |          0 | 5.086263e-06

![Illustration de l'ordre de la méthode des trapèzes](./img/test_2.png)

Il n'y a pas d'erreur en dessous du degré 2, ce qui confirme que la méthode permet d'intégrer exactement les polynômes d'un degré inférieur à 2.
On voit que la pente de l'erreur est de 2. La méthode des trapèzes est donc d'ordre 2.

3. On veut tester nos formules pour d'autres fonctions que les
polynômes. Pour cela, on ajoute les fonctions souhaitées dans le fichier
[./src/fonctions_test.py](./src/fonctions_test.py). En suivant le modèle
donné pour les monomes, programmer les fonctions, et une de leurs
primitives
 - $f(x) = |x|$ et $g(x) = 0.5*x*|x|$;
 - $f(x) = cos(x)$ et $g(x) = sin(x)$;
 - $f(x) = exp(x)$ et $g(x) = exp(x)$;
 - $f(x) = 1/(1+x^2)$ et $g(x) = atan(x)$.

4. Produire une unique figure qui compare les graphes de convergence de
l'erreur pour ces nouvelles fonctions integrées sur l'intervalle
$[-1,1]$ avec les méthodes du point milieu et des trapèzes. Insérez
l'image ci-dessous, et faites tous les commentaires utiles.
Pour plus de précision, donnez un tableau comparatif des erreurs commise
pour chacune de ces fonctions pour les deux méthodes.

![Illustration de l'ordre de la méthode des trapèzes et du point commun](./img/test_3.png)


On remarque que ces graphes sont pratiquement identiques, les deux méthodes convergent donc à la même vitesse (elles sont donc d'ordre 2, d'après la question 2.)

##Tableau comparatif d'erreur pour la méthode du point milieu

  n | abs(x)     | cos(x)        | exp(x)         | 1/(1+x^2)
--- | ---------- |  ----------   | ----------     | ---------- 
1   |          0 | 0.31705803    | 0.35040239     | 0.42920367
2   |          0 | 0.072223154   | 0.095150457    | 0.029203673
4   |          0 | 0.017659321   | 0.024306003    | 0.010380144
8   |          0 | 0.0043906638  | 0.0061097001   | 0.0026039324
16  |          0 | 0.0010961649  | 0.0015295128   | 0.000651038
32  |          0 | 0.00027394755 | 0.00038250889  | 0.00016276036
64  |          0 | 6.8481035e-05 | 9.5635394e-05  | 4.0690103e-05
128 |          0 | 1.7119893e-05 | 2.3909359e-05  | 1.0172526e-05
256 |          0 | 4.2799504e-06 | 5.9773717e-06  | 2.5431315e-06
512 |          0 | 1.0699862e-06 | 1.4943449e-06  | 6.3578288e-07

##Tableau comparatif d'erreur pour la méthode des trapèzes

  n | abs(x)     | cos(x)        | exp(x)         | 1/(1+x^2)
--- | ---------- |  ----------   | ----------     | ---------- 
1   |          0 | 0.60233736    | 0.73575888     | 0.57079633
2   |          0 | 0.14263966    | 0.19267825     | 0.070796327
4   |          0 | 0.035208255   | 0.048763895    | 0.020796327
8   |          0 | 0.0087744669  | 0.012228946    | 0.0052080915
16  |          0 | 0.0021919016  | 0.0030596231   | 0.0013020795
32  |          0 | 0.00054786834 | 0.00076505514  | 0.00032552077
64  |          0 | 0.0001369604  | 0.00019127312  | 8.1380207e-05
128 |          0 | 3.4239681e-05 | 4.7818864e-05  | 2.0345052e-05
256 |          0 | 8.5598942e-06 | 1.1954753e-05  | 5.086263e-06
512 |          0 | 2.1399719e-06 | 2.9886904e-06  | 1.2715658e-06

5. Programmez maintenant la méthode de Simpson et les méthodes de
Gauss-Legendre à 2 et 3 points (voir le document
[./tex/memo_quadratures.pdf](./tex/memo_quadratures.pdf)). 

  1. Expliquez la stratégie de programmation retenue.
  
  J'ai codé séparément chaques méthodes en me basant sur le modèle de celle fournie dans le fichier de départ (méthode du point milieu)
  
  2. Vérifiez numériquement que les formules intègrent exactement les
polynomes de degré au plus 3 (Simpson, Gauss-Legendre à 2 points) ou 5
(Gauss-Legendre à 3 points).

  En dehors de ce qui me semble être des zéros machines (erreurs à 10^-17), les méthodes intègrent exactement les polynômes de degré 3 à 5.
  
  3. Calculez numériquement l'ordre de convergence de ces méthodes
     (graphes et tableaux).
  
  ## Méthode de Simpson
  
  n   | erreur x^2 | erreur x^3 | erreur x^4
--- | ---------- | ---------- | ----------
1   |          0 |          0 | 0.26666667
2   |          0 |          0 | 0.016666667
4   |          0 |          0 | 0.0010416667
8   |          0 |          0 | 6.5104167e-05
16  |          0 |          0 | 4.0690104e-06
32  |          0 |          0 | 2.5431315e-07
64  |          0 |          0 | 1.5894572e-08
128 |          0 |          0 | 9.9341069e-10
256 |          0 |          0 | 6.2088112e-11
512 |          0 |          0 | 3.8804515e-12  

![Illustration de l'ordre de la méthode de Simpson](./img/test_simpson.png) 

On voit que la pente de la courbe est d'environ 4. On peut donc dire que l'ordre de convergence de la méthode de Simpson est de 4.

  ## Méthode de Gauss-Legendre à 2 points
  
  n   | erreur x^2 | erreur x^3 | erreur x^4
--- | ---------- | ---------- | ----------
1   |          0 |          0 | 0.17777778
2   |          0 |          0 | 0.011111111
4   |          0 |          0 | 0.00069444444
8   |          0 |          0 | 4.3402778e-05
16  |          0 |          0 | 2.7126736e-06
32  |          0 |          0 | 1.695421e-07
64  |          0 |          0 | 1.0596381e-08
128 |          0 |          0 | 6.6227368e-10
256 |          0 |          0 | 4.1392223e-11
512 |          0 |          0 | 2.5871527e-12 

![Illustration de l'ordre de la méthode de Gauss-Legendre à 2 points](./img/test_GL2.png) 

On voit que la pente de la courbe est d'environ 5. On peut donc dire que l'ordre de convergence de la méthode de Gauss-Legendre à 2 points est de 5.

  ## Méthode de Gauss-Legendre à 3 points
  
  n   | erreur x^4 | erreur x^5 | erreur x^6
--- | ---------- | ---------- | ----------
1   |          0 |          0 | 0.045714286
2   |          0 |          0 | 0.00071428571
4   |          0 |          0 | 1.1160714e-05
8   |          0 |          0 | 1.7438616e-07
16  |          0 |          0 | 2.7247838e-09
32  |          0 |          0 | 4.2574777e-11
64  |          0 |          0 | 6.6530115e-13
128 |          0 |          0 | 1.0436096e-14
256 |          0 |          0 | 1.6653345e-16
512 |          0 |          0 | 5.5511151e-17 

![Illustration de l'ordre de la méthode de Gauss-Legendre à 3 points](./img/test_GL3.png) 

On voit que la pente de la courbe est d'environ 7. On peut donc dire que l'ordre de convergence de la méthode de Gauss-Legendre à 3 points est de 7.     

6. On peut maintenant comparer l'ensemble des méthodes programmées, pour
chacune des fonctions de la question 3. Produisez les tableaux et
graphes d'erreurs que vous jugez utilse et discutez les résultats
obtenus.

**N'oubliez pas de valider les modifications faites le plus souvent
possible (*validations atomiques*), et de documenter intelligiblement
l'historique associé (les messages). Finalement, n'oubliez pas de
pousser votre travail sur le dépôt.**
