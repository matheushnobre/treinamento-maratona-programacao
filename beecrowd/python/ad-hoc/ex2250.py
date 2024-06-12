ct = 0
while True:
    ct += 1
    j = int(input())
    if j == 0: break
    
    tabela = []
    for _ in range(j):
        nome = input()
        pont = 0
        maior = 0
        menor = 1000
        
        for p in input().split():
            pont += int(p)
            menor = min(menor, int(p))
            maior = max(maior, int(p))
        
        pont -= (menor+maior)
        tabela.append([nome, pont])
    
    tabela.sort(key=lambda x: (-x[1], x[0]))
    print(f"Teste {ct}")
    p = 1
    ps = 1
    for index, jog in enumerate(tabela):
        if index != 0:
            if jog[1] == tabela[index-1][1]:
                ps += 1
            else:
                p += ps
                ps = 1
        print(p, jog[1], jog[0])
    print()