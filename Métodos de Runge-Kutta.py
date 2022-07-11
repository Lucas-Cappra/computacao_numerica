import numpy as np
import matplotlib.pyplot as plt

# Usando o método de Runge Kutta de quarta ordem

def g(x, y):
    return -1.2*y + 7*(np.exp(-0.3*x))
def f(x):
    return (70*np.exp(-0.3*x)/9)-(43*np.exp(-1.2*x)/9)

#a, b, h = float(input("Digite o valor de a, b e h iniciais: "))
a, b, h = 0, 2.5, 0.5
x0, y0 = 0, 3
n = round((b-a)*2)
print(n)
def MRK4(a, b, h, x0, y0, n):
    x, y = x0, y0
    for i in range(0, n+1):
        # iteração 1:
        k1 = g(x, y)
        k2 = g(x+(h/2), y+k1*(h/2))
        k3 = g(x+(h/2), y+ k2*(h/2))
        k4 = g(x+(h), y+k3*h)

        k = (k1+2*k2+2*k3+k4)/6
        y1 = y + k*h
        x1 = x + h

        x, y = x1, y1
        print(f"x e y da iteração {i}: ({x}, {y})")
    return print(f"x e y da iteração {i}: ({x}, {y})")
MRK4(a,b,h,x0,y0,n)