import numpy as np

M = np.array([
  [2, 2, 1, 4, 5, 5, ],
  [-2., 3, 1, 1, -4, -4,],
  [6, -9., 2, -2., 17, 15,],
  [2, 17, -3., 21, 3, 3,],
  [4, -1., 20, 15, 42, 27,],
  [-4., 1, 0, 13, 8, -7.,]
])
b = np.array([
  [ 13.],
  [-11.],
  [-25.],
  [ 36.],
  [ 1.],
  [ 21.],
])
def trocaLinha(A, x, y):
    aux = np.copy(A[x,:])
    A[x,:] = np.copy(A[y,:])
    A[y,:] = aux
    return A

A = np.concatenate((M,b),1)
L = np.eye(6,6)

for j in range(5):
    pivo = A[j,j]
    for i in range(j+1,6):
        f = A[i,j]/pivo
        L[i,j] = f
        A[i,:] = A[i,:] - f*A[j,:]

U = A[:,0:6]
c = A[:,6]
c = np.array([c]).T

print("U: \n", U)  #matriz triangular superior
print("c: \n",c)    #matriz 
print("L: \n",L)    #matriz triangular inferior

print("M: \n",M)
print("LxU: \n",L@U)