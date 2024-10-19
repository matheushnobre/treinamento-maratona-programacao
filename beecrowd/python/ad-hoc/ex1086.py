def first(m, n, l, tab):
    qtd = 0
    linhas = (m * 100) / l
    inicio = 1
    if linhas % 1 == 0:
        for i in range(int(linhas)):
            if tab[n] > 0:
                qtd += 1
                tab[n] -= 1
            else:
                passou = False
                for j in range(inicio, n//2+2):
                    if tab[j] > 0:
                        if (j != n-j and tab[n-j] > 0) or (j==n-j and tab[j] > 1):
                            qtd += 2
                            tab[j] -= 1
                            tab[n-j] -= 1
                            passou = True
                            inicio = j
                            break
                if not passou:
                    return 100001
    else:
        return 100001
    return qtd

while True:
    m, n = map(int, input().split()) 
    if m == 0: break
    l = int(input()) # em centimetros
    k = int(input()) 
    tab = {i:0 for i in range(1, 10001)}
    for t in input().split():
        tab[int(t)] += 1
    reserva = tab.copy()
    menor = 100001
    
    qtd = first(m, n, l, tab)
    qtd2 = first(n, m, l, reserva)
    menor = min(qtd, qtd2, menor)           
    if menor == 100001:
        print('impossivel')
    else:
        print(menor)