while True:
    s, b = map(int, input().split())
    if s == b == 0: break
    sm = []
    
    for i in range(b):
        l, r = map(int, input().split())
        for i in range(l, r+1):
            sm.append(i)
        
        se, sd = '*', '*'
        c = l-1
        while se == '*' and c > 0:
            if c not in sm:
                se = c
            c -= 1
                
        c = r+1
        while sd == '*' and c <= s:
            if c not in sm:
                sd = c
            c += 1
            
        print(se, sd)
        
    print('-')