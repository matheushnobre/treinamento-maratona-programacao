def fat(n):
    f = 1
    for i in range(n):
        f *= i+1
    return f

while True:
    try:
        p = input()
        f = fat(len(p))
        
        d = 1
        v = []
        for l in p:
            if l not in v:
                d *= fat(p.count(l))
                v.append(l)
        print((f//d) % 1000000007)
            
    except EOFError:
        break