def busca(lista, item):
    inicio = 0
    fim = len(lista)
    meio = (inicio + fim) // 2
    
    maior = 10e10
    indmaior = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio+1
        elif lista[meio] < item:
            inicio = meio+1
        else:
            fim = meio-1
        
        if lista[meio] > item and lista[meio] < maior:
            maior = lista[meio]
            indmaior = meio
    
    if lista[inicio] > item and lista[inicio] < maior:
        maior = lista[inicio]
        indmaior = inicio
            
    return indmaior + 1

t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    lista = list(map(int, input().split()))
    lista.sort(reverse=True)
    saida = []
    soma = 0
    for k in lista:
        soma += k
        saida.append(soma)
    total = soma
    
    for j in range(q):
        qtd = int(input())
        if qtd > total:
            print(-1)
        else:
            print(busca(saida, qtd))