t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    maior = 0
    soma = 0
    for i in list(map(int, input().split())):
        maior = max(maior, i)
        soma += i
    
    d = soma / x
    if d % 1 != 0: d += 1
    d = int(d)
    print(max(d, maior))