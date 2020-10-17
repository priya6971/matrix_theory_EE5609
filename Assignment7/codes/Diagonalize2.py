# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:16:40 2020

@author: Priya Bhatia
"""

from sympy import Matrix, Rational

Mat = Matrix([[1, 0],[Rational(5,12), 0],[0, 1]])

M = Mat.transpose() * Mat
print(M)
P, D = M.diagonalize()

print(P)
print(D)