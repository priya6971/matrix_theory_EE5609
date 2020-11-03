# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:44:04 2020

@author: Priya Bhatia
"""

import numpy as np


# Method to define Row Reduced Echelon Form
def reducedRowEchelonForm(z):
    # rowEchelonForm(z)
    r, c = z.shape
    row = r - 1

    while row > 0:
        i = row
        for j in range(c):
            if z[i, j] == 1:
                while i > 0:
                    z[i - 1] -= z[i - 1, j] * z[row]  
                    i -= 1
        row = row - 1
    return z



# Method to find Row Echelon Form:-
def rowEchelonForm(a):
    rows, columns = a.shape
    if rows == 0 or columns == 0:
        return a  

    for i in range(len(a)):  
        if a[i, 0] == 0:
            continue
        else:
            break
    else:  
        b = rowEchelonForm(a[:, 1:])  
        return np.hstack([a[:, :1], b])

    if i > 0:  
        ithRow = a[i].copy()
        a[i] = a[0]
        a[0] = ithRow

    a[0] = a[0] / a[0][0]  
    a[1:] = a[1:] - a[1:, 0:1] * a[0]  

    b = rowEchelonForm(a[1:, 1:]) 
    c = np.hstack([a[1:, :1], b])  
    return np.vstack([a[:1], c])  



# Method to find Inverse of the matrix
def inversematrix(m):
    row, col = m.shape

    if row != col:
        return print("Its NOT a square matrix,Therefore Inverse does not exist")
    elif np.linalg.det(m) == 0:
        return print("Inverse does not exist when determinant is zero")
    else:
        concatenatedMatrix = np.hstack([m, np.identity(row)])  
        rowEchelonForm(concatenatedMatrix)
        reducedRowEchelonForm(concatenatedMatrix)
        rInv, cInv = concatenatedMatrix.shape
        cInv = int(cInv / 2)
        return print("The Inverse is: \n", concatenatedMatrix[:, cInv:])


# Given Test Cases
A = np.array([[1,0,2,1,-1],[-1,2,-4,2,0],[2,-1,5,2,1],[2,1,3,5,2]])

# Function Calling
inverse = A.copy()
rowEchelonForm(A)
reducedRowEchelonForm(A)
print("The row reduced echelon form is: \n", A)
#inversematrix(inverse)
