
# coding: utf-8

# In[1]:


import numpy as np
x = np.array([1, 2, 3, 5])
x
N = 3
np.vander(x, N)
np.column_stack([x**(N-1-i) for i in range(N)])
x = np.array([1, 2, 3, 5])
np.vander(x)
np.vander(x, increasing=True)

