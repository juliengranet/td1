# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import quadratures as q    # nos formules de quadrature
import fonctions_test as f # nos fonctions pour faire des tests

# Ce fichier réalise l'ensemble des tests qui sont demandé dans le TP.

# Un premier exemple est donné ci-dessous, qui compare l'intégrale de la
# fonction x^k sur l'intervalle [0,1] avec sa valeur approchée par la
# méthode du point milieu. La comparaisons est faite sur des découpages
# de [0,1] en n=1, 2, 2^2, 2^3,... 2^10 sous-intervalles de même
# longueur, et pour les fonctions f(x)=1, f(x)=x et f(x)=x^2.

a,b = 0., 1.            # l'intervalle
k_max = 10              # On va faire l'approximation en découpant en
                        # 2^k morceaux pour k=0,1...k_max

N = 2**np.arange(k_max) # pour avoir 2^{0,1,2,3,4...k_max} -- un tableau
                        # de type np.array
h = (b-a)/N             # c'est aussi un tableau

Q = np.zeros_like(N,dtype=np.float) # Alloue un tableau de la même
                                    # taille que N, initialisé à 0, pour
                                    # stocker les quadratures
E = np.zeros_like(N,dtype=np.float) # Même chose, pour stocker les
                                    # erreurs

# Pour le monome de degré 0,1,2: f(x) = 1,x,x^2
for k in np.arange(3):
    print("test pour le degré {}".format(k))
    f.degre = k # degré des monomes à tester
    I = f.primitive_monome(b)-f.primitive_monome(a) # intégrale exacte
                                                    # puisqu'on connait
                                                    # une primitive
    # Boucle sur les découpages
    for i in np.arange(k_max):
        Q[i] = q.pt_milieu(f.monome,a,b,N[i])
        E[i] = I-Q[i]
        print ("{:5d} {:14.8g} {:14.8g} {:14.8g}".format(N[i],I,Q[i],E[i]))
    # On peut tracer les courbes d'erreur en fonction de N, en échelles
    # logarithmiques (suivant x et y)
    plt.loglog(N,E,'+-',label="monome de degré {}".format(k))

# Les trois courbes (pour 1, x, x^2) ont été tracées, on ajoute titre,
# légende...
plt.title("Test de convergence méthode du point milieu sur 1, x, x^2")
plt.legend()
plt.xlabel("N")
plt.ylabel("Erreur")
plt.grid()
# Utilisez une des deux lignes ci-dessous pour voir à l'écran ou enregistrer le graphique
# plt.show() 
plt.savefig("../img/test_1.png")

