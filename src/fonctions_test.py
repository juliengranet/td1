# -*- coding: utf-8 -*-

import numpy as np

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

# Définir ici les autres fonctions utilisées pour des tests et leurs
# primitives si elles sont connues
