def qualehopai(x, pai):
    if x != pai[x]:
        pai[x] = qualehopai(pai[x], pai)  
    return pai[x]

n, k = map(int, input().split())
pai = [i for i in range(n+1)]

for _ in range(k):
    i, a, b = input().split()
    a, b = int(a), int(b)
    if i == 'C':
        if qualehopai(a, pai) == qualehopai(b, pai):
            print('S')
        else:
            print('N')
    else:
        pai[qualehopai(b, pai)] = qualehopai(a, pai)
