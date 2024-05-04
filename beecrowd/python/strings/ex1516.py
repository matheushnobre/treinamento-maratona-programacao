while True:
    n, m = map(int, input().split())
    if n == m == 0: break
    
    img = []
    for i in range(n):
        img.append(input())
    a, b = map(int, input().split())
    a, b = a//n, b//n
    
    novo = []
    for linha in img:
        nl = []
        for c in linha:
            nl += c*b
        for i in range(a):
            novo.append(nl)
            
    for linha in novo:
        print(''.join(linha))
    print('')