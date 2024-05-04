camp = []
maior = 0

n, m = map(int, input().split())
for i in range(n):
    l = [int(i) for i in input().split()]
    camp.append(l)
    if sum(l) > maior:
        maior = sum(l)

for j in range(m):
    c = [camp[i][j] for i in range(n)]
    if sum(c) > maior:
        maior = sum(c)

print(maior)