# PremiÃ¨re initiation Ã  git, python, markdown en programmant des formules de quadrature en python

## Introduction
Ce fichier fait en mÃªme temps office d'Ã©noncÃ© du travail et de compte
rendu. Il doit donc Ãªtre complÃ©tÃ© au cours de la sÃ©ance, au fur et Ã 
mesure que vous rÃ©alisez le travail. Les modifications de ce fichier
[./README.md](./README.md) et des fichiers modifiÃ©s et ajoutÃ©s par
exemple dans les rÃ©pertoires [./src](./src) ou [./img](./img) doivent
donc Ãªtre dÃ©crit dans l'historique du dÃ©pÃ´t git, Ã  travers une sÃ©rie de
*commit* les plus simples possible (dits *atomiques*).

Ce fichier est rÃ©digÃ©, et doit Ãªtre complÃ©tÃ© en utilisant le formatage
*markdown*.

Ce travail me permet d'Ã©valuer
- vos capacitÃ©s initiales de programmation en python
- votre capacitÃ© Ã  utiliser un document mathÃ©matique pour rÃ©aliser un
  programme
- votre capacitÃ© Ã  apprendre un nouveau formalisme (*python* et surtout *markdown*)
- vos compÃ©tences techniques relatives Ã  l'utilisation de git
- vos capacitÃ©s Ã  documenter avec un niveau de dÃ©tail adaptÃ© votre
  travail. 

*Il n'est pas nÃ©cessaire d'aller au bout des questions de programmation
(le niveau de dÃ©part en programmation au sein du groupe est trÃ¨s
hÃ©tÃ©rogÃ¨ne), l'essentiel est que j'ai la possibilitÃ© de comprendre quels
sont vos acquis sur les points ci-dessus.*

**Ã€ la fin de votre travail, il est donc capital de pousser (*git push*)
  vos modifications sur le serveur, afin que je puisse les voir**

