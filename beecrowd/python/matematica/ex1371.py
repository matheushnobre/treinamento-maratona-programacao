while True:
    n = int(input())
    if n == 0: break
    
    abertos = []
    i = 1
    while i**2 <= n:
        abertos.append(i**2)
        i += 1
            
    print(' '.join(str(aberto) for aberto in abertos))