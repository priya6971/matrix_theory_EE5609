#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


A = np.array([[158,-378],[-378,152]])


# In[5]:


print(A)


# In[6]:


b = np.array([-74,-604])


# In[7]:


print(b)


# In[8]:


z = np.linalg.solve(A,b)


# In[9]:


print(z)


# In[ ]:




