#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
U_1 = np.array(([0,0]))
U_2= np.array(([1,0]))
P_1 = np.array(([1/2,math.sqrt(3)/2]))
P_2 = np.array(([1/2,-math.sqrt(3)/2]))
P_3 = np.array(([1,0]))
P_4 = np.array(([0,0]))
r_1 = np.sqrt(LA.norm(U_1)**2+1)
r_2 = np.sqrt(LA.norm(U_2)**2+0)
x_circ1= circ_gen(U_1,r_1)
x_circ2=circ_gen(U_2,r_2)
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle with centre(1,0)$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle with centre(0,0)$')
plt.scatter(1/2,math.sqrt(3)/2)
plt.scatter(1/2,-math.sqrt(3)/2)
plt.scatter(0,0)
plt.scatter(1,0)
plt.annotate("A", (1/2, math.sqrt(3)/2))
plt.annotate("B", (1/2, -math.sqrt(3)/2))
plt.annotate("O_1", (1,0))
plt.annotate("O_2", (0,0))
plt.plot([0,1/2],[0, math.sqrt(3)/2])
plt.plot([0,1/2],[0, -math.sqrt(3)/2])
plt.plot([1,1/2],[0, math.sqrt(3)/2])
plt.plot([1, 1/2],[0, -math.sqrt(3)/2])
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




