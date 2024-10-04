from math import sqrt
saidas = [0] * 51

n = 50
hastes = [[] for _ in range(n)]
num = 0
while True:
    num += 1
    adicionou = False
    for j in range(n):
        if hastes[j]:
            if sqrt(hastes[j][-1] + num) % 1 == 0:
                hastes[j].append(num)
                adicionou = True
                break
        else:
            saidas[j] = num-1 
            hastes[j].append(num)
            adicionou = True
            break
    if not adicionou: break
saidas[50] = num - 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(saidas[n])