# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:52:29 2020

@author: Priya Bhatia
"""

from sympy import Matrix, Rational

Mat = Matrix([[1, 0],[Rational(5,12), 0],[0, 1],])

M = Mat * Mat.transpose()
print(M)
P, D = M.diagonalize(0)

print(P)
print(D)