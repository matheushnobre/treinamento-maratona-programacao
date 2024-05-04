while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    
    p = []
    for i in range(n):
        p.append(input().split())
    
    c1, c2, c3, c4 = True, True, True, True
    for linha in p:
        if '0' not in linha:
            c1 = False
        if '1' not in linha:
            c4 = False
      
    for j in range(m):
        coluna = [p[i][j] for i in range(n)]
        if '0' not in coluna:
            c3 = False  
        if '1' not in coluna:
            c2 = False
           
    c = c1 + c2 + c3 + c4
    
    print(c)