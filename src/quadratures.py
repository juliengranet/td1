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
