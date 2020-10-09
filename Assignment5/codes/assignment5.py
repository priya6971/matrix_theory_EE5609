#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def parab_gen(y):
    y = 3/2-x**2/2
    return y

omat = np.array([[0,1],[-1,0]])
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
x = np.linspace(-5, 5, 100)

def line_dir_pt(m,A,k1,k2):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(k1,k2,len)
    for i in range(len):
        temp1 = A + lam_1[i]*m
        x_AB[:,i]= temp1.T
    return x_AB

#parabola parameters
V = np.array(([1,0],[0,0]))
u = np.array(([0,1]))
ut = u[np.newaxis, :].T
f = -3
p = np.array(([0,1]))
p1t = p[np.newaxis, :].T

# Eigenvalues and eigenvectors
# D_vec,P = LA.eig(V)
# D = np.diag(D_vec)
# print(D,P)
P = np.array(([0,1],[1,0]))
#Generating the Standard parabola
y = parab_gen(x)
# 2y + x**2 = 3
xStandardparab = np.vstack((x,y))
#

#Affine Parameters
R =  np.array(([0,1],[1,0]))
eta = (u@p1t)[0]
# print("eta",eta)
cA = np.vstack((u+(eta*p),V))
cb = np.vstack((-f,(eta*p1t-ut).reshape(-1,1)))
# print(cA)
# print(cb)
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()
yStandardparab = np.vstack((x,y))
yActualparab = P@xStandardparab + c[:,np.newaxis]
#


#Tangent analysis
q = np.array(([1,1]))
m = np.array(([1,-1]))
n = np.array(([1,1]))
# q = q.reshape(-1,1)
#Generating the tangent
k1 = 8
k2 = -8
x_AB = line_dir_pt(m,q,k1,k2)
#

#Generating the normal
k1 = 8
k2 = -8
x_CD = line_dir_pt(n,q,k1,k2)
#

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='Tangent')

#Plotting all lines
plt.plot(x_CD[0,:],x_CD[1,:],label='Normal')

#Plotting the actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Parabola',color='y')
# plt.plot(xActualparab[0,:],xActualparab[1,:],label='Parabola',color='r')
plt.scatter(1,1)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()


# In[ ]:





# In[ ]:




