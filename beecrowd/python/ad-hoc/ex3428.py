n = int(input())
lista = list(map(int, input().split()))
control = [0] * (10**6+1)

s = 0
for i in lista:
    if control[i] == 0:
        s += 1
    control[i] = max(0, control[i]-1)
    control[i-1] += 1
    
print(s)