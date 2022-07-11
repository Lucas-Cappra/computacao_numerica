import numpy as np

A = np.array([
 [15, 3, 3],
 [2, 12, 3],
 [4, 2, -15.]
])

b = [
 [-3.],
 [15.],
 [3]
]

n, nc = np.shape(A)
B = np.eye(3) - np.linalg.inv(np.eye(n)*A)@A
g = np.linalg.inv(np.eye(n)*A)@b
#chute inicial:
x = np.zeros((n,1)) #tamanho de linhas por 1 coluna

#iteração 1
xold = np.copy(x)
x[0,0] = B[0,:]@x + g[0,0]
x[1,0] = B[1,:]@x + g[1,0]
x[2,0] = B[2,:]@x + g[2,0]

Er = np.max(np.abs(x-xold))/np.max(np.abs(x))
print('Valor de x é, \n', x)
print('Valor de Er é, \n', Er)  

#iteração 2
xold = np.copy(x)
x[0,0] = B[0,:]@x + g[0,0]
x[1,0] = B[1,:]@x + g[1,0]
x[2,0] = B[2,:]@x + g[2,0]

Er = np.max(np.abs(x-xold))/np.max(np.abs(x))
print('Valor de x é, \n', x)
print('Valor de Er é, \n', Er)  