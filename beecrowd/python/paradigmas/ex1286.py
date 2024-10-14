while True:
    n = int(input())
    if n == 0: break

    tempo = []
    quantidade = []
    p = int(input())
    for _ in range(n):
        tt, qtd = map(int, input().split())
        tempo.append(tt)
        quantidade.append(qtd)
        
    # Ideia da Mochila
    aux = [[0]*(p+1) for _ in range(n+1)] # Cria uma tabela auxiliar para armazenar os resultados
    for i in range(n):
        pizzas = quantidade[i]
        for j in range(p+1):
            if j < pizzas:
                aux[i+1][j] = aux[i][j] # Se não for possível, não adiciona o pedido na mochila
            else:
                aux[i+1][j] = max(aux[i][j], tempo[i] + aux[i][j-pizzas]) # Se for possível, escolhe entre adicionar ou não adicionar o pedido
     
    # Imprime o resultado na tela           
    print(f'{aux[-1][-1]} min.')