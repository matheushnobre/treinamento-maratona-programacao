while True:
    n = int(input())
    if n == 0: break
    
    while True:
        original = [i for i in range(1, n+1)]
        vagoes = list(map(int, input().split()))
        if vagoes == [0]: 
            print()
            break
        
        s = 'Yes'
        pilha = []
        for v in vagoes:
            while original and original[0] <= v:
                pilha.append(original[0])
                del original[0]
            if pilha[-1] != v:
                s = 'No'
            del pilha[-1]
        
        print(s)        