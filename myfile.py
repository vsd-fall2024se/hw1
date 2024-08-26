import numpy as np

A = np.ones((5, 5))


A[:, 1] = 5


s=[]
for i in range(5):
    sm=0
    for j in range(5):
      sm+=A[i][j]
    s.append(sm)
prin(s)