## Avant de commencer
* prenre connaissance, briÃ¨vement, du [langage
Markdown](https://guides.github.com/features/mastering-markdown) propre
Ã  la plateforme Github.

Si vous lisez ceci, c'est que vous avez:

- un compte sur la plateforme github.com, et un email validÃ© de
  l'UniversitÃ© (IDNum)

- utilisÃ© le lien dÃ©posÃ© sur moodle, et acceptÃ© la crÃ©ation automatique
  d'un dÃ©pÃ´t git contenant ce rÃ©pertoire de travail.

## PremiÃ¨re partie: environnement de travail et initiation Ã  Python

1. Une fois le dÃ©pÃ´t crÃ©Ã©, vous le voyez sur votre compte github (en
ligne). Vous pouvez donc rÃ©cupÃ©rer l'adresse et commencer Ã  travailler
(*git clone <url Ã  rÃ©cupÃ©rer en ligne>*).

2. N'oubliez pas de configurer git si nÃ©cessaire: *git config --list,
git config --local user.{name,email}* pour regler vos identifiant et
adresse email..

3. PrÃ©parez votre environnement de travail: Ã©diteur de texte (*emacs*,
*vim*, *atom*...) et terminaux (terminal par dÃ©faut du systÃ¨me, pour git
et pour l'interprÃ©teur *ipython3*), ou bien environnement de
dÃ©veloppement intÃ©grÃ© (comme *spyder3* ou *pycharm*). 

DÃ©taillez ci-dessous votre choix d'environnement de travail et les
raisons de ce choix.

*J'ai choisi d'utiliser spyder3 pour effectuer le tp car c'est un logiciel que j'ai l'habitude d'utiliser pour coder en python depuis l'an dernier*

4. Puisque vous avez apportÃ© des modifications cohÃ©rentes (rÃ©ponse Ã  la
question 3. ci-dessus), validez ces modifications (*git add* et *git
commit -m "..."*).

5. Familiarisez vous avec le contenu du rÃ©pertoire, qui devrait
ressembler Ã  :
    
```
â”œâ”€â”€ README.md
â”œâ”€â”€ img
â”‚Â Â  â””â”€â”€ test_1.png
â”œâ”€â”€ src
â”‚Â Â  â”œâ”€â”€ fonctions_test.py
â”‚Â Â  â”œâ”€â”€ quadratures.py
â”‚Â Â  â””â”€â”€ tests.py
â””â”€â”€ tex
    â”œâ”€â”€ memo_quadratures.pdf
    â”œâ”€â”€ memo_quadratures.tex
```

Quel est la nature (langage ?) et le rÃ´le (texte, programme, autre) de
chacun des fichiers prÃ©sents ?

*1.Le rôle du fichier README.md est de décrire la nature des divers fichiers accessibles à l'utilisateur, il est écrit en Markdown

2.test_1.png est un graphique représentant la convergence de la méthode du point milieu en fonction du degré du monôme, l'image est donnée par un code en python

3.fonction_test.py est un code en python qui définit des fonctions vérifiant la précision et l'ordre de convergeance des formules de quadratures

4.quadratures.py est un code en python donnant la quadrature de f par la méthode du point milieu

5.test.py est un code en python qui compare l'application des méthodes précédentes sur l'intervalle [0;1] de différents monômes. Le code créer ensuite l'image test_1.png pour comparer la convergence.

6.memo_quadratures.tex en est fichier écrit en LaTeX qui explique les propriétés des divers formules de quadratures

7.memo_quadratures.pdf est la version pdf du fichier précédent.*

**Pensez Ã  valider rÃ©guliÃ¨rement votre travail, et Ã  pousser les
  changements sur le serveur (*git push*) de temps en temps et surtout Ã 
  la fin de la sÃ©ance de travail**

## DeuxiÃ¨me partie: formules de quadrature

### Exemple: brÃ¨ve analyse de l'ordre de la formule du point milieu
Le programme fournit permet de tester la formule du point milieu sur les
monomes (puissance 0, 1, 2). Les rÃ©sultats obtenus sont donnÃ©s dans le
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

![Illustration de l'ordre de la mÃ©thode du point
milieu](./img/test_1.png)

L'erreur est nulle pour l'intÃ©gration des fonctions $x^0$ et $x^1$ car
la formule utilisÃ©e est exacte pour les polynÃ´mes jusqu'au degrÃ© 1. La
courbe ne s'affiche donc pas (en Ã©chelle logarithmique, $0$ est Ã 
$-\infty$). 

Pour la fonction $x^2$, on voit que l'erreur dÃ©croit proportionnellement
Ã  $1/n^2$: elle est divisÃ©e par 4 Ã  chaque fois que $n$ est multipliÃ©
par 2 (dans le tableau) ou encore est divisÃ©e par 10^2 chaque fois que
$n$ est multipliÃ© par 10 (visible sur le graphe). C'est cohÃ©rent avec la
thÃ©orie pour une formule composÃ©e d'ordre 1.

### Programmation et analyse d'autres formules

1. En suivant le modÃ¨le de la formule du point milieu, dans le fichier
[./src/quadratures.py](./src/quadratures.py) programmer la mÃ©thode des
trapÃ¨zes (programmer une autre fonction dans le mÃªme fichier
[./src/quadratures.py](./src/quadratures.py)).

2. Tester cette nouvelle quadrature en utilisant comme modÃ¨le le
programme [./src/tests.py](./src/tests.py): vÃ©rifier que cette formule
calcul de maniÃ¨re exacte les intÃ©grales de polynomes de degrÃ© au plus 1,
et commet une erreur Ã©quivalente Ã  $h^2$ (ou encore
$N^{-2}$). Reproduire ci-dessous les tableaux d'erreurs qui dÃ©montrent
ce rÃ©sultat, et inclure le graphe de convergence des approximations.

![Illustration de l'ordre de la mÃ©thode des trapèzes](./img/test_2.png)



3. On veut tester nos formules pour d'autres fonctions que les
polynÃ´mes. Pour cela, on ajoute les fonctions souhaitÃ©es dans le fichier
[./src/fonctions_test.py](./src/fonctions_test.py). En suivant le modÃ¨le
donnÃ© pour les monomes, programmer les fonctions, et une de leurs
primitives
 - $f(x) = |x|$ et $g(x) = 0.5*x*|x|$;
 - $f(x) = cos(x)$ et $g(x) = sin(x)$;
 - $f(x) = exp(x)$ et $g(x) = exp(x)$;
 - $f(x) = 1/(1+x^2)$ et $g(x) = atan(x)$.

4. Produire une unique figure qui compare les graphes de convergence de
l'erreur pour ces nouvelles fonctions integrÃ©es sur l'intervalle
$[-1,1]$ avec les mÃ©thodes du point milieu et des trapÃ¨zes. InsÃ©rez
l'image ci-dessous, et faites tous les commentaires utiles.

<<<<<<< HEAD
![Illustration de l'ordre de la méthode des trap�zes et du point commun](./img/test_3_bis.png)
=======
![Illustration de l'ordre de la mÃ©thode des trapèzes et du point commun](./img/test_3_bis.png)
>>>>>>> 5e19d6a444f9bd0105cdf13218251f941023c3ce

On remarque une variation de pente entre les deux méthodes, la méthode du point milieu converge plus vite que celle des trapèzes
Pour plus de prÃ©cision, donnez un tableau comparatif des erreurs commise
pour chacune de ces fonctions pour les deux mÃ©thodes.

5. Programmez maintenant la mÃ©thode de Simpson et les mÃ©thodes de
Gauss-Legendre Ã  2 et 3 points (voir le document
[./tex/memo_quadratures.pdf](./tex/memo_quadratures.pdf)). 

  1. Expliquez la stratÃ©gie de programmation retenue.
  
  2. VÃ©rifiez numÃ©riquement que les formules intÃ¨grent exactement les
polynomes de degrÃ© au plus 3 (Simpson, Gauss-Legendre Ã  2 points) ou 5
(Gauss-Legendre Ã  3 points).
  
  3. Calculez numÃ©riquement l'ordre de convergence de ces mÃ©thodes
     (graphes et tableaux).

6. On peut maintenant comparer l'ensemble des mÃ©thodes programmÃ©es, pour
chacune des fonctions de la question 3. Produisez les tableaux et
graphes d'erreurs que vous jugez utilse et discutez les rÃ©sultats
obtenus.

**N'oubliez pas de valider les modifications faites le plus souvent
possible (*validations atomiques*), et de documenter intelligiblement
l'historique associÃ© (les messages). Finalement, n'oubliez pas de
pousser votre travail sur le dÃ©pÃ´t.**
