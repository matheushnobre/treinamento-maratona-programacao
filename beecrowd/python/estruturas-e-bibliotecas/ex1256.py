n = int(input())
for i in range(n):
    m, c = map(int, input().split())
    dicio = {i: [] for i in range(m)}
    lista = [int(i) for i in input().split()]
    
    for valor in lista:
        endereco = valor % m
        dicio[endereco].append(valor)
        
    for chave, valor in dicio.items():
        saida = str(chave)+' -> '
        if valor:
            saida += ' -> '.join(str(v) for v in valor)
            saida += ' -> '
        saida += '\\'
        print(saida)
        
    if i != n-1:
        print()