while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0: break
    
    if h1 == h2 and m1 == m2: resultado = 0
    elif h1 == h2 and m1 > m2: resultado = 1440 + m2-m1
    elif h1 == h2 and m1 < m2: resultado = m2-m1
    elif h1 < h2: resultado = (h2-h1)*60 + (m2-m1)
    else: resultado = (24-(h1-h2))*60 + (m2-m1) 
    
    print(resultado)