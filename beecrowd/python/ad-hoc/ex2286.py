t=1
while True:
    n = int(input())
    if n == 0: break
    
    j1 = input()
    j2 = input()
    print(f'Teste {t}')
    for i in range(n):
        a, b = map(int, input().split())
        if (a+b) % 2 == 0: print(j1)
        else: print(j2)
    print('')
    t += 1