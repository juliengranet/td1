# -*- coding: utf-8 -*-

import numpy as np
import cmath as math
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
    xm=a+np.arange(n)*h
    xm1=a+(np.arange(n)+1)*h
    Q=(h/2)*(np.sum(f(xm))+np.sum(f(xm1)))
    return Q                   

def met_simpson(f,a,b,n):
    h=(b-a)/n
    xm=a+np.arange(n)*h
    xm1=a+(np.arange(n)+0.5)*h
    xm2=a+(np.arange(n)+1)*h
    Q=(h/6)*np.sum(f(xm)+4*f(xm1)+f(xm2))
    return Q

def met_GL(f,a,b,n,o):
    h=(b-a)/n
    if o==2:
        xm=a+(np.arange(n)+(3-math.sqrt(3))/6)*h
        xm1=a+(np.arange(n)+(3+math.sqrt(3))/6)*h
        Q=(h/2)*np.sum(f(xm)+f(xm1))
    if o==3:
        xm=a+(np.arange(n)+(5-math.sqrt(15))/10)*h
        xm1=a+(np.arange(n)+0.5)*h
        xm2=a+(np.arange(n)+(5+math.sqrt(15))/10)*h
        Q=(h/18)*np.sum(5*f(xm)+8*f(xm1)+5*f(xm2))
    return Q