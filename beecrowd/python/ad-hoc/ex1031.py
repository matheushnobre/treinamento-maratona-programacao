while True:
    n = int(input())
    if n == 0: break
    
    m = 0
    ultimaRegiao = -1
    
    while ultimaRegiao != 13:
        m += 1
        regioes = [i for i in range(1, n+1)]
        
        posicao = 0
        while len(regioes) != 1:
            regioes.pop(posicao)
            posicao = (posicao + m - 1) % len(regioes)
        ultimaRegiao = regioes.pop()
    
    print(m)