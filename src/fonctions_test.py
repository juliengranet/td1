# -*- coding: utf-8 -*-

import numpy as np
import cmath as math
# On définit ici des fonctions qui permettent de vérifier la précision
# et l'ordre de convergence des formules de quadrature. Pour chaque
# fonction, on définit donc sa primitive.

degre = 0 # degré des polynôme

def monome(x):
    """fonction monome x^k, pour vérifier l'ordre théorique des
    quadratures. Par défaut k=0.

    """
    return x**degre

def primitive_monome(x):
    """primitive de la fonction x^k. Par défaut k=0."""

    return x**(degre+1)/(degre+1.)
def abso(x):
    return np.abs(x)
def prim_abso(x):
    return 0.5*x*np.abs(x)
def trig(x):
    return np.cos(x)
def prim_trig(x):
    return np.sin(x)
def exp(x):
    return np.exp(x)
def pol(x):
    return 1/(1+x^2)
def prim_pol(x):
    return math.atan(x)
# Définir ici les autres fonctions utilisées pour des tests et leurs
# primitives si elles sont connues
