import numpy as np
#tirangular inferior
A = np.array([
  [ 6., -3., -3., 5.],
  [-6.,  2., -4.,-2.],
  [36.,-19.,-28.,28.],
  [ -24., 16.,61.,9.]
])
b = np.array([
  [ -9.],
  [-36.],
  [-120.],
  [ 363.]
])
def triangularInferior(A,b) :
  n,n = np.shape(A) #para matriz quadrada
  x = np.zeros(np.shape(b))  #iniciando vetor de x

  for i in range(n):    # Linha 0 1 2 3 4
    soma = 0
    for j in range(i):  #Coluna 0 1 2 3 4
      soma = soma+A[i,j]*x[j,0]
    x[i,0] = (b[i,0] - soma)/A[i,i]

  return x
x = triangularInferior(A,b)
print(x)

def triangularSuperior(A,b) :
  n,n = np.shape(A) #para matriz quadrada
  x = np.zeros(np.shape(b))  #iniciando vetor de x

  for i in range(n, -1, -1):  # Linha 4 3 2 1 0
    soma = 0
    for j in range(n, -1, -1): #Coluna 4 3 2 1 0 
      soma = soma+A[i,j]*x[j,0]
    x[i,0] = (b[i,0] - soma)/A[i,i]

  return x
x = triangularSuperior(A,b)
print(x)

