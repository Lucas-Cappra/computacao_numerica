def metodoLagrange():
    pontos = int(input("Quantidade de pontos que serão utilizados: "))
    X, Y = [],[]
    for i in range(pontos):
        x = float(input("x" + str(i) + " = "))
        X.append(x)
        y = float(input("y" + str(i) + " = "))
        Y.append(y)

    x = float(input("Valor que deseja interpolar: "))
    coeficiente = []
    for indice in range(pontos):
        L = 1
        for j in range(len(X)):
            if indice != j:
                L *=(x - X[j])/(X[indice] - X[j])
        coeficiente.append(L)

    pn = 0
    for i in range(len(coeficiente)):
        pn += Y[i]*coeficiente[i]


    print("p(" + str(x) + ")= ", pn)
metodoLagrange()
#(2.7 ; -3.36) (3.1 ; -3.33) (3.5 ; -2.64) (3.9 ; -1.53) (4.2 ; -0.577) (5.7 ; 2.79) (6.3 ; 2.82)