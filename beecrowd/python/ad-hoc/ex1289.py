t = 1
while True:
    n = int(input())
    if n == 0: break
    l = [int(i) for i in input().split()]
    
    print(f'Teste {t}')
    for i, p in enumerate(l):
        if i+1 == p:
            print(i+1)
            break
    print('')
    t += 1