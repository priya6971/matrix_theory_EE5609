# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:49:36 2020

@author: Priya Bhatia
"""

from sympy import Matrix, Rational

Mat = Matrix([[1, 0],[Rational(5,12), 0],[0, 1]])

p_inverse = Mat.pinv()

print(p_inverse)