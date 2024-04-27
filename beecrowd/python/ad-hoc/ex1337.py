while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0: break
    
    # É um set
    if a == b == c:
        if a < 13:
            s = [a+1, b+1, c+1]
        else:
            s = ['*']
    
    # É um par
    elif a == b or a == c or b == c:
        if a == b:
            iguais = a
            sozinho = c
        elif a == c:
            iguais = a
            sozinho = b
        elif b == c:
            iguais = b
            sozinho = a
        maior = max(a, b, c)
        
        if iguais < 13 and maior < 13:
            if iguais < sozinho:
                s = [iguais, iguais, maior+1]
            else:
                if iguais - sozinho == 1:
                    s = [iguais, iguais, sozinho+2]
                else:
                    s = [iguais, iguais, sozinho+1]
        elif iguais < 13 and maior == 13:
            s = [1, iguais+1, iguais+1] 
        elif iguais == 13:
            if sozinho < 12:
                s = [sozinho+1, 13, 13]

            else:
                s = [1, 1, 1]
                    
    # É um não-par:
    else:
        s = [1, 1, 2]
        
    s.sort()
    print(*s)