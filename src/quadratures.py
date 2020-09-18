# -*- coding: utf-8 -*-

import numpy as np

def pt_milieu(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode du point milieu sur
    [a,b] découpé en n sous-intervalles égaux.

    """
    h = (b-a)/n
    xm = a + (0.5+np.arange(n))*h
    Q = h*np.sum(f(xm))
    return Q

# Définir ci-dessous les autres méthodes de quadrature

def met_trapezes(f,a,b,n):
    h=(b-a)/n
    xm=(a+np.arange(n)*h)
    Q=(h/2)*(np.sum(f(xm)))
    for i in range(len(xm)-1):
        Q=Q+(h/2)*(f(xm[i+1])) 
    return Q                   

