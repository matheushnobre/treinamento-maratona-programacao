while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    
    t = input().split()
    b, v = [], []
    
    for i in t:
        if i not in b:
            b.append(i)
        elif i not in v:
            v.append(i)
        
    print(len(v))