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

a,b = -1., 1.            # l'intervalle
k_max = 10             # On va faire l'approximation en découpant en
                        # 2^k morceaux pour k=0,1...k_max

N = 2**np.arange(k_max) # pour avoir 2^{0,1,2,3,4...k_max} -- un tableau
                        # de type np.array
h = (b-a)/N             # c'est aussi un tableau

Q = np.zeros_like(N,dtype=np.float) # Alloue un tableau de la même
                                    # taille que N, initialisé à 0, pour
                                    # stocker les quadratures
E = np.zeros_like(N,dtype=np.float) # Même chose, pour stocker les
                                    # erreurs
Q1 = np.zeros_like(N,dtype=np.float)
E1 = np.zeros_like(N,dtype=np.float)
Q2 = np.zeros_like(N,dtype=np.float)
E2 = np.zeros_like(N,dtype=np.float)
Q3 = np.zeros_like(N,dtype=np.float)
E3 = np.zeros_like(N,dtype=np.float)
Q4 = np.zeros_like(N,dtype=np.float)
E4 = np.zeros_like(N,dtype=np.float)
Q5 = np.zeros_like(N,dtype=np.float)
E5 = np.zeros_like(N,dtype=np.float)
Q6 = np.zeros_like(N,dtype=np.float)
E6 = np.zeros_like(N,dtype=np.float)
Q7 = np.zeros_like(N,dtype=np.float)
E7 = np.zeros_like(N,dtype=np.float)
 #Pour le monome de degré 0,1,2: f(x) = 1,x,x^2
#for k in np.arange(3):
#    print("test pour le degré {}".format(k))
#    f.degre = k # degré des monomes à tester
#    I = f.primitive_monome(b)-f.primitive_monome(a) # intégrale exacte
#                                                    # puisqu'on connait
#                                                    # une primitive
#    # Boucle sur les découpages
#    for i in np.arange(k_max):
#        Q[i] = q.met_trapezes(f.monome,a,b,N[i])
#        E[i] = I-Q[i]
#        print ("{:5d} {:14.8g} {:14.8g} {:14.8g}".format(N[i],I,Q[i],E[i]))
#    # On peut tracer les courbes d'erreur en fonction de N, en échelles
#    # logarithmiques (suivant x et y)
#    plt.loglog(N,E,'+-',label="monome de degré {}".format(k))
#
## Les trois courbes (pour 1, x, x^2) ont été tracées, on ajoute titre,
## légende...
#plt.title("Test de convergence méthode des trapèzes sur 1, x, x^2")
#plt.legend()
#plt.xlabel("N")
#plt.ylabel("Erreur")
#plt.grid()
## Utilisez une des deux lignes ci-dessous pour voir à l'écran ou enregistrer le graphique
## plt.show() 
#plt.savefig("../img/test_3.png")

I0=f.prim_abso(b)-f.prim_abso(a)
I1=f.prim_trig(b)-f.prim_trig(a)
I2=f.exp(b)-f.exp(a)
I3=f.prim_pol(b)-f.prim_pol(a)
for i in np.arange(k_max):
        Q[i] = q.pt_milieu(f.abso,a,b,N[i])
        E[i] = abs(I0-Q[i])
        Q1[i] = q.pt_milieu(f.trig,a,b,N[i])
        E1[i] = abs(I1-Q1[i])
        Q2[i] = q.pt_milieu(f.exp,a,b,N[i])
        E2[i] = abs(I2-Q2[i])
        Q3[i] = q.pt_milieu(f.pol,a,b,N[i])
        E3[i] = abs(I3-Q3[i])
        Q4[i] = q.met_trapezes(f.abso,a,b,N[i])
        E4[i] = abs(I0-Q4[i])
        Q5[i] = q.met_trapezes(f.trig,a,b,N[i])
        E5[i] = abs(I1-Q5[i])
        Q6[i] = q.met_trapezes(f.exp,a,b,N[i])
        E6[i] = abs(I2-Q6[i])
        Q7[i] = q.met_trapezes(f.pol,a,b,N[i])
        E7[i] = abs(I3-Q7[i])
        print ("{:5d} {:14.8g} {:14.8g} {:14.8g}".format(N[i],I0,Q[i],E[i]))
plt.subplot(211)
plt.title("Erreur des fonctions pour la méthode du point milieu")
plt.xlabel("N")
plt.ylabel("Erreur")
plt.grid()
# Utilisez une des deux lignes ci-dessous pour voir à l'écran ou enregistrer le graphique
#plt.loglog(N,E,E1,E2,E3,'+-',label="fonctions")
plt.loglog(N,E,label='|x|')
plt.loglog(N,E1,label='cos(x)')
plt.loglog(N,E2,label='exp(x)')
plt.loglog(N,E3,label='1/1+x²')
plt.legend()
plt.subplot(212)
plt.title("Erreur des fonctions pour la méthode des trapèzes")
plt.xlabel("N")
plt.ylabel("Erreur")
plt.grid()
plt.loglog(N,E4,label='|x|')
plt.loglog(N,E5,label='cos(x)')
plt.loglog(N,E6,label='exp(x)')
plt.loglog(N,E7,label='1/1+x²')
plt.legend()
plt.tight_layout()
plt.savefig("../img/test_3.png")
plt.show()
