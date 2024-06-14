while True:
    try:
        n = input()
    except EOFError: break
    
    sorobov = []
    
    for i in range(len(n)-1, -1, -1):
        d = int(n[i])
        if d < 5:
            p = [1, 1, 1, 1, 1, 0, 1]
            p[4-d] = 0
        else: 
            p = [1, 1, 1, 1, 1, 1, 0]
            p[4-(d-5)] = 0
        sorobov.append(p)
    
    while len(sorobov) < 9:
        sorobov.append([1, 1, 1, 1, 0, 0, 1])
    
    for i in range(7):
        if i == 2:
            print(9*'-')
        s = ''
        for j in range(len(sorobov)-1, -1, -1):
            p = sorobov[j]
            s += str(p.pop())
        print(s)
        
    print()