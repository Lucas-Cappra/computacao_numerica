def coeficientesNewton():
    quantpontos = int(input('Quantidade de pontos: '))
    pontos, fpontos = [], []
    tabela = [] # para calcular a aproximação.
    for i in range(quantpontos):
        ponto = float(input('x%d = ' %i)) #%d serve para expressar um número inteiro em py.
        fponto = float(input('f(x%d) = '%i))
        pontos.append(ponto)
        fpontos.append(fponto)
    tabela.append(fpontos)  #salva a ordem 0 na tabela.

    x = float(input('Ponto x em que deseja estimar: '))
    print()

    passo = 1
    for n in range(quantpontos - 1): #se o usuario der 3 pontos, o polinomio vai ser de grau 2.
        ordem = []
        for m in range(len(tabela[n]) - 1):
            diferençadividida = (tabela[n][m+1] - tabela[n][m])/(pontos[m+passo] - pontos[m])
            ordem.append(diferençadividida)# qual a ordem?
        tabela.append(ordem) # cada linha guarda uma ordem.
        passo += 1
    for k in range(len(tabela)):
        print('Ordem %d: '%k, tabela[k])
    print()

    aprox = 0 
    grau = 0

    for i in range(len(tabela)):
        fator = tabela[i][0]
        for j in range(grau):
            fator *= (x - pontos[j])
        grau += 1
        aprox += fator
    print(' A aproximação de f(%f) = %f' %(x, aprox))
coeficientesNewton()